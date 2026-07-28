from pathlib import Path
from langchain.agents import create_agent
from langchain_core.tools import tool

from ba_team_agent._common_ import llm, load_prompt, read_file

__all__ = ["functional_requirements_subagent", "save_functional_requirements_report"]


@tool
def save_functional_requirements_report(report_markdown: str, output_dir: str = "outputs") -> str:
    """Saves the formal Functional Requirements Markdown report containing FR-xxx specifications.
    
    Parameters
    ----------
    report_markdown : str
        The complete markdown text report to save into the workspace.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / "03_functional_requirements.md"
    file_path.write_text(report_markdown, encoding="utf-8")
    print(f"\n[ba_team_agent] Successfully saved Functional Requirements report to '{file_path.resolve()}'")
    return f"Successfully saved 03_functional_requirements.md to '{file_path.resolve()}'"


functional_requirements_subagent = create_agent(
    model=llm,
    tools=[save_functional_requirements_report, read_file],
    system_prompt=load_prompt("functional_requirements.md"),
    name="functional_requirements_generator",
)
