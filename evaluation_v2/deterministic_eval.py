import re
import os
import json
from pathlib import Path
from typing import List, Dict, Tuple, Any, Union, Optional
from html.parser import HTMLParser

from evaluation_v2.states.state import (
    DeterministicMetrics,
    IxDMetrics,
    TraceabilityMetrics,
    SystemEfficiencyMetrics
)

# Standard Requirements Engineering ambiguous/vague words dictionary (IEEE 830 / ISO 29148 standards)
AMBIGUOUS_WORDS = {
    "fast", "quick", "quickly", "easy", "easily", "user-friendly", "user friendly",
    "seamless", "seamlessly", "efficient", "efficiently", "flexible", "robust",
    "scalable", "reliable", "intuitive", "appropriate", "adequate", "sufficient",
    "state-of-the-art", "etc", "and so on", "as far as possible", "well", "good",
    "optimal", "maximum", "minimum", "high-performance", "high quality"
}

BDD_GIVEN_PATTERN = re.compile(r'\b(given|given that)\b', re.IGNORECASE)
BDD_WHEN_PATTERN = re.compile(r'\b(when|whenever)\b', re.IGNORECASE)
BDD_THEN_PATTERN = re.compile(r'\b(then)\b', re.IGNORECASE)


class InteractiveComponentCounter(HTMLParser):
    """HTML Parser using standard library to count interactive DOM elements."""
    def __init__(self):
        super().__init__()
        self.buttons_count = 0
        self.inputs_count = 0
        self.containers_count = 0

    def handle_starttag(self, tag, attrs):
        tag_lower = tag.lower()
        if tag_lower in ['button', 'a']:
            self.buttons_count += 1
        elif tag_lower in ['input', 'select', 'textarea']:
            self.inputs_count += 1
        elif tag_lower in ['form', 'table', 'article', 'section', 'main']:
            self.containers_count += 1


def evaluate_bdd_syntax(text: str) -> bool:
    given_match = BDD_GIVEN_PATTERN.search(text)
    when_match = BDD_WHEN_PATTERN.search(text)
    then_match = BDD_THEN_PATTERN.search(text)

    if not (given_match and when_match and then_match):
        return False

    return given_match.start() < when_match.start() < then_match.start()


def scan_ambiguous_words(text: str) -> Tuple[int, Dict[str, int]]:
    text_lower = text.lower()
    frequency_map: Dict[str, int] = {}
    total_count = 0

    for word in AMBIGUOUS_WORDS:
        pattern = r'\b' + re.escape(word) + r'\b'
        matches = len(re.findall(pattern, text_lower))
        if matches > 0:
            frequency_map[word] = matches
            total_count += matches

    return total_count, frequency_map


def _tokenize(text: str) -> set:
    words = re.findall(r'\b\w+\b', text.lower())
    stop_words = {'the', 'a', 'an', 'and', 'or', 'to', 'in', 'of', 'for', 'with', 'on', 'at', 'by', 'from', 'is', 'are', 'be', 'must', 'shall', 'should', 'as', 'user', 'system', 'app'}
    return {w for w in words if w not in stop_words and len(w) > 2}


def compute_redundancy_score(texts: List[str]) -> float:
    if len(texts) <= 1:
        return 0.0

    token_sets = [_tokenize(t) for t in texts]
    pair_similarities: List[float] = []

    for i in range(len(token_sets)):
        for j in range(i + 1, len(token_sets)):
            s1 = token_sets[i]
            s2 = token_sets[j]
            if not s1 or not s2:
                continue
            intersection = len(s1.intersection(s2))
            union = len(s1.union(s2))
            jaccard = intersection / union if union > 0 else 0.0
            pair_similarities.append(jaccard)

    if not pair_similarities:
        return 0.0

    return round(sum(pair_similarities) / len(pair_similarities), 4)


def extract_requirement_texts(data: Any) -> List[str]:
    texts: List[str] = []
    if isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                texts.append(item)
            elif isinstance(item, dict):
                parts = []
                for k in ["user_story", "User_story", "Requirement", "requirement", "title", "description", "acceptance_criteria", "AcceptanceCriteria"]:
                    if k in item and item[k]:
                        val = item[k]
                        if isinstance(val, list):
                            parts.append(" ".join(str(x) for x in val))
                        else:
                            parts.append(str(val))
                if parts:
                    texts.append(" ".join(parts))
                else:
                    texts.append(str(item))
    elif isinstance(data, dict):
        for key in ["user_stories", "requirements", "functional_requirements", "non_functional_requirements"]:
            if key in data:
                return extract_requirement_texts(data[key])
        texts.append(str(data))
    elif isinstance(data, str):
        texts.append(data)

    return texts


