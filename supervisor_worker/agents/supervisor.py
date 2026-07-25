import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage

from supervisor_worker._common_ import llm, load_prompt
from supervisor_worker.local_states._state_ import AgentState
from supervisor_worker.local_states.supervisor_state import SupervisorReview
from global_layer.functions import _save_supervisor_review

__all__ = ["generate"]

# Registry mapping for evaluated phases
EVAL_CONFIG = {
    "ba": {
        "prompt": "coordinator_ba.md",
        "subfolder": "01_business_analysis",
        "get_message": lambda state: f"User Requirement:\n{state.get('input')}\n\nBA Output:\n{json.dumps(state.get('ba_output'), indent=2)}",
    },
    "ixd": {
        "prompt": "coordinator_ixd.md",
        "subfolder": "02_interaction_design",
        "get_message": lambda state: (
            f"User Stories:\n{json.dumps((state.get('ba_output') or {}).get('user_stories', []), indent=2)}\n\n"
            f"IXD Output:\n{json.dumps(state.get('ixd_output'), indent=2)}"
        ),
    },
}


def generate(state: AgentState):
    phase = state.get("phase", "ba")
    if phase not in EVAL_CONFIG:
        phase = "ba"

    config = EVAL_CONFIG[phase]
    iterations = dict(state.get("iterations", {"ba": 0, "ixd": 0}))
    current_iter = iterations.get(phase, 0)

    # Output directory for supervisor review file
    iter_dir = Path(state["output_dir"]) / config["subfolder"] / f"iter_{current_iter}"

    system_prompt = load_prompt(config["prompt"])
    human_msg = config["get_message"](state)

    structured_llm = llm.with_structured_output(SupervisorReview)
    review = cast(
        SupervisorReview,
        structured_llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_msg)
        ])
    )

    # Save formatted review using shared global function
    _save_supervisor_review(review, output_dir=str(iter_dir))

    # Format feedback text
    issues_formatted = "\n".join(f"- {issue}" for issue in review.issues)
    combined_feedback = f"{review.feedback}\n\nIssues Identified:\n{issues_formatted}" if review.issues else review.feedback

    # Construct feedback history entry
    new_log = {
        "phase": phase,
        "iteration": current_iter,
        "verdict": review.verdict,
        "score": review.score,
        "issues": review.issues,
        "feedback": review.feedback,
    }

    # Increment per-phase iteration counter
    iterations[phase] = current_iter + 1

    return {
        "verdict": review.verdict,
        "supervisor_feedback": combined_feedback,
        "feedback_history": [new_log],
        "phase": review.phase,
        "iterations": iterations,
    }