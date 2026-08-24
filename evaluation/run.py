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
        "--user-stories", "-u",
        default=None,
        help="Path to generated user stories file (05_user_stories.md). If omitted, attempts to auto-locate in agent directory.",
    )
    parser.add_argument(
        "--skip-coverage",
        action="store_true",
        help="Skip embedding-based coverage evaluation.",
    )
    parser.add_argument(
        "--skip-llm-judge",
        action="store_true",
        help="Skip LLM judge coverage evaluation.",
    )
    parser.add_argument(
        "--skip-iso-audit",
        action="store_true",
        help="Skip ISO 29148 requirements quality audit.",
    )
    parser.add_argument(
        "--skip-invest-eval",
        action="store_true",
        help="Skip INVEST user story evaluation.",
    )
    parser.add_argument(
        "--html-dir", "-hd",
        default=None,
        help="Path to generated HTML directory or file. If omitted, attempts to auto-locate 'html/' subfolder.",
    )
    parser.add_argument(
        "--skip-html-eval",
        action="store_true",
        help="Skip Playwright/Axe HTML accessibility evaluation.",
    )
    parser.add_argument(
        "--code-dir", "-cd",
        default=None,
        help="Path to generated code directory (.js, .ts, .py). If omitted, attempts to auto-locate.",
    )
    parser.add_argument(
        "--skip-accs",
        action="store_true",
        help="Skip Acceptance Criteria Extraction and Coverage Score (ACCS) evaluation.",
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

    # Auto-resolve user stories file if not provided
    if args.user_stories:
        user_stories = args.user_stories if os.path.isabs(args.user_stories) else os.path.join(project_root, args.user_stories)
    else:
        # Check standard folder locations
        possible_us_dir = os.path.dirname(func_reqs)
        default_us_path = os.path.join(possible_us_dir, "05_user_stories.md")
        user_stories = default_us_path if os.path.isfile(default_us_path) else None

    # Auto-resolve html dir if not provided
    if args.html_dir:
        html_target = args.html_dir if os.path.isabs(args.html_dir) else os.path.join(project_root, args.html_dir)
    else:
        possible_us_dir = os.path.dirname(func_reqs)
        default_html_dir = os.path.join(possible_us_dir, "html")
        html_target = default_html_dir if (os.path.isdir(default_html_dir) or os.path.isfile(default_html_dir)) else None

    # Validate inputs exist
    for label, path in [("func-reqs", func_reqs), ("nfunc-reqs", nfunc_reqs)]:
        if not os.path.isfile(path):
            print(f"Error: {label} file not found: {path}")
            sys.exit(1)

    coverage_json_path = os.path.join(agent_output_dir, f"{args.agent}_coverage.json")
    llm_eval_json_path = os.path.join(agent_output_dir, f"{args.agent}_llm_eval.json")
    llm_eval_table_path = os.path.join(agent_output_dir, f"{args.agent}_llm_eval_table.csv")
    iso_eval_json_path = os.path.join(agent_output_dir, f"{args.agent}_iso_eval.json")
    iso_table_path = os.path.join(agent_output_dir, f"{args.agent}_iso_table.csv")
    invest_eval_json_path = os.path.join(agent_output_dir, f"{args.agent}_invest_eval.json")
    invest_table_path = os.path.join(agent_output_dir, f"{args.agent}_invest_table.csv")
    html_eval_json_path = os.path.join(agent_output_dir, f"{args.agent}_html_accessibility_eval.json")
    html_table_path = os.path.join(agent_output_dir, f"{args.agent}_html_accessibility_table.csv")
    accs_eval_json_path = os.path.join(agent_output_dir, f"{args.agent}_accs_eval.json")
    accs_table_path = os.path.join(agent_output_dir, f"{args.agent}_accs_table.csv")
    ratio_table_path = os.path.join(agent_output_dir, f"{args.agent}_coverage_ratio_table.csv")

    code_target = args.code_dir if (args.code_dir and (os.path.isabs(args.code_dir) or os.path.isdir(os.path.join(project_root, args.code_dir)))) else html_target

    print("=" * 60)
    print(f"Evaluation Runner — Agent: {args.agent}")
    print(f"  Functional Reqs:     {func_reqs}")
    print(f"  Non-Functional Reqs: {nfunc_reqs}")
    print(f"  User Stories File:   {user_stories or 'None'}")
    print(f"  HTML Mockups Target: {html_target or 'None'}")
    print(f"  Code Target:         {code_target or 'None'}")
    print("=" * 60)

    # --- Step 1: Embedding-based Coverage ---
    if not args.skip_coverage:

        print("\n[Step 1/5] Running embedding-based coverage evaluation...")
        from evaluation.confusion_matrix import get_ground_truths, get_generated, requirements_coverage
        from evaluation.visualize_metrics import build_coverage_ratio_table

        ground_truths = get_ground_truths()
        generated_reqs = get_generated(func_reqs, nfunc_reqs)

        print(f"  Ground truth items: {len(ground_truths)}")
        print(f"  Generated items:    {len(generated_reqs)}")

        requirements_coverage(
            ground_truths=ground_truths,
            generated_reqs=generated_reqs,
            output_json_path=coverage_json_path,
        )
        if os.path.isfile(coverage_json_path):
            print("\n  Embedding Coverage Ratio Table:")
            table = build_coverage_ratio_table(coverage_json_path, ratio_table_path)
            print(table.to_string(index=False))
    else:
        print("\n[Step 1/5] Skipped embedding-based coverage (--skip-coverage).")

    # --- Step 2: LLM Judge Coverage ---
    if not args.skip_llm_judge:
        print("\n[Step 2/5] Running LLM Judge ground truth coverage evaluation...")
        from evaluation.llm_judge import evaluate_requirements
        from evaluation.visualize_metrics import build_coverage_llm_ratio_table

        evaluate_requirements(
            func_reqs=func_reqs,
            non_func_reqs=nfunc_reqs,
            output_file=llm_eval_json_path,
            model=args.model,
        )
        print(f"  LLM Judge results saved to: {llm_eval_json_path}")
        if os.path.isfile(llm_eval_json_path):
            print("\n  LLM Judge Coverage Ratio Table:")
            llm_table = build_coverage_llm_ratio_table(llm_eval_json_path, llm_eval_table_path)
            print(llm_table.to_string(index=False))
    else:
        print("\n[Step 2/5] Skipped LLM Judge coverage (--skip-llm-judge).")

    # --- Step 3: INVEST User Stories Evaluation ---
    if not args.skip_invest_eval:
        if user_stories and os.path.isfile(user_stories):
            print("\n[Step 3/5] Running INVEST Agile User Story Evaluation...")
            from evaluation.llm_judge import evaluate_invest_user_stories
            from evaluation.visualize_metrics import build_invest_table

            evaluate_invest_user_stories(
                user_stories_file_or_text=user_stories,
                output_file=invest_eval_json_path,
                model=args.model,
            )
            print(f"  INVEST Evaluation results saved to: {invest_eval_json_path}")
            if os.path.isfile(invest_eval_json_path):
                print("\n  INVEST User Story Evaluation Table:")
                invest_table = build_invest_table(invest_eval_json_path, invest_table_path)
                print(invest_table.to_string(index=False))
        else:
            print("\n[Step 3/5] Skipped INVEST Evaluation (User Stories file not found or not provided).")
    else:
        print("\n[Step 3/5] Skipped INVEST Evaluation (--skip-invest-eval).")

    # --- Step 4: HTML Playwright / Axe Accessibility Evaluation ---
    if not args.skip_html_eval:
        if html_target and (os.path.isdir(html_target) or os.path.isfile(html_target)):
            print("\n[Step 4/5] Running HTML Playwright/Axe Accessibility Evaluation...")
            from evaluation.html_evals import evaluate_html_accessibility, build_html_accessibility_table


            try:
                evaluate_html_accessibility(
                    html_dir_or_file=html_target,
                    output_json_path=html_eval_json_path,
                    output_csv_path=html_table_path,
                )
                if os.path.isfile(html_table_path):
                    print("\n  HTML Accessibility Summary Table:")
                    html_table = build_html_accessibility_table(html_eval_json_path, html_table_path)
                    print(html_table.to_string(index=False))
            except ImportError:
                print("  Skipped HTML accessibility evaluation due to missing packages.")
        else:
            print("\n[Step 4/5] Skipped HTML Accessibility Evaluation (HTML target directory/file not found or not provided).")
    else:
        print("\n[Step 4/5] Skipped HTML Accessibility Evaluation (--skip-html-eval).")

    # --- Step 5: Acceptance Criteria Coverage Score (ACCS) ---
    if not args.skip_accs:
        if user_stories and os.path.isfile(user_stories) and html_target:
            print("\n[Step 5/5] Running Acceptance Criteria Coverage Score (ACCS) Evaluation...")
            from evaluation.accs_eval import evaluate_accs, build_accs_table

            accs_report = evaluate_accs(
                user_stories_source=user_stories,
                html_target=html_target,
                code_target=code_target,
                output_json_path=accs_eval_json_path,
                output_csv_path=accs_table_path,
                model=args.model,
            )
            print(f"  ACCS Evaluation results saved to: {accs_eval_json_path}")
            if os.path.isfile(accs_table_path):
                print("\n  ACCS Summary Table:")
                accs_table = build_accs_table(accs_report)
                print(accs_table.to_string(index=False))
        else:
            print("\n[Step 5/5] Skipped ACCS Evaluation (Requires both User Stories and HTML/Code target).")
    else:
        print("\n[Step 5/5] Skipped ACCS Evaluation (--skip-accs).")

    print("\n" + "=" * 60)
    print("Evaluation complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()
