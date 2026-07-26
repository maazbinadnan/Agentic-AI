import os
import json
import pandas as pd
from typing import List, Dict, Any
from evaluation_v2.pipeline import run_evaluation_pipeline

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "Data")
SOURCE_DOC = os.path.join(DATA_DIR, "requirements.md")
GT_FUNCTIONAL = os.path.join(DATA_DIR, "functional_requirements.json")
GT_NON_FUNCTIONAL = os.path.join(DATA_DIR, "non_functional_requirements.json")

EVAL_OUTPUT_DIR = os.path.join(BASE_DIR, "evaluation_v2", "results")


def run_batch_evaluation(runs: List[Dict[str, str]], model: str = "gpt-4o") -> pd.DataFrame:
    """
    Runs batch evaluation across multiple generated architecture run output folders
    and returns a comparative pandas DataFrame.
    """
    records: List[Dict[str, Any]] = []

    for run_info in runs:
        arch_name = run_info.get("architecture", "Unknown")
        target_type = run_info.get("target_type", "Functional")
        run_output_dir = run_info["run_output_dir"]
        gt_file = GT_FUNCTIONAL if target_type.lower() == "functional" else GT_NON_FUNCTIONAL

        output_json = os.path.join(
            EVAL_OUTPUT_DIR,
            arch_name.lower().replace(" ", "_"),
            f"eval_summary_{target_type.lower()}.json"
        )

        try:
            summary = run_evaluation_pipeline(
                architecture_name=arch_name,
                target_type=target_type,
                source_doc_file=SOURCE_DOC,
                ground_truth_file=gt_file,
                run_output_dir=run_output_dir,
                output_summary_file=output_json,
                model=model
            )

            record = {
                "Architecture": arch_name,
                "Target Type": target_type,
                "Total Reqs": summary.deterministic_metrics.total_requirements,
                "BDD Compliance %": summary.deterministic_metrics.bdd_compliance_percentage,
                "Ambiguity Density": summary.deterministic_metrics.ambiguity_density_per_100_words,
                "Redundancy Index": summary.deterministic_metrics.redundancy_score,
                "Semantic Recall": summary.alignment_metrics.recall,
                "Semantic Precision": summary.alignment_metrics.precision,
                "Macro F1": summary.alignment_metrics.macro_f1,
                "G-Eval Overall": summary.g_eval_metrics.mean_overall_score,
            }

            if summary.ixd_metrics:
                record["Mockup Files"] = summary.ixd_metrics.total_mockup_files
                record["Interactive Components"] = summary.ixd_metrics.total_interactive_components
                record["Story Coverage %"] = summary.ixd_metrics.story_mapping_coverage_percentage

            if summary.system_metrics:
                record["Total Iterations"] = summary.system_metrics.total_iterations
                record["Feedback Rounds"] = summary.system_metrics.feedback_rounds_count

            records.append(record)

        except Exception as e:
            print(f"Error evaluating [{arch_name}] ({target_type}): {e}")

    df = pd.DataFrame(records)
    csv_path = os.path.join(EVAL_OUTPUT_DIR, "architecture_comparison_matrix.csv")
    os.makedirs(EVAL_OUTPUT_DIR, exist_ok=True)
    df.to_csv(csv_path, index=False)
    print(f"\nSaved Architecture Comparison Table to: {csv_path}")

    return df


if __name__ == "__main__":
    # Example test runs
    sample_runs = [
        {
            "architecture": "Single Agent Final",
            "target_type": "Functional",
            "run_output_dir": os.path.join(BASE_DIR, "single_agent", "outputs", "test_run")
        },
        {
            "architecture": "Supervisor Worker",
            "target_type": "Functional",
            "run_output_dir": os.path.join(BASE_DIR, "supervisor_worker", "outputs", "test_run")
        }
    ]

    print("=== Launching Evaluation V2 End-to-End Batch Run ===")
    df_results = run_batch_evaluation(sample_runs, model="gpt-4o")
    print("\n=== Benchmark Summary Matrix ===")
    print(df_results.to_string())
