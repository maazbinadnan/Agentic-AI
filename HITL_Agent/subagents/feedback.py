from pathlib import Path
from langchain.agents import create_agent
from langchain_core.tools import tool

from hitl_agent._common_ import llm, load_prompt, read_file

__all__ = [
    "feedback_subagent",
    "ask_stakeholder_feedback",
    "update_deliverable_file",
    "save_feedback_report",
]


@tool
def ask_stakeholder_feedback(prompt_text: str, context_summary: str = "") -> str:
    """Asks the human stakeholder in the CLI console for final review feedback or requested changes on the deliverables package.
    
    Parameters
    ----------
    prompt_text : str
        The question or prompt presented to the stakeholder (e.g. 'Do you have any feedback or requested changes on the deliverables package?').
    context_summary : str
        Brief summary of the completed deliverables being reviewed.
    """
    print("\n=======================================================")
    print("[?] FEEDBACK AGENT STAKEHOLDER REVIEW TOOL CALL")
    print(f"Prompt: {prompt_text}")
    if context_summary:
        print(f"Deliverables Context: {context_summary}")
    print("=======================================================")

    answer = input("Stakeholder Feedback / Changes (or press Enter if approved as-is): ").strip()
    ans_text = answer or "No changes requested; deliverables package approved as presented."
    
    print(f"-> Recorded Stakeholder Response: '{ans_text}'\n")
    return f"Stakeholder Feedback Response: {ans_text}"


@tool
def update_deliverable_file(filename: str, updated_content: str, output_dir: str = "outputs") -> str:
    """Updates an existing deliverable report or HTML mockup file with revised content based on stakeholder feedback.
    
    Parameters
    ----------
    filename : str
        Name of the file to update (e.g. '03_functional_requirements.md', '05_user_stories.md', 'html/dashboard.html').
    updated_content : str
        Complete revised text/markdown/HTML content for the file.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir)
    file_path = out_path / filename
    
    # Ensure parent directories exist (e.g. for html/ subfolder)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(updated_content, encoding="utf-8")
    
    print(f"\n[feedback agent] Successfully updated deliverable file '{file_path.resolve()}'")
    return f"Successfully updated '{filename}' in '{out_path.resolve()}'"


@tool
def save_feedback_report(report_markdown: str, output_dir: str = "outputs") -> str:
    """Saves the formal Feedback & Revision Markdown report (08_feedback_report.md) containing stakeholder feedback log and revision status.
    
    Parameters
    ----------
    report_markdown : str
        The complete markdown text report to save into the workspace.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / "08_feedback_report.md"
    file_path.write_text(report_markdown, encoding="utf-8")
    print(f"\n[feedback agent] Successfully saved feedback report to '{file_path.resolve()}'")
    return f"Successfully saved 08_feedback_report.md to '{file_path.resolve()}'"


feedback_subagent = create_agent(
    model=llm,
    tools=[ask_stakeholder_feedback, update_deliverable_file, save_feedback_report, read_file],
    system_prompt=load_prompt("feedback.md"),
    name="feedback_specialist",
)
