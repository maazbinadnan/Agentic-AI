from pathlib import Path
from langchain_core.tools import tool

__all__ = ["save_report_file", "save_html_mockup", "read_file"]


@tool
def save_report_file(filename: str, report_markdown: str, output_dir: str = "outputs") -> str:
    """Saves a formal Markdown report deliverable (e.g., '01_elicitation_report.md', '02_user_needs_report.md', '03_functional_requirements.md', '04_non_functional_requirements.md', '05_user_stories.md', '06_ui_mockups.md', 'INDEX.md') into output_dir.
    
    Parameters
    ----------
    filename : str
        Target report filename (e.g. '01_elicitation_report.md' or '06_ui_mockups.md').
    report_markdown : str
        The complete markdown text content of the report.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / filename
    file_path.write_text(report_markdown, encoding="utf-8")
    print(f"\n[single_agent_2] Successfully saved deliverable '{filename}' to '{file_path.resolve()}'")
    return f"Successfully saved '{filename}' to '{file_path.resolve()}'"


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
    print(f"\n[single_agent_2] Successfully saved HTML mockup to '{file_path.resolve()}'")
    return f"Successfully saved HTML mockup '{filename}' to '{file_path.resolve()}'"


@tool
def read_file(filename: str, output_dir: str = "outputs") -> str:
    """Reads a previously generated report file from output_dir.
    
    Parameters
    ----------
    filename : str
        Name of the file to read (e.g. '05_user_stories.md').
    output_dir : str
        Target output directory path.
    """
    file_path = Path(output_dir) / filename
    if not file_path.exists():
        if Path(filename).exists():
            return Path(filename).read_text(encoding="utf-8")
        return f"File '{filename}' not found in directory '{output_dir}'."
    return file_path.read_text(encoding="utf-8")
