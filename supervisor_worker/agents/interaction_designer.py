import os
import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage, AIMessage

from supervisor_worker._common_ import llm, load_prompt
from supervisor_worker.local_states._state_ import AgentState
from global_layer.ixd_state import IxdPipelineOutput
from global_layer.functions import _save_ixd_files


def generate(state: AgentState):
    iterations = state.get("iterations", {})
    iteration = iterations.get("ixd", 0)
    phase_dir = Path(state["output_dir"]) / "02_interaction_design" / f"iter_{iteration}"

    system_prompt = load_prompt("ixd_team.md")
    ba_output = state.get("ba_output")

    if ba_output:
        user_stories = ba_output.get("user_stories", [])
    else:
        return {
            "messages": [AIMessage(content="[Interaction Designer] Error: No user stories available to analyze.")]
        }

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"User Stories Data:\n{json.dumps(user_stories, indent=2)}"),
    ]

    # Include previous output and cumulative feedback history if revising
    feedback_history = state.get("feedback_history", [])
    ixd_reviews = [log for log in feedback_history if log.get("phase") == "ixd"]
    prev_output = state.get("ixd_output")

    if ixd_reviews and prev_output:
        feedback_summary = "\n---\n".join(
            f"Review Iteration {idx}:\nFeedback: {rev.get('feedback')}\nIssues: {rev.get('issues')}"
            for idx, rev in enumerate(ixd_reviews)
        )
        messages.append(
            HumanMessage(
                content=(
                    f"Your Previous Output:\n{json.dumps(prev_output, indent=2)}\n\n"
                    f"Supervisor Feedback History to apply:\n{feedback_summary}"
                )
            )
        )

    print(f"Generating Interaction Designer Output (Iteration {iteration})...")

    structured_llm = llm.with_structured_output(IxdPipelineOutput)
    response = cast(IxdPipelineOutput, structured_llm.invoke(messages))

    # Save output to phase iteration folder
    _save_ixd_files(response, output_dir=str(phase_dir))

    return {
        "ixd_output": response.model_dump(),
        "messages": [
            AIMessage(
                content=(
                    f"[Iteration {iteration}] Generated IxD Specifications & Mockups:\n"
                    f"- {len(response.mockup_files.files)} HTML Mockup Files\n"
                    f"- {len(response.mapping_table.mapping_table)} User Story Mappings\n"
                    f"- {len(response.tradeoffs.table)} UI/UX Trade-off Decisions"
                )
            )
        ],
    }