def evaluate_deterministic_metrics(generated_data: Any) -> DeterministicMetrics:
    req_texts = extract_requirement_texts(generated_data)
    total_reqs = len(req_texts)

    if total_reqs == 0:
        return DeterministicMetrics(
            total_requirements=0,
            bdd_compliant_count=0,
            bdd_compliance_percentage=0.0,
            total_words=0,
            avg_word_count_per_requirement=0.0,
            ambiguous_words_found=0,
            ambiguity_density_per_100_words=0.0,
            redundancy_score=0.0,
            ambiguous_terms_breakdown={}
        )

    bdd_compliant_count = 0
    total_words = 0
    total_ambiguous_count = 0
    combined_freq_map: Dict[str, int] = {}

    for text in req_texts:
        if evaluate_bdd_syntax(text):
            bdd_compliant_count += 1

        words = len(re.findall(r'\b\w+\b', text))
        total_words += words

        amb_count, freq_map = scan_ambiguous_words(text)
        total_ambiguous_count += amb_count
        for k, v in freq_map.items():
            combined_freq_map[k] = combined_freq_map.get(k, 0) + v

    bdd_percentage = round((bdd_compliant_count / total_reqs) * 100.0, 2)
    avg_words = round(total_words / total_reqs, 2) if total_reqs > 0 else 0.0
    amb_density = round((total_ambiguous_count / total_words) * 100.0, 2) if total_words > 0 else 0.0
    redundancy = compute_redundancy_score(req_texts)

    return DeterministicMetrics(
        total_requirements=total_reqs,
        bdd_compliant_count=bdd_compliant_count,
        bdd_compliance_percentage=bdd_percentage,
        total_words=total_words,
        avg_word_count_per_requirement=avg_words,
        ambiguous_words_found=total_ambiguous_count,
        ambiguity_density_per_100_words=amb_density,
        redundancy_score=redundancy,
        ambiguous_terms_breakdown=combined_freq_map
    )


# =========================================================================
# Phase 2 IxD HTML Mockup & Story Traceability Evaluator
# =========================================================================

def evaluate_ixd_mockups(ixd_data: Any, total_user_stories_count: int = 0) -> IxDMetrics:
    """
    Parses Phase 2 Interaction Design outputs (HTML mockups, mapping table, tradeoffs).
    """
    mockup_files = []
    mapping_rows = []
    tradeoffs_rows = []

    if isinstance(ixd_data, dict):
        mockup_files = ixd_data.get("mockup_files", {}).get("files", []) or ixd_data.get("mockup_files", {}).get("table", [])
        mapping_rows = ixd_data.get("mapping_table", {}).get("mapping_table", [])
        tradeoffs_rows = ixd_data.get("tradeoffs", {}).get("table", [])

    buttons_count = 0
    inputs_count = 0
    containers_count = 0

    for file_obj in mockup_files:
        html_code = ""
        if isinstance(file_obj, dict):
            html_code = file_obj.get("html_content") or file_obj.get("html_code") or ""
        else:
            html_code = getattr(file_obj, "html_content", "")

        if html_code:
            parser = InteractiveComponentCounter()
            try:
                parser.feed(html_code)
                buttons_count += parser.buttons_count
                inputs_count += parser.inputs_count
                containers_count += parser.containers_count
            except Exception:
                pass

    total_interactive = buttons_count + inputs_count + containers_count

    # Check mapped user stories in mapping table
    mapped_stories_set = set()
    for row in mapping_rows:
        if isinstance(row, dict):
            stories = row.get("user_stories") or row.get("UserStory") or []
            if isinstance(stories, list):
                for s in stories:
                    mapped_stories_set.add(str(s).strip())
            elif isinstance(stories, str):
                mapped_stories_set.add(stories.strip())

    mapped_count = len(mapped_stories_set)
    target_stories_count = total_user_stories_count if total_user_stories_count > 0 else mapped_count
    unmapped_count = max(0, target_stories_count - mapped_count)
    coverage_pct = round((mapped_count / target_stories_count) * 100.0, 2) if target_stories_count > 0 else 100.0

    return IxDMetrics(
        total_mockup_files=len(mockup_files),
        total_interactive_components=total_interactive,
        buttons_count=buttons_count,
        inputs_count=inputs_count,
        containers_count=containers_count,
        story_mapping_coverage_percentage=coverage_pct,
        mapped_stories_count=mapped_count,
        unmapped_stories_count=unmapped_count,
        tradeoffs_count=len(tradeoffs_rows)
    )


def evaluate_traceability(ba_data: Any) -> TraceabilityMetrics:
    user_needs = []
    fr_list = []
    us_list = []
    matrix = []

    if isinstance(ba_data, dict):
        user_needs = ba_data.get("user_needs", [])
        fr_list = ba_data.get("functional_requirements", [])
        us_list = ba_data.get("user_stories", [])
        matrix = ba_data.get("traceability_matrix") or ba_data.get("TraceabilityMatrix") or []

    total_un = len(user_needs)

    mapped_un_set = set()
    if isinstance(matrix, list):
        for row in matrix:
            if isinstance(row, dict):
                un_id = row.get("user_need_id") or row.get("UserNeedID")
                if un_id:
                    mapped_un_set.add(str(un_id).strip())

    completeness_pct = round((len(mapped_un_set) / total_un) * 100.0, 2) if total_un > 0 else 100.0

    return TraceabilityMetrics(
        total_user_needs=total_un,
        total_functional_reqs=len(fr_list),
        total_user_stories=len(us_list),
        matrix_entries_count=len(matrix) if isinstance(matrix, list) else 0,
        matrix_completeness_percentage=completeness_pct
    )


def evaluate_system_efficiency(state_data: Any) -> SystemEfficiencyMetrics:
    iterations = {}
    feedback_history = []
    verdict = None

    if isinstance(state_data, dict):
        iterations = state_data.get("iterations", {})
        feedback_history = state_data.get("feedback_history", [])
        verdict = state_data.get("verdict")

    ba_iter = iterations.get("ba", 0) if isinstance(iterations, dict) else 0
    ixd_iter = iterations.get("ixd", 0) if isinstance(iterations, dict) else 0
    total_iter = ba_iter + ixd_iter if (ba_iter + ixd_iter) > 0 else 1

    return SystemEfficiencyMetrics(
        total_iterations=total_iter,
        ba_iterations=ba_iter,
        ixd_iterations=ixd_iter,
        feedback_rounds_count=len(feedback_history) if isinstance(feedback_history, list) else 0,
        verdict=verdict
    )
