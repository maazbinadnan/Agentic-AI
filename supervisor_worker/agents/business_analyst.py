import os
import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage, AIMessage

from supervisor_worker._common_ import llm, load_prompt
from supervisor_worker.local_states._state_ import AgentState
from global_layer.ba_state import RequirementsPipelineOutput
from global_layer.functions import _save__requirement_files,token_counter

__all__ = ["generate"]


def generate(state: AgentState):
    iterations = state.get("iterations", {})
    iteration = iterations.get("ba", 0)

    # Phase-scoped iteration folder (e.g. outputs/run_1/01_business_analysis/iter_0)
    phase_dir = Path(state["output_dir"]) / "01_business_analysis" / f"iter_{iteration}"

    system_prompt = load_prompt("business_analyst.md")
    input_val = state.get("input")
    assert input_val is not None

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Requirements Data:\n{input_val}"),
    ]

    # Targeted Feedback Context Trimming & Surgical Item Revision
    feedback_history = state.get("feedback_history", [])
    ba_reviews = [log for log in feedback_history if log.get("phase") == "ba"]
    prev_output = state.get("ba_output")

    if ba_reviews and prev_output:
        latest_review = ba_reviews[-1]
        issues_list = latest_review.get("issues", [])
        issues_text = "\n".join(f"- {issue}" for issue in issues_list) if issues_list else "None"
        feedback_text = latest_review.get("feedback", "")

        messages.append(
            HumanMessage(
                content=(
                    f"### PREVIOUS GENERATED OUTPUT:\n{json.dumps(prev_output, indent=2)}\n\n"
                    f"### SUPERVISOR AUDIT FEEDBACK (LATEST ITERATION):\n"
                    f"Verdict: {latest_review.get('verdict')}\n"
                    f"Score: {latest_review.get('score')}/5\n"
                    f"Feedback: {feedback_text}\n"
                    f"Flagged Issues:\n{issues_text}\n\n"
                    f"### SURGICAL REVISION INSTRUCTIONS:\n"
                    f"1. Perform IN-PLACE PATCHING: Preserve all valid, approved User Needs, Functional Requirements, Non-Functional Requirements, and User Stories from your Previous Output.\n"
                    f"2. Fix and update ONLY the specific items, IDs, or missing criteria cited in the Flagged Issues above.\n"
                    f"3. Do NOT delete or modify unflagged approved items."
                )
            )
        )

    print(f"[Business Analyst Worker] Generating Business Analyst Output (Iteration {iteration})...")

    structured_llm = llm.with_structured_output(RequirementsPipelineOutput, include_raw=True)
    response = structured_llm.invoke(messages)

    if isinstance(response, dict):
        result = response["parsed"]
        in_tokens,out_tokens,tot_tokens = token_counter(response,"business analyst")
        print(f"[BA Usage Iter {iteration}] Input: {in_tokens}, Output: {out_tokens}, Total: {tot_tokens}")
    else:
        result = cast(RequirementsPipelineOutput, response)
        in_tokens, out_tokens, tot_tokens = 0, 0, 0

    # Save output to phase iteration folder
    _save__requirement_files(result, output_dir=str(phase_dir))

    return {
        "ba_output": result.model_dump(),
        "input_tokens": in_tokens,
        "output_tokens": out_tokens,
        "total_tokens": tot_tokens,
        "messages": [
            AIMessage(
                content=(
                    f"[Iteration {iteration}] Generated requirements specification:\n"
                    f"- {len(result.user_needs)} User Needs\n"
                    f"- {len(result.functional_requirements)} Functional Requirements\n"
                    f"- {len(result.non_functional_requirements)} Non-Functional Requirements\n"
                    f"- {len(result.user_stories)} User Stories\n"
                    f"[Tokens: {in_tokens} in / {out_tokens} out]"
                )
            )
        ],
    }