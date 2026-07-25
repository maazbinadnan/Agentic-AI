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
    iter_dir = os.path.join(state["output_dir"], str(iteration))
    ba_output = state.get("ba_output")
    
    system_prompt = load_prompt("coordinator.md") # Rubric prompt
    human_msg = f"User Requirement:\n{state['input']}\n\nBA Output:\n{json.dumps(ba_output)}"
    
    structured_llm = llm.with_structured_output(SupervisorReview)

    review = cast(SupervisorReview, structured_llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_msg)
    ]))

    _save_supervisor_review(review, output_dir=iter_dir)

    return {
        "verdict": review.verdict,
        "supervisor_feedback": "\n".join(review.actionable_feedback),
        "iteration_count": iteration + 1
    }

def _save_supervisor_review(review, output_dir: str = "output", filename: str = "supervisor_review.md") -> str:
    """Saves the Supervisor's review/feedback into a formatted Markdown file.
    
    Parameters
    ----------
    review : Pydantic BaseModel, dict, or str
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

        if "quality_score" in data or "completeness_score" in data:
            score = data.get("quality_score") or data.get("completeness_score")
            lines.append(f"- **Quality Score:** {score}/10")

        if "traceability_passed" in data:
            lines.append(f"- **Traceability Passed:** {data['traceability_passed']}")

        lines.append("\n---\n")

        feedback = data.get("actionable_feedback") or data.get("feedback_summary") or data.get("feedback")
        if isinstance(feedback, list):
            lines.append("## Actionable Feedback Points:\n")
            for item in feedback:
                lines.append(f"- {item}")
        elif isinstance(feedback, str):
            lines.append("## Feedback Summary:\n")
            lines.append(feedback)
    else:
        lines.append(str(review))

    file_path.write_text("\n".join(lines), encoding="utf-8")
    print(f" Successfully saved supervisor review to '{file_path.resolve()}'")
    return str(file_path)