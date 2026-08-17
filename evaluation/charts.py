import pandas as pd
import seaborn as sns
from pathlib import Path


def load_and_merge_df(**files):
    return pd.concat(
        [pd.read_csv(filepath).assign(type=label) for label, filepath in files.items()],
        ignore_index=True
    )

def draw_llm_coverage_bar_chart(df:pd.DataFrame):
    g = sns.catplot(
        data = df , kind ="bar",
        x = "coverage_verdict" , y = "ratio" , hue = "type",
        errorbar="sd", palette="dark", alpha=.6, height=6
    )
    g.despine(left=True)
    g.set_axis_labels("", "Coverage Ratio")

    for ax in g.axes.flat:
        for container in ax.containers:
            ax.bar_label(
                container,
                fmt="%.2f",  # 2 decimal places (use '%.1f%%' if ratio is 0-100)
                padding=3,  # Space between bar top (or error bar) and label
                fontsize=9,
            )

    # Ensure labels don't get clipped by the top of the plot
    g.fig.subplots_adjust(top=0.9)

    Path(r'evaluation\charts\llm_coverage.png').parent.mkdir(parents=True, exist_ok=True)
    g.savefig(r'evaluation\charts\llm_coverage.png')
    print(f"Chart saved")
    return g

def draw_invest_score_bar(df:pd.DataFrame):
    g = sns.catplot(
        data = df , kind ="bar",
        x = "criterion" , y = "average_score" , hue = "type",
        errorbar="sd", palette="dark", alpha=.6, height=6, aspect=1.8
    )
    g.despine(left=True)
    g.set_axis_labels("", "Average Score")

    for ax in g.axes.flat:
        for container in ax.containers:
            ax.bar_label(
                container,
                fmt="%.2f",  # 2 decimal places (use '%.1f%%' if ratio is 0-100)
                padding=3,  # Space between bar top (or error bar) and label
                fontsize=9,
            )

    # Ensure labels don't get clipped by the top of the plot
    g.fig.subplots_adjust(top=0.9)

    Path(r'evaluation\charts\invest_scores.png').parent.mkdir(parents=True, exist_ok=True)
    g.savefig(r'evaluation\charts\invest_scores.png')
    print(f"Chart saved")
    return g


df_filepaths = [
    r'evaluation\evals\pure_hitl_gpt_5.4\pure_hitl_gpt_5.4_invest_table.csv',
    r'evaluation\evals\pure_rc_gpt_5.4\pure_rc_gpt_5.4_invest_table.csv',
    r'evaluation\evals\pure_single_gpt_5.4\pure_single_gpt_5.4_invest_table.csv'
]

final_df = load_and_merge_df(
    hitl=df_filepaths[0],
    review=df_filepaths[1],
    single=df_filepaths[2]
)

draw_invest_score_bar(final_df)

print(final_df)

