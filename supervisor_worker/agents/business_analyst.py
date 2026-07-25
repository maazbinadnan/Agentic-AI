import os
from supervisor_worker._common_ import llm, load_prompt
from supervisor_worker.local_states._state_ import AgentState
from global_layer.state import RequirementsPipelineOutput
from global_layer.functions import _save__requirement_files

from langchain.messages import SystemMessage, HumanMessage, AIMessage
from typing import cast
import json

__all__ = ["generate"]

def generate(state: AgentState):
    iteration = state.get("iteration_count", 0)
    iter_dir = os.path.join(state["output_dir"], str(iteration))

    system_prompt = load_prompt("business_analyst.md")
    input_val = state.get("input")
    assert input_val is not None

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Requirements Data:\n{input_val}"),
    ]

    # Append supervisor feedback if this is a revision iteration
    feedback = state.get("supervisor_feedback")
    prev_output = state.get("ba_output")
    if feedback and prev_output:
        messages.append(
            HumanMessage(
                content=(
                    f"Your Previous Output:\n{json.dumps(prev_output, indent=2)}\n\n"
                    f"Supervisor Feedback to apply:\n{feedback}"
                )
            )
        )

    print(f"Generating Business Analyst Output (Iteration {iteration})...")

    structured_llm = llm.with_structured_output(RequirementsPipelineOutput)
    response = cast(RequirementsPipelineOutput, structured_llm.invoke(messages))

    # Save output to iteration folder (e.g., test_run_1/0)
    _save__requirement_files(response, output_dir=iter_dir)

    return {
        "ba_output": response.model_dump(),
        "messages": [
            AIMessage(
                content=(
                    f"[Iteration {iteration}] Generated requirements specification:\n"
                    f"- {len(response.user_needs)} User Needs\n"
                    f"- {len(response.functional_requirements)} Functional Requirements\n"
                    f"- {len(response.non_functional_requirements)} Non-Functional Requirements\n"
                    f"- {len(response.user_stories)} User Stories"
                )
            )
        ],
    }