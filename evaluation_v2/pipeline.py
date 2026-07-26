import os
import json
from pathlib import Path
from typing import Any, Optional
from global_layer.functions import _read_file, _write_json_file
from evaluation_v2.states.state import EvaluationV2Summary
from evaluation_v2.deterministic_eval import (
    evaluate_deterministic_metrics,
    evaluate_ixd_mockups,
    evaluate_traceability,
    evaluate_system_efficiency,
)
from evaluation_v2.llm_judge_eval import (
    evaluate_semantic_alignment,
    evaluate_g_eval_rubric,
)


def _load_json_or_raw(filepath: str) -> Any:
    """Helper to safely read file and parse JSON if applicable."""
    if not os.path.exists(filepath):
        return None
    raw = _read_file(filepath)
    try:
        return json.loads(raw)
    except Exception:
        return raw


def run_evaluation_pipeline(
    architecture_name: str,
    target_type: str,
    source_doc_file: str,
    ground_truth_file: str,
    run_output_dir: str,
    output_summary_file: str,
    model: str = "gpt-4o"
) -> EvaluationV2Summary:
    """
    Executes full evaluation pipeline (Phase 1 BA Requirements + Phase 2 IxD Mockups + Traceability + System Metrics)
    for a specified architecture's output directory.
    """
    print(f"\n=========================================================================")
    print(f"Running Evaluation V2 Pipeline: [{architecture_name}] ({target_type})")
    print(f"Source Folder: {run_output_dir}")
    print(f"=========================================================================\n")

    run_path = Path(run_output_dir)

    # 1. Load state.json
    state_json_path = run_path / "state.json"
    state_data = _load_json_or_raw(str(state_json_path)) or {}

    # 2. Extract BA and IxD output objects from state or subfolders
    ba_output = state_data.get("ba_output") or {}
    ixd_output = state_data.get("ixd_output") or {}

    # Fallback to searching subfolders if state.json does not contain full dumps
    ba_folder = run_path / "01_business_analysis"
    if not ba_output and ba_folder.exists():
        # Read user_stories.md or functional_requirements.md
        us_file = ba_folder / "04_user_stories.md"
        if us_file.exists():
            ba_output = {"user_stories": _read_file(str(us_file))}

    # Determine generated requirements target file for semantic evaluation
    gen_req_file = str(run_path / "01_business_analysis" / "04_user_stories.md")
    if not os.path.exists(gen_req_file):
        gen_req_file = str(run_path / "01_business_analysis" / "iter_0" / "04_user_stories.md")
    if not os.path.exists(gen_req_file):
        # Create a temporary file from ba_output
        gen_req_file = str(run_path / "generated_requirements_eval_tmp.json")
        _write_json_file(gen_req_file, ba_output)

    # 3. Step 1: Deterministic Requirements Metrics
    print("Step 1/5: Computing Deterministic Metrics (BDD Syntax, Ambiguity, Redundancy)...")
    deterministic_res = evaluate_deterministic_metrics(ba_output if ba_output else _read_file(gen_req_file))

    # 4. Step 2: Semantic Alignment (Precision, Recall, Macro F1)
    print("Step 2/5: Computing Semantic Alignment (Precision, Recall, F1 against Ground Truth)...")
    alignment_res = evaluate_semantic_alignment(
        ground_truth_file=ground_truth_file,
        generated_file=gen_req_file,
        model=model
    )

    # 5. Step 3: G-Eval Rubric Assessment
    print("Step 3/5: Running G-Eval Rubric Evaluation...")
    g_eval_res = evaluate_g_eval_rubric(
        original_source_file=source_doc_file,
        generated_file=gen_req_file,
        model=model
    )

    # 6. Step 4: Phase 2 IxD Mockup & Story Traceability Evaluation
    print("Step 4/5: Evaluating IxD HTML Mockups & Story Coverage...")
    total_us_count = deterministic_res.total_requirements
    ixd_res = evaluate_ixd_mockups(ixd_output, total_user_stories_count=total_us_count)
    traceability_res = evaluate_traceability(ba_output)

    # 7. Step 5: Multi-Agent System & Iteration Efficiency
    print("Step 5/5: Extracting System Iteration & Efficiency Metrics...")
    system_res = evaluate_system_efficiency(state_data)

    # Build Master Summary
    summary = EvaluationV2Summary(
        architecture_name=architecture_name,
        target_type=target_type,
        deterministic_metrics=deterministic_res,
        alignment_metrics=alignment_res,
        g_eval_metrics=g_eval_res,
        ixd_metrics=ixd_res,
        traceability_metrics=traceability_res,
        system_metrics=system_res
    )

    # Save JSON Report
    os.makedirs(os.path.dirname(os.path.abspath(output_summary_file)), exist_ok=True)
    _write_json_file(output_summary_file, summary.model_dump())
    print(f"\nSuccessfully generated evaluation summary at: {output_summary_file}\n")

    return summary
