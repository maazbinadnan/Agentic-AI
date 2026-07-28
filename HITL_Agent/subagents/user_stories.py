from pathlib import Path
from langchain.agents import create_agent
from langchain_core.tools import tool

from ba_team_agent._common_ import llm, load_prompt, read_file

__all__ = ["user_stories_subagent", "save_user_stories_report"]


@tool
def save_user_stories_report(report_markdown: str, output_dir: str = "outputs") -> str:
    """Saves the formal Agile User Stories Markdown report containing US-xxx specifications and AC-xxx Gherkin criteria.
    
    Parameters
    ----------
    report_markdown : str
        The complete markdown text report to save into the workspace.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / "05_user_stories.md"
    file_path.write_text(report_markdown, encoding="utf-8")
    print(f"\n[ba_team_agent] Successfully saved User Stories report to '{file_path.resolve()}'")
    return f"Successfully saved 05_user_stories.md to '{file_path.resolve()}'"


user_stories_subagent = create_agent(
    model=llm,
    tools=[save_user_stories_report, read_file],
    system_prompt=load_prompt("user_stories.md"),
    name="user_story_writer",
)
