from supervisor_worker._common_ import llm,load_prompt
from supervisor_worker.local_states._state_ import AgentState
from supervisor_worker.local_states.supervisor_state import SupervisorReview
from pathlib import Path

from langchain.messages import SystemMessage, HumanMessage
from typing import cast
import json

__all__ = ["generate"]

import os

def generate(state: AgentState):
    iteration = state.get("iteration_count", 0)
    phase = state.get("phase", "ba")
    iter_dir = os.path.join(state["output_dir"], str(iteration))
    
    #load system prompt based on the phase
    if phase == "ba":
        system_prompt = load_prompt("coordinator_ba.md")
        ba_output = state.get("ba_output")
        # Rubric prompt
        human_msg = f"User Requirement:\n{state['input']}\n\nBA Output:\n{json.dumps(ba_output)}"
    else:
        system_prompt = load_prompt("coordinator_ixd.md")
        ixd_output = state.get("ixd_output")
        # Rubric prompt
        ba_output = state.get("ba_output")
        # Safely get the list of user stories (defaults to [] if missing)
        assert ba_output is not None
        user_stories = ba_output.get("user_stories", [])
        human_msg = f"User Stories:\n{json.dumps(user_stories)}\n\nIXD Output:\n{json.dumps(ixd_output)}"

    structured_llm = llm.with_structured_output(SupervisorReview)

    review = cast(SupervisorReview, structured_llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_msg)
    ]))
    _save_supervisor_review(review, output_dir=iter_dir)

    #set iteration if phase changes from BA to IxD
    if review.phase != phase and review.phase != "END":
        iteration = 0 
    else:
        iteration = iteration + 1

    issues_formatted = "\n".join(f"- {issue}" for issue in review.issues)

    # Combine feedback text and formatted issues list
    if review.issues:
        combined_feedback = f"{review.feedback}\n\nIssues Identified:\n{issues_formatted}"
    else:
        combined_feedback = review.feedback

    return {
        "verdict": review.verdict,
        "supervisor_feedback": combined_feedback,
        "phase": review.phase,
        "iteration_count": iteration,
    }
def _save_supervisor_review(review, output_dir: str = "output", filename: str = "supervisor_review.md") -> str:
    """Saves the Supervisor's review/feedback into a formatted Markdown file.
    
    Parameters
    ----------
    review : SupervisorReview, dict, or str
        The output from the Supervisor node.
    output_dir : str
        Target output directory.
    filename : str
        Name of the file to save (default: "supervisor_review.md").
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / filename

    lines = ["# Supervisor Review & Feedback\n"]

    if hasattr(review, "model_dump") or hasattr(review, "dict"):
        data = review.model_dump() if hasattr(review, "model_dump") else review.dict()

        verdict = data.get("verdict", "N/A")
        lines.append(f"## Overall Verdict: **{verdict}**\n")

        score = data.get("score")
        if score is not None:
            lines.append(f"- **Quality Score:** {score}/5")

        lines.append("\n---\n")

        issues = data.get("issues")
        if issues:
            lines.append("## Issues Found:\n")
            for item in issues:
                lines.append(f"- {item}")
            lines.append("")

        feedback = data.get("feedback")
        if feedback:
            lines.append("## Feedback Summary:\n")
            lines.append(feedback)
    else:
        lines.append(str(review))

    file_path.write_text("\n".join(lines), encoding="utf-8")
    print(f" Successfully saved supervisor review to '{file_path.resolve()}'")
    return str(file_path)