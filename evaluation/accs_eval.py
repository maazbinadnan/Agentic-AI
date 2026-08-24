"""Acceptance Criteria Extraction and Coverage Score (ACCS) Evaluator.

Before evaluating generated code and UI mockups, an evaluator model decomposes
the input user story U into a set of discrete, testable Acceptance Criteria:
    A = {a_1, a_2, ..., a_n}

An LLM-as-a-Judge inspects the generated code C (JavaScript, event handlers, logic)
and rendered DOM D (HTML elements, forms, interactive controls, accessibility attributes)
to verify criterion fulfillment using a verification function v(a_i, C, D) in {0.0, 0.5, 1.0}:
    - 1.0 : Full implementation (UI element present in DOM D AND logic/handlers implemented in code C)
    - 0.5 : Partial implementation (UI element present in DOM D but missing event handling/logic in code C, or vice versa)
    - 0.0 : Non-implementation (criterion is absent from both DOM D and code C)

The Acceptance Criteria Coverage Score (ACCS) is formulated as:
    ACCS = (sum_{i=1}^n v(a_i, C, D)) / |A|
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union, cast
from html.parser import HTMLParser
import pandas as pd

from global_layer.AzureClient import ChatClient
from global_layer.functions import _write_json_file
from evaluation.state.llm_judge_state import (
    AcceptanceCriterion,
    UserStoryDecomposition,
    CriterionVerification,
    UserStoryACCS,
    ACCSEvaluationReport,
)

# Resolve prompt paths relative to this file
_EVAL_DIR = os.path.dirname(os.path.abspath(__file__))
VERIFICATION_PROMPT_PATH = os.path.join(_EVAL_DIR, "prompts", "accs_evaluator.md")
DECOMPOSER_PROMPT_PATH = os.path.join(_EVAL_DIR, "prompts", "accs_decomposer.md")
DEFAULT_MODEL = os.getenv("EVAL_MODEL", "gpt-4.1")


class SimpleDOMExtractor(HTMLParser):
    """Extracts interactive elements, forms, and inline scripts from HTML."""

    def __init__(self):
        super().__init__()
        self.interactive_elements: List[Dict[str, Any]] = []
        self.headings: List[str] = []
        self.scripts: List[str] = []
        self.forms: List[Dict[str, Any]] = []
        self._current_tag: Optional[str] = None
        self._current_script: List[str] = []
        self._in_script: bool = False

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]):
        attr_dict = {k: (v or "") for k, v in attrs}
        self._current_tag = tag

        if tag == "script":
            self._in_script = True
            self._current_script = []

        if tag in ("button", "input", "select", "textarea", "a", "form"):
            element_info = {
                "tag": tag,
                "id": attr_dict.get("id", ""),
                "name": attr_dict.get("name", ""),
                "type": attr_dict.get("type", ""),
                "role": attr_dict.get("role", ""),
                "aria_label": attr_dict.get("aria-label", "") or attr_dict.get("aria-labelledby", ""),
                "classes": attr_dict.get("class", ""),
                "onclick": attr_dict.get("onclick", ""),
                "onsubmit": attr_dict.get("onsubmit", ""),
                "href": attr_dict.get("href", ""),
            }
            if tag == "form":
                self.forms.append(element_info)
            else:
                self.interactive_elements.append(element_info)

    def handle_endtag(self, tag: str):
        if tag == "script":
            self._in_script = False
            script_text = "".join(self._current_script).strip()
            if script_text:
                self.scripts.append(script_text)
            self._current_script = []
        self._current_tag = None

    def handle_data(self, data: str):
        if self._in_script:
            self._current_script.append(data)
        elif self._current_tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            text = data.strip()
            if text:
                self.headings.append(text)


def parse_dom_and_code_from_html(html_content: str, filename: str = "mockup.html") -> Dict[str, Any]:
    """Parses an HTML file and extracts DOM structure, interactive controls, and code/scripts."""
    parser = SimpleDOMExtractor()
    try:
        parser.feed(html_content)
    except Exception:
        pass

    # Extract inline event handlers and scripts
    inline_handlers = []
    all_elements = parser.interactive_elements + parser.forms
    for el in all_elements:
        if el.get("onclick"):
            inline_handlers.append(f"<{el['tag']} id='{el['id']}'> onclick: {el['onclick']}")
        if el.get("onsubmit"):
            inline_handlers.append(f"<{el['tag']} id='{el['id']}'> onsubmit: {el['onsubmit']}")

    return {
        "filename": filename,
        "raw_html": html_content,
        "headings": parser.headings,
        "forms": parser.forms,
        "interactive_elements": parser.interactive_elements,
        "scripts": parser.scripts,
        "inline_handlers": inline_handlers,
    }


def parse_user_stories_markdown(markdown_content: str) -> List[UserStoryDecomposition]:
    """Deterministically extracts user stories and acceptance criteria from markdown (05_user_stories.md)."""
    stories: List[UserStoryDecomposition] = []

    # Pattern to match user story sections
    # Matches: ### US-001 (or ### US-01, etc.) followed by **User Story:** ... and **Acceptance Criteria:**
    story_blocks = re.split(r"(?=###\s+US-\d+)", markdown_content)

    for block in story_blocks:
        block = block.strip()
        if not block.startswith("### US-"):
            continue

        us_id_match = re.search(r"###\s+(US-\d+)", block)
        us_id = us_id_match.group(1) if us_id_match else "US-UNKNOWN"

        story_text_match = re.search(r"\*\*User Story:\*\*\s*(.+?)(?=\r?\n-|\r?\n\*\*|\r?\n###|\Z)", block, re.DOTALL)
        user_story_text = story_text_match.group(1).strip() if story_text_match else ""

        # Extract Acceptance Criteria scenarios
        # Formats:
        # - **Scenario: <name>**
        #   - **Given:** ...
        #   - **When:** ...
        #   - **Then:** ...
        criteria: List[AcceptanceCriterion] = []
        scenario_pattern = re.compile(
            r"-\s*\*\*Scenario:\s*(.*?)\*\*\s*"
            r"(?:-\s*\*\*Given:\*\*\s*(.*?)\s*)?"
            r"(?:-\s*\*\*When:\*\*\s*(.*?)\s*)?"
            r"(?:-\s*\*\*Then:\*\*\s*(.*?)(?=\r?\n-\s*\*\*Scenario:|\r?\n###|\Z))",
            re.DOTALL | re.IGNORECASE,
        )

        matches = scenario_pattern.findall(block)
        for idx, match in enumerate(matches, 1):
            scenario_title = match[0].strip()
            given_clause = match[1].strip() if len(match) > 1 and match[1] else ""
            when_clause = match[2].strip() if len(match) > 2 and match[2] else ""
            then_clause = match[3].strip() if len(match) > 3 and match[3] else ""

            # Build full statement
            statement_parts = []
            if scenario_title:
                statement_parts.append(f"Scenario: {scenario_title}.")
            if given_clause:
                statement_parts.append(f"Given {given_clause},")
            if when_clause:
                statement_parts.append(f"when {when_clause},")
            if then_clause:
                statement_parts.append(f"then {then_clause}.")

            full_statement = " ".join(statement_parts).strip()
            if not full_statement:
                full_statement = f"Criterion for {scenario_title}"

            criteria.append(
                AcceptanceCriterion(
                    criterion_id=f"AC-{us_id.replace('US-', '')}-{idx}",
                    scenario=scenario_title,
                    given=given_clause,
                    when=when_clause,
                    then=then_clause,
                    statement=full_statement,
                )
            )

        # Fallback: if no Given-When-Then scenarios, look for bullet points under Acceptance Criteria:
        if not criteria and "**Acceptance Criteria:**" in block:
            ac_section = block.split("**Acceptance Criteria:**")[-1]
            bullet_items = re.findall(r"^-\s+(.+)$", ac_section, re.MULTILINE)
            for idx, item in enumerate(bullet_items, 1):
                clean_item = item.strip()
                if clean_item and not clean_item.startswith("**Source:"):
                    criteria.append(
                        AcceptanceCriterion(
                            criterion_id=f"AC-{us_id.replace('US-', '')}-{idx}",
                            scenario=f"Criterion {idx}",
                            statement=clean_item,
                        )
                    )

        if user_story_text:
            stories.append(
                UserStoryDecomposition(
                    us_id=us_id,
                    user_story=user_story_text,
                    acceptance_criteria=criteria,
                )
            )

    return stories


def decompose_user_story_llm(
    user_story_text: str,
    us_id: str = "US-001",
    model: Optional[str] = None,
    client: Optional[Any] = None,
) -> UserStoryDecomposition:
    """Decomposes an input user story U into a set of discrete, testable Acceptance Criteria A = {a_1, ..., a_n} via LLM."""
    model = model or DEFAULT_MODEL
    chat_client = client or ChatClient().client

    with open(DECOMPOSER_PROMPT_PATH, "r", encoding="utf-8") as pf:
        sys_prompt = pf.read()

    user_message = f"""
