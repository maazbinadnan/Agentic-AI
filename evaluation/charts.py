import os
import json
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_merge_df(**files):
    """Load multiple CSVs and concatenate them with an architecture/type label."""
    dfs = []
    for label, filepath in files.items():
        if os.path.exists(filepath):
            df = pd.read_csv(filepath).dropna(how="all")
            df = df.assign(type=label)
            dfs.append(df)
        else:
            print(f"Warning: File not found: {filepath}")
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()


def load_and_merge_invest_df(**files):
    """Load INVEST evaluation CSVs, compute OVERALL INVEST MEAN if missing or 0.0, and merge."""
    dfs = []
    for label, filepath in files.items():
        if not os.path.exists(filepath):
            print(f"Warning: File not found: {filepath}")
            continue

        df = pd.read_csv(filepath).dropna(how="all")
        crit_col = next((c for c in df.columns if "criterion" in str(c).lower()), "criterion")
        score_col = next((c for c in df.columns if "score" in str(c).lower()), "average_score")

        df[crit_col] = df[crit_col].astype(str)
        df[score_col] = pd.to_numeric(df[score_col], errors="coerce").fillna(0.0)

        main_scores = df[df[crit_col] != "OVERALL INVEST MEAN"][score_col]
        if (df[crit_col] == "OVERALL INVEST MEAN").any():
            ov_val = float(df.loc[df[crit_col] == "OVERALL INVEST MEAN", score_col].values[0])
            if ov_val == 0.0 and len(main_scores) > 0:
                df.loc[df[crit_col] == "OVERALL INVEST MEAN", score_col] = round(float(main_scores.mean()), 4)
        elif len(main_scores) > 0:
            overall_row = pd.DataFrame([{crit_col: "OVERALL INVEST MEAN", score_col: round(float(main_scores.mean()), 4)}])
            df = pd.concat([df, overall_row], ignore_index=True)

        df = df.assign(type=label)
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()


def load_and_merge_html_accessibility_df(**files):
    """Load HTML accessibility summary CSVs and return average violations and passes per page."""
    rows = []
    for label, filepath in files.items():
        if not os.path.exists(filepath):
            print(f"Warning: File not found: {filepath}")
            continue
        df = pd.read_csv(filepath).dropna(how="all")
        if df.empty:
            continue
        mean_viol = float(df["violations_count"].mean()) if "violations_count" in df.columns else 0.0
        mean_pass = float(df["passes_count"].mean()) if "passes_count" in df.columns else 0.0

        rows.append({"metric": "Avg Violations / Page", "value": round(mean_viol, 1), "type": label})
        rows.append({"metric": "Avg Passes / Page", "value": round(mean_pass, 1), "type": label})

    return pd.DataFrame(rows)


def load_and_merge_html_severity_df(**json_files):
    """Load HTML accessibility JSON reports and return violation severity breakdown per page."""
    rows = []
    severities = ["critical", "serious", "moderate", "minor"]
    for label, filepath in json_files.items():
        if not os.path.exists(filepath):
            print(f"Warning: File not found: {filepath}")
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            data = [data]
        total_pages = len(data)
        counts = {s: 0 for s in severities}
        for page in data:
            for v in page.get("violations", []):
                imp = str(v.get("impact", "minor")).lower()
                if imp in counts:
                    counts[imp] += 1
                else:
                    counts["minor"] += 1
        for s in severities:
            avg_val = (counts[s] / total_pages) if total_pages else 0.0
            rows.append({
                "severity": s.capitalize(),
                "avg_per_page": round(avg_val, 1),
                "total_count": counts[s],
                "type": label
            })
    return pd.DataFrame(rows)


