"""Standalone runner script for GEval requirement evaluation.

Evaluates generated Functional and Non-Functional requirements against
ground truth requirements using DeepEval's G-Eval metric.

Usage:
    python -m evaluation.geval.run_geval \
        --func-reqs hitl_agent/outputs/final_run/03_functional_requirements.md \
        --nfunc-reqs hitl_agent/outputs/final_run/04_non_functional_requirements.md \
        --agent hitl_geval_demo
"""

import argparse
import json
import os
import sys
from typing import Dict, Any

# Ensure UTF-8 output encoding on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from deepeval.test_case import LLMTestCase
from deepeval.metrics import GEval

from evaluation.geval.azure_model import AzureOpenAIDeepEval
from evaluation.geval.metrics import (
    create_functional_req_geval,
    create_non_functional_req_geval,
)


def load_file_content(path: str) -> str:
    """Load text content from a given file path."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_ground_truths(project_root: str) -> tuple[str, str]:
    """Load functional and non-functional ground truth requirements."""
    config_path = os.path.join(project_root, "evaluation", "config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    fnr_path = os.path.join(project_root, config["ground_fnr"])
    nfnr_path = os.path.join(project_root, config["ground_nfnr"])

    with open(fnr_path, "r", encoding="utf-8") as f:
        fnr_data = json.load(f)
    with open(nfnr_path, "r", encoding="utf-8") as f:
        nfnr_data = json.load(f)

    fnr_text = "\n".join([f"- {item['Requirement']}" for item in fnr_data if 'Requirement' in item])
    nfnr_text = "\n".join([f"- {item['Requirement']}" for item in nfnr_data if 'Requirement' in item])

    return fnr_text, nfnr_text


def run_geval_evaluation(
    func_reqs_path: str,
    nfunc_reqs_path: str,
    agent_name: str = "default_agent",
    output_dir: str | None = None,
) -> Dict[str, Any]:
    """Run GEval metrics on functional and non-functional requirements."""
    eval_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_root = os.path.dirname(eval_dir)

    # 1. Load generated requirements
    func_actual = load_file_content(func_reqs_path)
    nfunc_actual = load_file_content(nfunc_reqs_path)

    # 2. Load ground truth requirements
    func_expected, nfunc_expected = load_ground_truths(project_root)

    model = AzureOpenAIDeepEval()

    print(f"\n==================================================")
    print(f"  Starting GEval Evaluation for Agent: '{agent_name}'")
    print(f"==================================================\n")

    # --- 3. Evaluate Functional Requirements ---
    print("--> [1/2] Evaluating Functional Requirements with GEval...")
    fnr_geval = create_functional_req_geval(model=model)

    fnr_test_case = LLMTestCase(
        input="Extract and structure clear, complete functional requirements based on user needs.",
        actual_output=func_actual,
        expected_output=func_expected,
    )

    fnr_geval.measure(fnr_test_case)
    print(f"    [Functional Requirements GEval]")
    print(f"    Score:  {fnr_geval.score:.2f} (Threshold: {fnr_geval.threshold})")
    print(f"    Passed: {fnr_geval.is_successful()}")
    print(f"    Reason: {fnr_geval.reason}\n")

    # --- 4. Evaluate Non-Functional Requirements ---
    print("--> [2/2] Evaluating Non-Functional Requirements with GEval...")
    nfnr_geval = create_non_functional_req_geval(model=model)

    nfnr_test_case = LLMTestCase(
        input="Extract and structure non-functional requirements covering system quality attributes.",
        actual_output=nfunc_actual,
        expected_output=nfunc_expected,
    )

    nfnr_geval.measure(nfnr_test_case)
    print(f"    [Non-Functional Requirements GEval]")
    print(f"    Score:  {nfnr_geval.score:.2f} (Threshold: {nfnr_geval.threshold})")
    print(f"    Passed: {nfnr_geval.is_successful()}")
    print(f"    Reason: {nfnr_geval.reason}\n")

    # --- 5. Format & Save Results ---
    results = {
        "agent": agent_name,
        "functional_requirements_geval": {
            "metric": fnr_geval.name,
            "score": round(float(fnr_geval.score or 0.0), 4),
            "threshold": fnr_geval.threshold,
            "passed": fnr_geval.is_successful(),
            "reason": fnr_geval.reason,
        },
        "non_functional_requirements_geval": {
            "metric": nfnr_geval.name,
            "score": round(float(nfnr_geval.score or 0.0), 4),
            "threshold": nfnr_geval.threshold,
            "passed": nfnr_geval.is_successful(),
            "reason": nfnr_geval.reason,
        },
    }

    if output_dir is None:
        output_dir = os.path.join(eval_dir, "evals", agent_name)

    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, "geval_report.json")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print(f"Saved GEval evaluation report to: {out_file}")
    print(f"==================================================\n")

    return results


def main():
    parser = argparse.ArgumentParser(description="GEval Functional & Non-Functional Requirements Evaluator")
    parser.add_argument(
        "--func-reqs", "-f",
        default="hitl_agent/outputs/final_run/03_functional_requirements.md",
        help="Path to generated functional requirements markdown file.",
    )
    parser.add_argument(
        "--nfunc-reqs", "-n",
        default="hitl_agent/outputs/final_run/04_non_functional_requirements.md",
        help="Path to generated non-functional requirements markdown file.",
    )
    parser.add_argument(
        "--agent", "-a",
        default="hitl_geval_demo",
        help="Agent run name to label evaluation report.",
    )
    args = parser.parse_args()

    run_geval_evaluation(
        func_reqs_path=args.func_reqs,
        nfunc_reqs_path=args.nfunc_reqs,
        agent_name=args.agent,
    )


if __name__ == "__main__":
    main()
