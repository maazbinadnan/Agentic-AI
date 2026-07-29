from langchain.agents import create_agent
from langchain_core.tools import tool
from pathlib import Path
from hitl_agent._common_ import llm,load_prompt

__all__ = ["elicitation_subagent"]


@tool
def ask_stakeholder(question_text: str, context_reason: str = "") -> str:
    """Asks ONE single, individual clarifying question to the human stakeholder in the CLI console.
    CRITICAL: Never combine multiple questions into a single call. Call this tool once for each individual question.
    
    Parameters
    ----------
    question_text : str
        The single, specific question posed to the stakeholder (e.g. 'What is the maximum offline download limit?').
    context_reason : str
        Brief explanation of why this specific detail is ambiguous or missing in the requirements.
    """
    print("\n=======================================================")
    print("[?] ELICITATION AGENT CLARIFICATION TOOL CALL")
    print(f"Question: {question_text}")
    if context_reason:
        print(f"Context / Rationale: {context_reason}")
    print("=======================================================")

    answer = input("Stakeholder Answer (or press Enter for default): ").strip()
    ans_text = answer or "No specific preference provided; use standard domain defaults."
    
    print(f"-> Recorded Stakeholder Response: '{ans_text}'\n")
    return f"Stakeholder Answer to '{question_text}': {ans_text}"


@tool
def save_elicitation_report(report_markdown: str, output_dir: str = "outputs") -> str:
    """Saves the final Elicitation Markdown report containing original requirements, Q&A answers, and finalized user needs.
    
    Parameters
    ----------
    report_markdown : str
        The complete markdown text report to save into the workspace.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / "01_elicitation_report.md"
    file_path.write_text(report_markdown, encoding="utf-8")
    print(f"\n[elicitation agent] Successfully saved final report to '{file_path.resolve()}'")
    return f"Successfully saved 01_elicitation_report.md to '{file_path.resolve()}'"

from hitl_agent._common_ import llm, load_prompt, read_file

# 1. Compile the sub-agent graph using create_agent
elicitation_subagent = create_agent(
    model=llm,
    tools=[ask_stakeholder, save_elicitation_report, read_file],
    system_prompt=load_prompt("questioner.md"),
    name="elicitation_specialist",
)