Please decompose the following User Story into a discrete, atomic, and testable set of Acceptance Criteria:

User Story ID: {us_id}
User Story: {user_story_text}
"""

    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_message},
    ]

    try:
        response = chat_client.responses.parse(
            model=model,
            input=cast(Any, messages),
            text_format=UserStoryDecomposition,
        )
        return response.output_parsed
    except Exception:
        # Fallback to standard chat completions
        raw_res = chat_client.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": "json_object"},
        )
        content_str = raw_res.choices[0].message.content or "{}"
        data = json.loads(content_str)
        return UserStoryDecomposition(**data)


def extract_acceptance_criteria(
    user_stories_source: Union[str, Path, List[Dict[str, Any]]],
    model: Optional[str] = None,
) -> List[UserStoryDecomposition]:
    """Extracts and decomposes user stories into discrete acceptance criteria A = {a_1, ..., a_n}."""
    # If source is a file path
    if isinstance(user_stories_source, (str, Path)) and os.path.isfile(str(user_stories_source)):
        with open(str(user_stories_source), "r", encoding="utf-8") as f:
            content = f.read()
        # First attempt deterministic markdown parsing
        stories = parse_user_stories_markdown(content)
        if stories:
            return stories
        # Fallback if raw text
        return [decompose_user_story_llm(content, us_id="US-001", model=model)]

    # If source is a raw markdown or plain text string
    if isinstance(user_stories_source, str):
        stories = parse_user_stories_markdown(user_stories_source)
        if stories:
            return stories
        return [decompose_user_story_llm(user_stories_source, us_id="US-001", model=model)]

    # If source is a list of dicts
    if isinstance(user_stories_source, list):
        parsed_list: List[UserStoryDecomposition] = []
        for idx, item in enumerate(user_stories_source, 1):
            if isinstance(item, dict):
                us_id = item.get("us_id") or item.get("id") or f"US-{idx:03d}"
                us_text = item.get("user_story") or item.get("text") or ""
                criteria_raw = item.get("acceptance_criteria") or []
                if isinstance(criteria_raw, list) and criteria_raw and isinstance(criteria_raw[0], dict):
                    criteria = [AcceptanceCriterion(**c) for c in criteria_raw]
                    parsed_list.append(UserStoryDecomposition(us_id=us_id, user_story=us_text, acceptance_criteria=criteria))
                elif isinstance(criteria_raw, list) and criteria_raw and isinstance(criteria_raw[0], str):
                    criteria = [
                        AcceptanceCriterion(
                            criterion_id=f"AC-{idx}-{c_idx}",
                            scenario=f"Scenario {c_idx}",
                            statement=c_str,
                        )
                        for c_idx, c_str in enumerate(criteria_raw, 1)
                    ]
                    parsed_list.append(UserStoryDecomposition(us_id=us_id, user_story=us_text, acceptance_criteria=criteria))
                else:
                    decomp = decompose_user_story_llm(us_text, us_id=us_id, model=model)
                    parsed_list.append(decomp)
        return parsed_list

    return []


def collect_code_and_dom_artifacts(
    html_target: Optional[Union[str, Path]] = None,
    code_target: Optional[Union[str, Path]] = None,
) -> Tuple[str, str]:
    """Collects and summarizes Rendered DOM (D) and Generated Code (C) from target paths."""
    dom_summary_parts: List[str] = []
    code_summary_parts: List[str] = []

    # 1. Collect HTML / DOM files
    if html_target:
        h_path = Path(html_target).resolve()
        html_files = []
        if h_path.is_file():
            html_files = [h_path]
        elif h_path.is_dir():
            html_files = sorted(list(set(h_path.rglob("*.html"))))

        for hf in html_files:
            try:
                content = hf.read_text(encoding="utf-8")
                parsed = parse_dom_and_code_from_html(content, filename=hf.name)

                # Format DOM summary
                dom_summary_parts.append(f"### HTML Mockup: `{hf.name}`")
                if parsed["headings"]:
                    dom_summary_parts.append(f"- **Headings:** {', '.join(parsed['headings'])}")
                if parsed["forms"]:
                    dom_summary_parts.append(f"- **Forms:** {json.dumps(parsed['forms'], ensure_ascii=False)}")
                if parsed["interactive_elements"]:
                    dom_summary_parts.append(
                        f"- **Interactive Elements ({len(parsed['interactive_elements'])}):**\n"
                        f"```json\n{json.dumps(parsed['interactive_elements'][:25], indent=2, ensure_ascii=False)}\n```"
                    )
                dom_summary_parts.append(f"- **Full HTML Source:**\n```html\n{content}\n```\n")

                # Extract embedded scripts into code summary
                if parsed["scripts"] or parsed["inline_handlers"]:
                    code_summary_parts.append(f"### Scripts in `{hf.name}`:")
                    for h in parsed["inline_handlers"]:
                        code_summary_parts.append(f"- Inline Event: {h}")
                    for s in parsed["scripts"]:
                        code_summary_parts.append(f"```javascript\n{s}\n```")

            except Exception as e:
                dom_summary_parts.append(f"### Error reading `{hf.name}`: {e}")

    # 2. Collect separate code files (.js, .ts, .py, .css)
    if code_target:
        c_path = Path(code_target).resolve()
        code_files = []
        if c_path.is_file():
            code_files = [c_path]
        elif c_path.is_dir():
            for ext in ("*.js", "*.ts", "*.py", "*.css", "*.jsx", "*.tsx"):
                code_files.extend(c_path.rglob(ext))
            code_files = sorted(list(set(code_files)))

        for cf in code_files:
            try:
                code_content = cf.read_text(encoding="utf-8")
                code_summary_parts.append(f"### Code File: `{cf.name}`\n```{cf.suffix.replace('.', '')}\n{code_content}\n```\n")
            except Exception as e:
                code_summary_parts.append(f"### Error reading code `{cf.name}`: {e}")

    rendered_dom_text = "\n".join(dom_summary_parts) if dom_summary_parts else "No rendered DOM files provided."
    generated_code_text = "\n".join(code_summary_parts) if code_summary_parts else "No standalone code scripts provided (only static markup)."

    return rendered_dom_text, generated_code_text


def verify_user_story_accs(
    story: UserStoryDecomposition,
    rendered_dom_d: str,
    generated_code_c: str,
    model: Optional[str] = None,
    client: Optional[Any] = None,
) -> UserStoryACCS:
    """Evaluates a single User Story's Acceptance Criteria A against Code C and DOM D,

    computing v(a_i, C, D) in {0.0, 0.5, 1.0} and ACCS = sum(v(a_i, C, D)) / |A|.
    """
    model = model or DEFAULT_MODEL
    chat_client = client or ChatClient().client

    # Edge case: If user story has 0 acceptance criteria, return 0.0 ACCS
    if not story.acceptance_criteria:
        return UserStoryACCS(
            us_id=story.us_id,
            user_story=story.user_story,
            criteria_count=0,
            sum_verification_score=0.0,
            accs_score=0.0,
            verifications=[],
        )

    with open(VERIFICATION_PROMPT_PATH, "r", encoding="utf-8") as pf:
        sys_prompt = pf.read()

    criteria_formatted = []
    for c in story.acceptance_criteria:
        criteria_formatted.append(
            f"- **[{c.criterion_id}]**: {c.statement} "
            f"(Given: '{c.given}', When: '{c.when}', Then: '{c.then}')"
        )
    criteria_text = "\n".join(criteria_formatted)

    user_message = f"""
