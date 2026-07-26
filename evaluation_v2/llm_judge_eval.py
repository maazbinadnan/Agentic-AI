import os
import json
from typing import List, Dict, Any, Tuple, cast
from global_layer.AzureClient import ChatClient
from global_layer.functions import _read_file
from evaluation_v2.states.state import (
    SingleRequirementAlignment,
    AlignmentReport,
    GEvalRequirementEvaluation,
    GEvalReport,
)

# Relative file pathing based on script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")
ALIGNMENT_PROMPT_PATH = os.path.join(PROMPTS_DIR, "metrics_alignment_prompt.md")
G_EVAL_PROMPT_PATH = os.path.join(PROMPTS_DIR, "eval_g_eval_prompt.md")

client = ChatClient().client


def _load_prompt_template(prompt_path: str) -> str:
    """Safely reads prompt file content."""
    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Prompt file not found at: {prompt_path}")
    return _read_file(prompt_path)


def evaluate_semantic_alignment(
    ground_truth_file: str,
    generated_file: str,
    model: str = "gpt-4o"
) -> AlignmentReport:
    """
    Evaluates semantic coverage, precision, recall, and F1 by checking each
    ground truth requirement individually against the list of generated requirements.
    """
    gt_raw = _read_file(ground_truth_file)
    gen_raw = _read_file(generated_file)

    try:
        gt_items = json.loads(gt_raw) if isinstance(gt_raw, str) else gt_raw
    except Exception:
        gt_items = [{"No.": 1, "Requirement": gt_raw}]

    if not isinstance(gt_items, list):
        gt_items = [gt_items]

    prompt_template = _load_prompt_template(ALIGNMENT_PROMPT_PATH)
    alignments: List[SingleRequirementAlignment] = []
    matched_generated_indices = set()

    for idx, item in enumerate(gt_items):
        gt_id = str(item.get("No.", idx + 1))
        gt_text = item.get("Requirement", str(item))

        # Fill template variables
        filled_prompt = prompt_template.replace("{{GROUND_TRUTH_ID}}", gt_id)
        filled_prompt = filled_prompt.replace("{{GROUND_TRUTH_TEXT}}", gt_text)
        filled_prompt = filled_prompt.replace("{{GENERATED_LIST}}", str(gen_raw))

        messages = [
            {"role": "system", "content": "You are a precise software requirements semantic matching auditor."},
            {"role": "user", "content": filled_prompt}
        ]

        try:
            response = client.responses.parse(
                model=model,
                input=cast(str, messages),
                text_format=SingleRequirementAlignment
            )
            parsed: SingleRequirementAlignment = json.loads(response.output_text)
            alignments.append(parsed)

            if parsed.matched and parsed.matched_generated_requirement:
                matched_generated_indices.add(parsed.matched_generated_requirement.strip())

        except Exception as e:
            # Fallback error handling
            alignments.append(
                SingleRequirementAlignment(
                    ground_truth_id=gt_id,
                    ground_truth_text=gt_text,
                    matched=False,
                    match_score=0.0,
                    matched_generated_requirement=None,
                    explanation=f"LLM Parsing error during evaluation: {str(e)}"
                )
            )

    # Compute Recall, Precision, Macro F1
    total_gt = len(gt_items)
    successful_matches = sum(1 for a in alignments if a.matched)
    recall = round(successful_matches / total_gt, 4) if total_gt > 0 else 0.0

    # Parse total generated items count
    try:
        gen_parsed = json.loads(gen_raw) if isinstance(gen_raw, str) else gen_raw
        if isinstance(gen_parsed, list):
            total_gen = len(gen_parsed)
        elif isinstance(gen_parsed, dict) and "user_stories" in gen_parsed:
            total_gen = len(gen_parsed["user_stories"])
        else:
            total_gen = len(alignments)
    except Exception:
        total_gen = len(alignments)

    precision = round(len(matched_generated_indices) / total_gen, 4) if total_gen > 0 else recall
    if precision > 1.0:
        precision = 1.0  # cap boundary

    macro_f1 = round(2 * (precision * recall) / (precision + recall), 4) if (precision + recall) > 0 else 0.0

    return AlignmentReport(
        alignments=alignments,
        recall=recall,
        precision=precision,
        macro_f1=macro_f1
    )


def evaluate_g_eval_rubric(
    original_source_file: str,
    generated_file: str,
    model: str = "gpt-4o"
) -> GEvalReport:
    """
    Runs multi-criterion G-Eval rubric evaluation (INVEST, BDD, Completeness, Feasibility)
    on the generated requirements.
    """
    source_doc = _read_file(original_source_file)
    gen_doc = _read_file(generated_file)
    system_prompt = _load_prompt_template(G_EVAL_PROMPT_PATH)

    user_content = f"""
    ### ORIGINAL SOURCE DOCUMENT:
    {source_doc}

    ### GENERATED REQUIREMENTS TO EVALUATE:
    {gen_doc}

    Conduct a critical G-Eval assessment of every single generated requirement.
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_content}
    ]

    try:
        response = client.responses.parse(
            model=model,
            input=cast(str, messages),
            text_format=GEvalReport
        )
        report: GEvalReport = json.loads(response.output_text)
        return report

    except Exception as e:
        print(f"Warning: GEval structured parse encountered an exception: {e}")
        # Return fallback empty report
        return GEvalReport(
            evaluations=[],
            mean_invest_score=0.0,
            mean_bdd_score=0.0,
            mean_completeness_score=0.0,
            mean_feasibility_score=0.0,
            mean_overall_score=0.0
        )
