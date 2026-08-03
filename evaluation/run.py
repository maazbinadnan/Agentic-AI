"""Evaluation Runner — modular CLI entrypoint.

Usage examples:
    # Run all evaluations for HITL agent
    python -m evaluation.run --agent hitl \
        --func-reqs hitl_agent/outputs/stream_testl/03_functional_requirements.md \
        --nfunc-reqs hitl_agent/outputs/stream_testl/04_non_functional_requirements.md

    # Run all evaluations for single agent
    python -m evaluation.run --agent single_agent \
        --func-reqs single_agent/outputs/test_1/02_functional_requirements.md \
        --nfunc-reqs single_agent/outputs/test_1/03_non_functional_requirements.md

    # Run only embedding coverage (skip LLM judge)
    python -m evaluation.run --agent hitl \
        --func-reqs hitl_agent/outputs/stream_testl/03_functional_requirements.md \
        --nfunc-reqs hitl_agent/outputs/stream_testl/04_non_functional_requirements.md \
        --skip-llm-judge

    # Run only LLM judge (skip embedding coverage)
    python -m evaluation.run --agent hitl \
        --func-reqs hitl_agent/outputs/stream_testl/03_functional_requirements.md \
        --nfunc-reqs hitl_agent/outputs/stream_testl/04_non_functional_requirements.md \
        --skip-coverage
"""

