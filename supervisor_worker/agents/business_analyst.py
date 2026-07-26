import os
import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage, AIMessage

from supervisor_worker._common_ import llm, load_prompt
from supervisor_worker.local_states._state_ import AgentState
from global_layer.ba_state import RequirementsPipelineOutput
from global_layer.functions import _save__requirement_files

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

    # Include previous output and cumulative feedback history if revising
    feedback_history = state.get("feedback_history", [])
    ba_reviews = [log for log in feedback_history if log.get("phase") == "ba"]
    prev_output = state.get("ba_output")

    if ba_reviews and prev_output:
        feedback_summary = "\n---\n".join(
            f"Review Iteration {idx}:\nFeedback: {rev.get('feedback')}\nIssues: {rev.get('issues')}"
            for idx, rev in enumerate(ba_reviews)
        )
        messages.append(
            HumanMessage(
                content=(
                    f"Your Previous Output:\n{json.dumps(prev_output, indent=2)}\n\n"
                    f"Supervisor Feedback History to apply:\n{feedback_summary}"
                )
            )
        )

    print(f"[Supervisor Worker] Generating Business Analyst Output (Iteration {iteration})...")

    structured_llm = llm.with_structured_output(RequirementsPipelineOutput, include_raw=True)
    response = structured_llm.invoke(messages)

    if isinstance(response, dict):
        result = response["parsed"]
        raw_msg = response["raw"]
        usage = getattr(raw_msg, "usage_metadata", {}) or {}
        in_tokens = usage.get("input_tokens", 0)
        out_tokens = usage.get("output_tokens", 0)
        tot_tokens = usage.get("total_tokens", in_tokens + out_tokens)
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