def draw_llm_coverage_bar_chart(df: pd.DataFrame, output_path: str | Path, title: str | None = None):
    """Generate and save LLM coverage verdict bar chart."""
    if df.empty:
        print(f"Skipping LLM coverage chart for {output_path} (Empty DataFrame)")
        return None

    g = sns.catplot(
        data=df, kind="bar",
        x="coverage_verdict", y="ratio", hue="type",
        errorbar="sd", palette="dark", alpha=0.6, height=6
    )
    g.despine(left=True)
    g.set_axis_labels("Coverage Verdict", "Coverage Ratio")
    if title:
        g.fig.suptitle(title, y=0.98, fontsize=14, weight="bold")

    for ax in g.axes.flat:
        for container in ax.containers:
            ax.bar_label(
                container,
                fmt="%.2f",
                padding=3,
                fontsize=9,
            )

    g.fig.subplots_adjust(top=0.9)
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    g.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(g.fig)
    print(f"Saved LLM coverage chart to: {out}")
    return g


def draw_embedding_coverage_bar_chart(df: pd.DataFrame, output_path: str | Path, title: str | None = None):
    """Generate and save Embedding cosine similarity coverage band bar chart."""
    if df.empty:
        print(f"Skipping Embedding coverage chart for {output_path} (Empty DataFrame)")
        return None

    g = sns.catplot(
        data=df, kind="bar",
        x="coverage_band", y="ratio", hue="type",
        errorbar="sd", palette="dark", alpha=0.6, height=6
    )
    g.despine(left=True)
    g.set_axis_labels("Coverage Band", "Coverage Ratio")
    if title:
        g.fig.suptitle(title, y=0.98, fontsize=14, weight="bold")

    for ax in g.axes.flat:
        for container in ax.containers:
            ax.bar_label(
                container,
                fmt="%.2f",
                padding=3,
                fontsize=9,
            )

    g.fig.subplots_adjust(top=0.9)
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    g.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(g.fig)
    print(f"Saved Embedding coverage chart to: {out}")
    return g


def draw_invest_score_bar(df: pd.DataFrame, output_path: str | Path, title: str | None = None):
    """Generate and save INVEST criteria average scores bar chart."""
    if df.empty:
        print(f"Skipping INVEST chart for {output_path} (Empty DataFrame)")
        return None

    g = sns.catplot(
        data=df, kind="bar",
        x="criterion", y="average_score", hue="type",
        errorbar="sd", palette="dark", alpha=0.6, height=6, aspect=1.8
    )
    g.despine(left=True)
    g.set_axis_labels("INVEST Criterion", "Average Score")
    if title:
        g.fig.suptitle(title, y=0.98, fontsize=14, weight="bold")

    for ax in g.axes.flat:
        for container in ax.containers:
            ax.bar_label(
                container,
                fmt="%.1f",
                padding=3,
                fontsize=9,
            )

    g.fig.subplots_adjust(top=0.9)
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    g.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(g.fig)
    print(f"Saved INVEST score chart to: {out}")
    return g


def draw_html_accessibility_bar_chart(df: pd.DataFrame, output_path: str | Path, title: str | None = None):
    """Generate and save HTML accessibility summary bar chart (Average Violations & Passes per Page)."""
    if df.empty:
        print(f"Skipping HTML Accessibility chart for {output_path} (Empty DataFrame)")
        return None

    g = sns.catplot(
        data=df, kind="bar",
        x="metric", y="value", hue="type",
        errorbar="sd", palette="dark", alpha=0.6, height=6, aspect=1.3
    )
    g.despine(left=True)
    g.set_axis_labels("Accessibility Metric", "Average Count per Page")
    if title:
        g.fig.suptitle(title, y=0.98, fontsize=14, weight="bold")

    for ax in g.axes.flat:
        for container in ax.containers:
            ax.bar_label(
                container,
                fmt="%.1f",
                padding=3,
                fontsize=9,
            )

    g.fig.subplots_adjust(top=0.9)
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    g.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(g.fig)
    print(f"Saved HTML accessibility chart to: {out}")
    return g


def draw_html_severity_bar_chart(df: pd.DataFrame, output_path: str | Path, title: str | None = None):
    """Generate and save HTML accessibility violation severity breakdown bar chart."""
    if df.empty:
        print(f"Skipping HTML Severity chart for {output_path} (Empty DataFrame)")
        return None

    g = sns.catplot(
        data=df, kind="bar",
        x="severity", y="avg_per_page", hue="type",
        errorbar="sd", palette="dark", alpha=0.6, height=6, aspect=1.5
    )
    g.despine(left=True)
    g.set_axis_labels("Axe/WCAG Violation Severity", "Average Violations per Page")
    if title:
        g.fig.suptitle(title, y=0.98, fontsize=14, weight="bold")

    for ax in g.axes.flat:
        for container in ax.containers:
            ax.bar_label(
                container,
                fmt="%.1f",
                padding=3,
                fontsize=9,
            )

    g.fig.subplots_adjust(top=0.9)
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    g.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(g.fig)
    print(f"Saved HTML severity breakdown chart to: {out}")
    return g


