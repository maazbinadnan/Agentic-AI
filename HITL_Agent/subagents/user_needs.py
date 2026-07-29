from pathlib import Path
from langchain.agents import create_agent
from langchain_core.tools import tool

from hitl_agent._common_ import llm, load_prompt, read_file

__all__ = ["user_needs_subagent", "save_user_needs_report"]


@tool
def save_user_needs_report(report_markdown: str, output_dir: str = "outputs") -> str:
    """Saves the formal User Needs Markdown report containing personas and structured UN-xxx requirements.
    
    Parameters
    ----------
    report_markdown : str
        The complete markdown text report to save into the workspace.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / "02_user_needs_report.md"
    file_path.write_text(report_markdown, encoding="utf-8")
    print(f"\n[User Needs Agent] Successfully saved User Needs report to '{file_path.resolve()}'")
    return f"Successfully saved 02_user_needs_report.md to '{file_path.resolve()}'"


user_needs_subagent = create_agent(
    model=llm,
    tools=[save_user_needs_report, read_file],
    system_prompt=load_prompt("user_needs.md"),
    name="user_needs_generator",
)
