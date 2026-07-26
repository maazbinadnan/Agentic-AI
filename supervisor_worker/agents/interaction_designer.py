import os
import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage, AIMessage

from supervisor_worker._common_ import llm, load_prompt
from supervisor_worker.local_states._state_ import AgentState
from global_layer.ixd_state import IxdPipelineOutput
from global_layer.functions import _save_ixd_files,token_counter


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

    # Targeted Feedback Context Trimming & Surgical Item Revision
    feedback_history = state.get("feedback_history", [])
    ixd_reviews = [log for log in feedback_history if log.get("phase") == "ixd"]
    prev_output = state.get("ixd_output")

    if ixd_reviews and prev_output:
        latest_review = ixd_reviews[-1]
        issues_list = latest_review.get("issues", [])
        issues_text = "\n".join(f"- {issue}" for issue in issues_list) if issues_list else "None"
        feedback_text = latest_review.get("feedback", "")

        messages.append(
            HumanMessage(
                content=(
                    f"### PREVIOUS GENERATED IXD OUTPUT:\n{json.dumps(prev_output, indent=2)}\n\n"
                    f"### SUPERVISOR AUDIT FEEDBACK (LATEST ITERATION):\n"
                    f"Verdict: {latest_review.get('verdict')}\n"
                    f"Score: {latest_review.get('score')}/5\n"
                    f"Feedback: {feedback_text}\n"
                    f"Flagged Issues:\n{issues_text}\n\n"
                    f"### SURGICAL REVISION INSTRUCTIONS:\n"
                    f"1. Perform IN-PLACE PATCHING: Retain all valid, approved HTML mockup files, story mapping entries, and tradeoff decisions from your Previous Output.\n"
                    f"2. Modify, add, or repair ONLY the specific HTML mockup files or mapping rows cited in the Flagged Issues above.\n"
                    f"3. Do NOT discard or re-generate unflagged approved mockup screens."
                )
            )
        )

    print(f"[Interaction Designer Worker] Generating Interaction Designer Output (Iteration {iteration})...")

    structured_llm = llm.with_structured_output(IxdPipelineOutput, include_raw=True)
    response = structured_llm.invoke(messages)

    if isinstance(response, dict):
        result = response["parsed"]
        in_tokens,out_tokens,tot_tokens = token_counter(response,"Interaction Designer")
        print(f"[IxD Usage Iter {iteration}] Input: {in_tokens}, Output: {out_tokens}, Total: {tot_tokens}")
    else:
        result = cast(IxdPipelineOutput, response)
        in_tokens, out_tokens, tot_tokens = 0, 0, 0

    # Save output to phase iteration folder
    _save_ixd_files(result, output_dir=str(phase_dir))
    
    return {
        "ixd_output": result.model_dump(),
        "input_tokens": in_tokens,
        "output_tokens": out_tokens,
        "total_tokens": tot_tokens,
        "messages": [
            AIMessage(
                content=(
                    f"[Iteration {iteration}] Generated IxD Specifications & Mockups:\n"
                    f"- {len(result.mockup_files.files)} HTML Mockup Files\n"
                    f"- {len(result.mapping_table.mapping_table)} User Story Mappings\n"
                    f"- {len(result.tradeoffs.table)} UI/UX Trade-off Decisions\n"
                    f"[Tokens: {in_tokens} in / {out_tokens} out]"
                )
            )
        ],
    }