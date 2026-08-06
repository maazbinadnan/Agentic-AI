from pathlib import Path
from langchain.agents import create_agent
from langchain_core.tools import tool

from hitl_agent._common_ import llm, load_prompt, read_file

__all__ = [
    "re_validation_subagent",
    "save_re_validation_report",
]


@tool
def save_re_validation_report(report_markdown: str, output_dir: str = "outputs") -> str:
    """Saves the formal Requirements Engineering Validation Markdown report (06_analysis_summary.md.md) containing audit findings, traceability matrix, and quality scores.
    
    Parameters
    ----------
    report_markdown : str
        The complete markdown text report to save into the workspace.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / "re_validation_report.md"
    file_path.write_text(report_markdown, encoding="utf-8")
    print(f"\n[re validation agent] Successfully saved RE validation report to '{file_path.resolve()}'")
    return f"Successfully saved re_validation_report.md to '{file_path.resolve()}'"


re_validation_subagent = create_agent(
    model=llm,
    tools=[save_re_validation_report, read_file],
    system_prompt=load_prompt("re_validation.md"),
    name="re_validation_specialist",
)
