from pathlib import Path
from langchain.agents import create_agent
from langchain_core.tools import tool

from hitl_agent._common_ import llm, load_prompt, read_file

__all__ = ["design_elicitation_subagent"]


@tool
def save_design_elicitation_report(report_markdown: str, output_dir: str = "outputs") -> str:
    """Saves the formal Initial Design Requirement Markdown report containing visual and UI preferences.
    
    Parameters
    ----------
    report_markdown : str
        The complete markdown text report to save into the workspace.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / "06_design_requirements.md"
    file_path.write_text(report_markdown, encoding="utf-8")
    print(f"\n[design requirement agent] Successfully saved design requirements report to '{file_path.resolve()}'")
    return f"Successfully saved 06_design_requirements.md to '{file_path.resolve()}'"


@tool
def ask_stakeholder(question_text: str, context_reason: str = "") -> str:
    """Asks ONE single, individual clarifying question about design/UI preferences to the human stakeholder in the CLI console.
    CRITICAL: Never combine multiple questions into a single call. Call this tool once for each individual question.
    
    Parameters
    ----------
    question_text : str
        The single, specific question posed to the stakeholder (e.g. 'What is your preferred color theme (dark/light) and primary brand color?').
    context_reason : str
        Brief explanation of why this specific detail is needed for the design requirements.
    """
    print("\n=======================================================")
    print("[?] DESIGN ELICITATION AGENT CLARIFICATION TOOL CALL")
    print(f"Question: {question_text}")
    if context_reason:
        print(f"Context / Rationale: {context_reason}")
    print("=======================================================")

    answer = input("Stakeholder Answer (or press Enter for default): ").strip()
    ans_text = answer or "No specific preference provided; use standard modern UI defaults."
    
    print(f"-> Recorded Stakeholder Response: '{ans_text}'\n")
    return f"Stakeholder Answer to '{question_text}': {ans_text}"

llm_with_tools = llm.bind_tools(tools=[ask_stakeholder, save_design_elicitation_report, read_file],tool_choice="any")
# Compile the sub-agent graph using create_agent
design_elicitation_subagent = create_agent(
    model=llm,
    tools=[ask_stakeholder, save_design_elicitation_report, read_file],
    system_prompt=load_prompt("design_elicitation.md"),
    name="design_elicitation_specialist"
)