def generate_all_charts():
    base_dir = Path(__file__).resolve().parent
    evals_dir = base_dir / "evals"
    charts_dir = base_dir / "charts"
    charts_dir.mkdir(parents=True, exist_ok=True)

    # 1. Football Dataset (foot)
    foot_invest = {
        "hitl": evals_dir / "foot_hitl_gpt_5.4" / "foot_hitl_gpt_5.4_invest_table.csv",
        "review": evals_dir / "foot_rc_gpt_5.4" / "foot_rc_gpt_5.4_invest_table.csv",
        "single": evals_dir / "foot_single_gpt_5.4" / "single_gpt_5.5_invest_table.csv",
    }
    foot_embedding = {
        "hitl": evals_dir / "foot_hitl_gpt_5.4" / "foot_hitl_gpt_5.4_coverage_ratio_table.csv",
        "review": evals_dir / "foot_rc_gpt_5.4" / "foot_rc_gpt_5.4_coverage_ratio_table.csv",
        "single": evals_dir / "foot_single_gpt_5.4" / "single_gpt_5.5_coverage_ratio_table.csv",
    }
    foot_llm = {
        "hitl": evals_dir / "foot_hitl_gpt_5.4" / "foot_hitl_gpt_5.4_llm_eval_table.csv",
        "review": evals_dir / "foot_rc_gpt_5.4" / "foot_rc_gpt_5.4_llm_eval_table.csv",
        "single": evals_dir / "foot_single_gpt_5.4" / "single_gpt_5.5_llm_eval_table.csv",
    }
    foot_html_csv = {
        "hitl": evals_dir / "foot_hitl_gpt_5.4" / "foot_hitl_gpt_5.4_html_accessibility_table.csv",
        "review": evals_dir / "foot_rc_gpt_5.4" / "foot_rc_gpt_5.4_html_accessibility_table.csv",
        "single": evals_dir / "foot_single_gpt_5.4" / "foot_single_gpt_5.4_html_accessibility_table.csv",
    }
    foot_html_json = {
        "hitl": evals_dir / "foot_hitl_gpt_5.4" / "foot_hitl_gpt_5.4_html_accessibility_eval.json",
        "review": evals_dir / "foot_rc_gpt_5.4" / "foot_rc_gpt_5.4_html_accessibility_eval.json",
        "single": evals_dir / "foot_single_gpt_5.4" / "foot_single_gpt_5.4_html_accessibility_eval.json",
    }

    print("\n--- Generating Football (LiveFootball) Charts ---")
    foot_invest_df = load_and_merge_invest_df(**foot_invest)
    draw_invest_score_bar(
        foot_invest_df,
        output_path=charts_dir / "foot_invest_scores.png",
        title="Football Requirements: INVEST Scores by Agent Architecture"
    )

    foot_embedding_df = load_and_merge_df(**foot_embedding)
    draw_embedding_coverage_bar_chart(
        foot_embedding_df,
        output_path=charts_dir / "foot_embedding_coverage.png",
        title="Football Requirements: Embedding Coverage by Agent Architecture"
    )

    foot_llm_df = load_and_merge_df(**foot_llm)
    draw_llm_coverage_bar_chart(
        foot_llm_df,
        output_path=charts_dir / "foot_llm_coverage.png",
        title="Football Requirements: LLM Coverage by Agent Architecture"
    )

    foot_html_df = load_and_merge_html_accessibility_df(**foot_html_csv)
    draw_html_accessibility_bar_chart(
        foot_html_df,
        output_path=charts_dir / "foot_html_accessibility.png",
        title="Football Mockups: HTML Accessibility Summary (Passes vs Violations)"
    )

    foot_severity_df = load_and_merge_html_severity_df(**foot_html_json)
    draw_html_severity_bar_chart(
        foot_severity_df,
        output_path=charts_dir / "foot_html_severity.png",
        title="Football Mockups: Axe/WCAG Violation Severity Breakdown"
    )

    # 2. Pure Dataset (pure)
    pure_invest = {
        "hitl": evals_dir / "pure_hitl_gpt_5.4" / "pure_hitl_gpt_5.4_invest_table.csv",
        "review": evals_dir / "pure_rc_gpt_5.4" / "pure_rc_gpt_5.4_invest_table.csv",
        "single": evals_dir / "pure_single_gpt_5.4" / "pure_single_gpt_5.4_invest_table.csv",
    }
    pure_embedding = {
        "hitl": evals_dir / "pure_hitl_gpt_5.4" / "pure_hitl_gpt_5.4_coverage_ratio_table.csv",
        "review": evals_dir / "pure_rc_gpt_5.4" / "pure_rc_gpt_5.4_coverage_ratio_table.csv",
        "single": evals_dir / "pure_single_gpt_5.4" / "pure_single_gpt_5.4_coverage_ratio_table.csv",
    }
    pure_llm = {
        "hitl": evals_dir / "pure_hitl_gpt_5.4" / "pure_hitl_gpt_5.4_llm_eval_table.csv",
        "review": evals_dir / "pure_rc_gpt_5.4" / "pure_rc_gpt_5.4_llm_eval_table.csv",
        "single": evals_dir / "pure_single_gpt_5.4" / "pure_single_gpt_5.4_llm_eval_table.csv",
    }
    pure_html_csv = {
        "hitl": evals_dir / "pure_hitl_gpt_5.4" / "pure_hitl_gpt_5.4_html_accessibility_table.csv",
        "review": evals_dir / "pure_rc_gpt_5.4" / "pure_rc_gpt_5.4_html_accessibility_table.csv",
        "single": evals_dir / "pure_single_gpt_5.4" / "pure_single_gpt_5.4_html_accessibility_table.csv",
    }
    pure_html_json = {
        "hitl": evals_dir / "pure_hitl_gpt_5.4" / "pure_hitl_gpt_5.4_html_accessibility_eval.json",
        "review": evals_dir / "pure_rc_gpt_5.4" / "pure_rc_gpt_5.4_html_accessibility_eval.json",
        "single": evals_dir / "pure_single_gpt_5.4" / "pure_single_gpt_5.4_html_accessibility_eval.json",
    }

    print("\n--- Generating Pure Dataset Charts ---")
    pure_invest_df = load_and_merge_invest_df(**pure_invest)
    draw_invest_score_bar(
        pure_invest_df,
        output_path=charts_dir / "pure_invest_scores.png",
        title="Pure Requirements: INVEST Scores by Agent Architecture"
    )

    pure_embedding_df = load_and_merge_df(**pure_embedding)
    draw_embedding_coverage_bar_chart(
        pure_embedding_df,
        output_path=charts_dir / "pure_embedding_coverage.png",
        title="Pure Requirements: Embedding Coverage by Agent Architecture"
    )

    pure_llm_df = load_and_merge_df(**pure_llm)
    draw_llm_coverage_bar_chart(
        pure_llm_df,
        output_path=charts_dir / "pure_llm_coverage.png",
        title="Pure Requirements: LLM Coverage by Agent Architecture"
    )

    pure_html_df = load_and_merge_html_accessibility_df(**pure_html_csv)
    draw_html_accessibility_bar_chart(
        pure_html_df,
        output_path=charts_dir / "pure_html_accessibility.png",
        title="Pure Mockups: HTML Accessibility Summary (Passes vs Violations)"
    )

    pure_severity_df = load_and_merge_html_severity_df(**pure_html_json)
    draw_html_severity_bar_chart(
        pure_severity_df,
        output_path=charts_dir / "pure_html_severity.png",
        title="Pure Mockups: Axe/WCAG Violation Severity Breakdown"
    )

# def generate_confusion_matrix(filepath:str,agent_name:str | None):
    








if __name__ == "__main__":
    generate_all_charts()
