from pathlib import Path
from langchain.agents import create_agent
from langchain_core.tools import tool

from hitl_agent._common_ import llm, load_prompt, read_file

__all__ = ["ixd_subagent", "save_ui_mockups_report", "save_html_mockup"]


@tool
def save_html_mockup(filename: str, html_content: str, output_dir: str = "outputs") -> str:
    """Saves an individual HTML mockup file (e.g., 'login.html', 'dashboard.html') into the 'html/' subfolder of output_dir.
    
    Parameters
    ----------
    filename : str
        Name of the HTML file (e.g. 'login.html').
    html_content : str
        Complete valid HTML code string for the mockup.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir) / "html"
    out_path.mkdir(parents=True, exist_ok=True)
    if not filename.endswith(".html"):
        filename += ".html"
    file_path = out_path / filename
    file_path.write_text(html_content, encoding="utf-8")
    print(f"\n[interaction designer agent] Successfully saved HTML mockup to '{file_path.resolve()}'")
    return f"Successfully saved HTML mockup '{filename}' to '{file_path.resolve()}'"


@tool
def save_ui_mockups_report(report_markdown: str, output_dir: str = "outputs") -> str:
    """Saves the formal UI Mockups and Interaction Design Markdown report containing UI screen wireframes, layouts, and story mappings.
    
    Parameters
    ----------
    report_markdown : str
        The complete markdown text report to save into the workspace.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / "07_ui_mockups.md"
    file_path.write_text(report_markdown, encoding="utf-8")
    print(f"\n[interaction designer agent] Successfully saved UI Mockups report to '{file_path.resolve()}'")
    return f"Successfully saved 08_ui_mockups.md to '{file_path.resolve()}'"


ixd_subagent = create_agent(
    model=llm,
    tools=[save_html_mockup, save_ui_mockups_report, read_file],
    system_prompt=load_prompt("interaction_designer.md"),
    name="interaction_designer",
)