Please evaluate the following User Story and its Acceptance Criteria against the Rendered DOM and Generated Code:

### USER STORY [{story.us_id}]
{story.user_story}

### ACCEPTANCE CRITERIA A = {{a_1, ..., a_n}} (|A| = {len(story.acceptance_criteria)}):
{criteria_text}

---

### RENDERED DOM (D):
{rendered_dom_d}

---

### GENERATED CODE & EVENT HANDLERS (C):
{generated_code_c}
"""

    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_message},
    ]

    verifications: List[CriterionVerification] = []

    try:
        # Schema for single user story response from LLM judge
        class StoryVerificationResponse(UserStoryACCS):
            pass

        response = chat_client.responses.parse(
            model=model,
            input=cast(Any, messages),
            text_format=StoryVerificationResponse,
        )
        parsed = response.output_parsed
        verifications = parsed.verifications
    except Exception:
        # Fallback to chat completions json_object
        raw_res = chat_client.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": "json_object"},
        )
        content_str = raw_res.choices[0].message.content or "{}"
        data = json.loads(content_str)
        verif_raw = data.get("verifications", [])
        for v in verif_raw:
            verifications.append(
                CriterionVerification(
                    criterion_id=v.get("criterion_id", "AC-UNKNOWN"),
                    criterion_statement=v.get("criterion_statement", ""),
                    verification_score=float(v.get("verification_score", 0.0)),
                    verdict=v.get("verdict", "NONE"),
                    dom_evidence=v.get("dom_evidence", ""),
                    code_evidence=v.get("code_evidence", ""),
                    reasoning=v.get("reasoning", ""),
                )
            )

    # Sanitize and strictly enforce v(a_i, C, D) in {0.0, 0.5, 1.0}
    sanitized_verifications: List[CriterionVerification] = []
    total_score = 0.0

    for v in verifications:
        # Clamp score to exact allowed values {0.0, 0.5, 1.0}
        raw_score = float(v.verification_score)
        if raw_score >= 0.75:
            score = 1.0
            verdict = "FULL"
        elif raw_score >= 0.25:
            score = 0.5
            verdict = "PARTIAL"
        else:
            score = 0.0
            verdict = "NONE"

        total_score += score
        sanitized_verifications.append(
            CriterionVerification(
                criterion_id=v.criterion_id,
                criterion_statement=v.criterion_statement,
                verification_score=score,
                verdict=verdict,
                dom_evidence=v.dom_evidence,
                code_evidence=v.code_evidence,
                reasoning=v.reasoning,
            )
        )

    # Compute mathematical ACCS: ACCS = (sum_{i=1}^n v(a_i, C, D)) / |A|
    n = len(sanitized_verifications) if sanitized_verifications else len(story.acceptance_criteria)
    accs_score = round(total_score / n, 4) if n > 0 else 0.0

    return UserStoryACCS(
        us_id=story.us_id,
        user_story=story.user_story,
        criteria_count=n,
        sum_verification_score=round(total_score, 4),
        accs_score=accs_score,
        verifications=sanitized_verifications,
    )


def evaluate_accs(
    user_stories_source: Union[str, Path, List[Dict[str, Any]]],
    html_target: Optional[Union[str, Path]] = None,
    code_target: Optional[Union[str, Path]] = None,
    output_json_path: Optional[str] = None,
    output_csv_path: Optional[str] = None,
    model: Optional[str] = None,
) -> ACCSEvaluationReport:
    """End-to-end Acceptance Criteria Extraction & Coverage Score (ACCS) evaluator.

    Formulation:
        ACCS = (sum_{i=1}^n v(a_i, C, D)) / |A|
        where v(a_i, C, D) in {0.0, 0.5, 1.0}
    """
    model = model or DEFAULT_MODEL
    print(f"\n[ACCS Evaluator] Decomposing User Stories and Extracting Acceptance Criteria...")
    stories = extract_acceptance_criteria(user_stories_source, model=model)
    print(f"  Extracted {len(stories)} User Stories with total discrete criteria.")

    print(f"[ACCS Evaluator] Ingesting Rendered DOM (D) and Generated Code (C)...")
    dom_text, code_text = collect_code_and_dom_artifacts(html_target=html_target, code_target=code_target)

    story_evaluations: List[UserStoryACCS] = []
    total_criteria = 0
    total_score_sum = 0.0
    full_count = 0
    partial_count = 0
    none_count = 0

    print(f"[ACCS Evaluator] Evaluating {len(stories)} User Stories with LLM-as-a-Judge (model: {model})...")

    for story in stories:
        print(f"  Verifying {story.us_id} ({len(story.acceptance_criteria)} criteria)...")
        eval_result = verify_user_story_accs(
            story=story,
            rendered_dom_d=dom_text,
            generated_code_c=code_text,
            model=model,
        )
        story_evaluations.append(eval_result)

        total_criteria += eval_result.criteria_count
        total_score_sum += eval_result.sum_verification_score

        for v in eval_result.verifications:
            if v.verification_score == 1.0:
                full_count += 1
            elif v.verification_score == 0.5:
                partial_count += 1
            else:
                none_count += 1

        print(f"    -> ACCS({story.us_id}) = {eval_result.accs_score:.4f} (Score: {eval_result.sum_verification_score}/{eval_result.criteria_count})")

    # Calculate overall suite ACCS
    overall_accs = round(total_score_sum / total_criteria, 4) if total_criteria > 0 else 0.0
    full_ratio = round(full_count / total_criteria, 4) if total_criteria > 0 else 0.0
    partial_ratio = round(partial_count / total_criteria, 4) if total_criteria > 0 else 0.0
    none_ratio = round(none_count / total_criteria, 4) if total_criteria > 0 else 0.0

    report = ACCSEvaluationReport(
        total_user_stories=len(stories),
        total_criteria_count=total_criteria,
        total_score_sum=round(total_score_sum, 4),
        overall_accs=overall_accs,
        full_count=full_count,
        partial_count=partial_count,
        none_count=none_count,
        full_ratio=full_ratio,
        partial_ratio=partial_ratio,
        none_ratio=none_ratio,
        evaluations=story_evaluations,
    )

    if output_json_path:
        _write_json_file(output_json_path, report)
        print(f"[ACCS Evaluator] Saved detailed JSON report to: {output_json_path}")

    if output_csv_path:
        build_accs_table(report, output_csv_path)

    return report


def build_accs_table(
    report_or_filepath: Union[ACCSEvaluationReport, Dict[str, Any], str],
    output_table_path: Optional[str] = None,
) -> pd.DataFrame:
    """Builds a pandas DataFrame summary table for ACCS evaluations."""
    if isinstance(report_or_filepath, str):
        with open(report_or_filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    elif isinstance(report_or_filepath, ACCSEvaluationReport):
        data = report_or_filepath.model_dump()
    else:
        data = report_or_filepath

    evaluations = data.get("evaluations", [])
    rows = []

    for item in evaluations:
        verifs = item.get("verifications", [])
        f_cnt = sum(1 for v in verifs if float(v.get("verification_score", 0.0)) == 1.0)
        p_cnt = sum(1 for v in verifs if float(v.get("verification_score", 0.0)) == 0.5)
        n_cnt = sum(1 for v in verifs if float(v.get("verification_score", 0.0)) == 0.0)

        rows.append({
            "us_id": item.get("us_id"),
            "criteria_count (|A|)": item.get("criteria_count", len(verifs)),
            "full_impl (1.0)": f_cnt,
            "partial_impl (0.5)": p_cnt,
            "no_impl (0.0)": n_cnt,
            "sum_score": item.get("sum_verification_score", 0.0),
            "accs_score": item.get("accs_score", 0.0),
        })

    # Add summary mean row
    if rows:
        total_a = data.get("total_criteria_count", sum(r["criteria_count (|A|)"] for r in rows))
        total_sum = data.get("total_score_sum", sum(r["sum_score"] for r in rows))
        overall = data.get("overall_accs", round(total_sum / total_a, 4) if total_a else 0.0)

        rows.append({
            "us_id": "OVERALL ACCS MEAN",
            "criteria_count (|A|)": total_a,
            "full_impl (1.0)": data.get("full_count", sum(r["full_impl (1.0)"] for r in rows)),
            "partial_impl (0.5)": data.get("partial_count", sum(r["partial_impl (0.5)"] for r in rows)),
            "no_impl (0.0)": data.get("none_count", sum(r["no_impl (0.0)"] for r in rows)),
            "sum_score": round(total_sum, 4),
            "accs_score": overall,
        })

    table = pd.DataFrame(rows)

    if output_table_path:
        output_dir = os.path.dirname(output_table_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        table.to_csv(output_table_path, index=False)
        print(f"Saved ACCS summary table to: {output_table_path}")

    return table


def build_accs_criteria_detail_table(
    report_or_filepath: Union[ACCSEvaluationReport, Dict[str, Any], str],
    output_table_path: Optional[str] = None,
) -> pd.DataFrame:
    """Builds a detailed criterion-level DataFrame for granular inspection."""
    if isinstance(report_or_filepath, str):
        with open(report_or_filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    elif isinstance(report_or_filepath, ACCSEvaluationReport):
        data = report_or_filepath.model_dump()
    else:
        data = report_or_filepath

    evaluations = data.get("evaluations", [])
    rows = []

    for item in evaluations:
        us_id = item.get("us_id")
        for v in item.get("verifications", []):
            rows.append({
                "us_id": us_id,
                "criterion_id": v.get("criterion_id"),
                "criterion_statement": v.get("criterion_statement"),
                "verification_score v(a_i, C, D)": v.get("verification_score"),
                "verdict": v.get("verdict"),
                "dom_evidence": v.get("dom_evidence"),
                "code_evidence": v.get("code_evidence"),
                "reasoning": v.get("reasoning"),
            })

    table = pd.DataFrame(rows)

    if output_table_path:
        output_dir = os.path.dirname(output_table_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        table.to_csv(output_table_path, index=False)
        print(f"Saved ACCS criteria detail table to: {output_table_path}")

    return table


def main():
    parser = argparse.ArgumentParser(
        description="Acceptance Criteria Extraction & Coverage Score (ACCS) Evaluator.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--user-stories", "-u",
        required=True,
        help="Path to user stories file (e.g. 05_user_stories.md) or text.",
    )
    parser.add_argument(
        "--html-dir", "-hd",
        default=None,
        help="Path to rendered HTML mockups directory or file.",
    )
    parser.add_argument(
        "--code-dir", "-cd",
        default=None,
        help="Path to generated code directory (.js, .ts, .py, etc.).",
    )
    parser.add_argument(
        "--agent", "-a",
        default="eval_run",
        help="Agent name for namespacing outputs.",
    )
    parser.add_argument(
        "--output-json", "-oj",
        default=None,
        help="Path to save detailed JSON report.",
    )
    parser.add_argument(
        "--output-csv", "-oc",
        default=None,
        help="Path to save summary CSV table.",
    )
    parser.add_argument(
        "--model", "-m",
        default=None,
        help="LLM model deployment name for evaluation.",
    )

    args = parser.parse_args()

    # Default output filenames if not provided
    out_json = args.output_json or f"scratch/{args.agent}_accs_eval.json"
    out_csv = args.output_csv or f"scratch/{args.agent}_accs_table.csv"

    report = evaluate_accs(
        user_stories_source=args.user_stories,
        html_target=args.html_dir,
        code_target=args.code_dir,
        output_json_path=out_json,
        output_csv_path=out_csv,
        model=args.model,
    )

    summary_table = build_accs_table(report)
    print("\n" + "=" * 60)
    print("ACCS EVALUATION SUMMARY TABLE:")
    print("=" * 60)
    print(summary_table.to_string(index=False))
    print(f"\nOverall ACCS Score: {report.overall_accs:.4f}")
    print(f"Full: {report.full_count} ({report.full_ratio * 100:.1f}%), "
          f"Partial: {report.partial_count} ({report.partial_ratio * 100:.1f}%), "
          f"None: {report.none_count} ({report.none_ratio * 100:.1f}%)")


if __name__ == "__main__":
    main()