import argparse
import os
import json
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Modular Evaluation Runner — pass agent name and generated requirement files at runtime.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--agent", "-a",
        required=True,
        help="Agent name used to namespace output folder (e.g., 'single_agent', 'hitl', 'supervisor_worker').",
    )
    parser.add_argument(
        "--func-reqs", "-f",
        required=True,
        help="Path to generated functional requirements file (relative to project root or absolute).",
    )
    parser.add_argument(
        "--nfunc-reqs", "-n",
        required=True,
        help="Path to generated non-functional requirements file (relative to project root or absolute).",
    )
    parser.add_argument(
        "--skip-coverage",
        action="store_true",
        help="Skip embedding-based coverage evaluation.",
    )
    parser.add_argument(
        "--skip-llm-judge",
        action="store_true",
        help="Skip LLM judge evaluation.",
    )
    parser.add_argument(
        "--skip-iso-audit",
        action="store_true",
        help="Skip ISO 29148 requirements quality audit.",
    )
    parser.add_argument(
        "--skip-viz",
        action="store_true",
        help="Skip coverage ratio visualization table.",
    )
    parser.add_argument(
        "--model", "-m",
        default=None,
        help="LLM model deployment name for LLM judge (default: from MODEL env var or gpt-4.1).",
    )
    args = parser.parse_args()

    # --- Resolve paths ---
    eval_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(eval_dir)

    with open(os.path.join(eval_dir, "config.json"), "r") as f:
        config = json.load(f)

    evals_folder = os.path.join(project_root, config["evals_folder"])
    agent_output_dir = os.path.join(evals_folder, args.agent)
    os.makedirs(agent_output_dir, exist_ok=True)

    # Resolve input files (support both relative-to-root and absolute)
    func_reqs = args.func_reqs if os.path.isabs(args.func_reqs) else os.path.join(project_root, args.func_reqs)
    nfunc_reqs = args.nfunc_reqs if os.path.isabs(args.nfunc_reqs) else os.path.join(project_root, args.nfunc_reqs)

    # Validate inputs exist
    for label, path in [("func-reqs", func_reqs), ("nfunc-reqs", nfunc_reqs)]:
        if not os.path.isfile(path):
            print(f"Error: {label} file not found: {path}")
            sys.exit(1)

    coverage_json_path = os.path.join(agent_output_dir, f"{args.agent}_coverage.json")
    llm_eval_json_path = os.path.join(agent_output_dir, f"{args.agent}_llm_eval.json")
    llm_eval_table_path = os.path.join(agent_output_dir, f"{args.agent}_llm_eval_table.csv")
    iso_eval_json_path = os.path.join(agent_output_dir, f"{args.agent}_iso_29148_eval.json")
    iso_table_path = os.path.join(agent_output_dir, f"{args.agent}_iso_29148_table.json")
    ratio_table_path = os.path.join(agent_output_dir, f"{args.agent}_coverage_ratio_table.csv")

    print("=" * 60)
    print(f"Evaluation Runner — Agent: {args.agent}")
    print(f"  Functional Reqs:     {func_reqs}")
    print(f"  Non-Functional Reqs: {nfunc_reqs}")
    print(f"  Output Directory:    {agent_output_dir}")
    print("=" * 60)

    # --- Step 1: Embedding-based Coverage ---
    if not args.skip_coverage:
        print("\n[Step 1/4] Running embedding-based coverage evaluation...")
        from evaluation.confusion_matrix import get_ground_truths, get_generated, requirements_coverage

        ground_truths = get_ground_truths()
        generated_reqs = get_generated(func_reqs, nfunc_reqs)

        print(f"  Ground truth items: {len(ground_truths)}")
        print(f"  Generated items:    {len(generated_reqs)}")

        requirements_coverage(
            ground_truths=ground_truths,
            generated_reqs=generated_reqs,
            output_json_path=coverage_json_path,
        )
    else:
        print("\n[Step 1/4] Skipped embedding-based coverage (--skip-coverage).")

    # --- Step 2: LLM Judge ---
    if not args.skip_llm_judge:
        print("\n[Step 2/4] Running LLM Judge ground truth coverage evaluation...")
        from evaluation.llm_judge import evaluate_requirements

        evaluate_requirements(
            func_reqs=func_reqs,
            non_func_reqs=nfunc_reqs,
            output_file=llm_eval_json_path,
            model=args.model,
        )
        print(f"  LLM Judge results saved to: {llm_eval_json_path}")
    else:
        print("\n[Step 2/4] Skipped LLM Judge coverage (--skip-llm-judge).")

    # --- Step 3: ISO 29148 Quality Audit ---
    if not args.skip_iso_audit:
        print("\n[Step 3/4] Running ISO 29148 Requirements Quality Audit...")
        from evaluation.llm_judge import evaluate_iso_29148_quality

        evaluate_iso_29148_quality(
            func_reqs=func_reqs,
            non_func_reqs=nfunc_reqs,
            output_file=iso_eval_json_path,
            model=args.model,
        )
        print(f"  ISO 29148 Quality Audit results saved to: {iso_eval_json_path}")
    else:
        print("\n[Step 3/4] Skipped ISO 29148 Quality Audit (--skip-iso-audit).")

    # --- Step 4: Coverage & ISO Summary Tables ---
    if not args.skip_viz:
        print("\n[Step 4/4] Building summary and ratio tables...")
        from evaluation.visualize_metrics import (
            build_coverage_ratio_table,
            build_coverage_llm_ratio_table,
            build_iso_table,
        )

        if not args.skip_coverage and os.path.isfile(coverage_json_path):
            print("\nEmbedding Coverage Ratio Table:")
            table = build_coverage_ratio_table(coverage_json_path, ratio_table_path)
            print(table.to_string(index=False))

        if not args.skip_llm_judge and os.path.isfile(llm_eval_json_path):
            print("\nLLM Judge Coverage Ratio Table:")
            llm_table = build_coverage_llm_ratio_table(llm_eval_json_path, llm_eval_table_path)
            print(llm_table.to_string(index=False))

        if not args.skip_iso_audit and os.path.isfile(iso_eval_json_path):
            print("\nISO 29148 Quality Summary Table:")
            iso_table = build_iso_table(iso_eval_json_path, iso_table_path)
    else:
        print("\n[Step 4/4] Skipped visualization.")

    print("\n" + "=" * 60)
    print("Evaluation complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()
