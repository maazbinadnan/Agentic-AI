import os
import json
from pathlib import Path
from typing import Dict, Any, List
import pandas as pd

from global_layer.functions import _write_json_file


def evaluate_html_accessibility(
    html_dir_or_file: str,
    output_json_path: str | None = None,
    output_csv_path: str | None = None,
) -> List[Dict[str, Any]]:
    """Evaluates HTML mockup file(s) for WCAG/Axe accessibility violations using Playwright and Axe.

    Parameters
    ----------
    html_dir_or_file : str
        Path to an HTML file or a directory containing HTML files.
    output_json_path : str, optional
        Path to save the detailed JSON evaluation report.
    output_csv_path : str, optional
        Path to save the summary CSV table.

    Returns
    -------
    List[Dict[str, Any]]
        Detailed accessibility audit results per HTML file.
    """
    try:
        from playwright.sync_api import sync_playwright
        from axe_playwright_python.sync_playwright import Axe
    except ImportError as e:
        print(
            "\n[HTML Accessibility Eval] Error: Required packages are missing.\n"
            "Please install them using:\n"
            "    pip install playwright axe-playwright-python\n"
            "    playwright install chromium\n"
        )
        raise e

    target_path = Path(html_dir_or_file).resolve()
    if target_path.is_file():
        html_files = [target_path]
    elif target_path.is_dir():
        html_files = sorted(list(set(target_path.rglob("*.html"))))
    else:
        print(f"[HTML Accessibility Eval] Target HTML file/directory not found: {html_dir_or_file}")
        return []

    if not html_files:
        print(f"[HTML Accessibility Eval] No .html files found in: {html_dir_or_file}")
        return []

    results_list: List[Dict[str, Any]] = []
    axe = Axe()

    print(f"\n[HTML Accessibility Eval] Auditing {len(html_files)} HTML file(s) using Playwright + Axe...")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        for html_file in html_files:
            file_url = html_file.as_uri()
            print(f"  Auditing: {html_file.name} ...")
            try:
                page.goto(file_url)
                axe_results = axe.run(page)

                violations = axe_results.response.get("violations", [])
                passes = axe_results.response.get("passes", [])
                incomplete = axe_results.response.get("incomplete", [])
                inapplicable = axe_results.response.get("inapplicable", [])

                file_audit = {
                    "filename": html_file.name,
                    "filepath": str(html_file),
                    "violations_count": len(violations),
                    "passes_count": len(passes),
                    "incomplete_count": len(incomplete),
                    "inapplicable_count": len(inapplicable),
                    "report_summary": axe_results.generate_report(),
                    "violations": [
                        {
                            "id": v.get("id"),
                            "impact": v.get("impact"),
                            "description": v.get("description"),
                            "help": v.get("help"),
                            "helpUrl": v.get("helpUrl"),
                            "nodes_count": len(v.get("nodes", [])),
                        }
                        for v in violations
                    ],
                }
                results_list.append(file_audit)
                print(f"    -> Violations: {len(violations)}, Passes: {len(passes)}")

            except Exception as ex:
                print(f"    -> Error evaluating {html_file.name}: {ex}")
                results_list.append({
                    "filename": html_file.name,
                    "filepath": str(html_file),
                    "error": str(ex),
                    "violations_count": -1,
                    "passes_count": 0,
                    "incomplete_count": 0,
                    "inapplicable_count": 0,
                    "violations": [],
                })

        browser.close()

    # Save detailed JSON
    if output_json_path:
        _write_json_file(output_json_path, results_list)
        print(f"  Detailed JSON report saved to: {output_json_path}")

    # Build and save CSV summary table
    if output_csv_path:
        build_html_accessibility_table(results_list, output_csv_path)

    return results_list


def build_html_accessibility_table(
    results_or_filepath: List[Dict[str, Any]] | str,
    output_table_path: str | None = None,
) -> pd.DataFrame:
    """Generates a summary DataFrame for HTML accessibility evaluations."""
    if isinstance(results_or_filepath, str):
        with open(results_or_filepath, "r", encoding="utf-8") as f:
            results_list = json.load(f)
    else:
        results_list = results_or_filepath

    if not isinstance(results_list, list):
        results_list = [results_list]

    rows = []
    for item in results_list:
        rows.append({
            "html_filename": item.get("filename"),
            "violations_count": item.get("violations_count", 0),
            "passes_count": item.get("passes_count", 0),
            "incomplete_count": item.get("incomplete_count", 0),
            "status": "PASS (0 Violations)" if item.get("violations_count") == 0 else f"FAIL ({item.get('violations_count')} Violations)",
        })

    table = pd.DataFrame(rows)

    if output_table_path:
        output_dir = os.path.dirname(output_table_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        table.to_csv(output_table_path, index=False)
        print(f"Saved HTML accessibility summary table to: {output_table_path}")

    return table


if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else r"hitl_agent/outputs/stream_testl/html"
    evaluate_html_accessibility(target, "scratch/html_eval_test.json", "scratch/html_eval_test.csv")
