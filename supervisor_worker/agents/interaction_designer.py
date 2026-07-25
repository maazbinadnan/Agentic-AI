import os
from supervisor_worker._common_ import llm, load_prompt
from supervisor_worker.local_states._state_ import AgentState
from global_layer.ixd_state import IxdPipelineOutput
from global_layer.functions import _save_ixd_files

from langchain.messages import SystemMessage, HumanMessage, AIMessage
from typing import cast
import json


def generate(state: AgentState):
    iteration = state.get("iteration_count", 0)
    iter_dir = os.path.join(state["output_dir"], str(iteration))

    #load system prompt
    system_prompt = load_prompt("ixd_team.md")
    #get the user stories
    ba_output = state.get("ba_output")

    if ba_output:
    # Safely get the list of user stories (defaults to [] if missing)
        user_stories = ba_output.get("user_stories", [])
    else:
        return{
            "messages":[(HumanMessage(content = " no user stories to analyze"))]
        }
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"User Stories Data:\n{user_stories}"),
    ]

    # Append supervisor feedback if this is a revision iteration
    feedback = state.get("supervisor_feedback")
    prev_output = state.get("ixd_output")
    if feedback and prev_output:
        messages.append(
            HumanMessage(
                content=(
                    f"Your Previous Output:\n{json.dumps(prev_output, indent=2)}\n\n"
                    f"Supervisor Feedback to apply:\n{feedback}"
                )
            )
        )

    print(f"Generating Interaction Designer Output (Iteration {iteration})...")

    structured_llm = llm.with_structured_output(IxdPipelineOutput)
    response = cast(IxdPipelineOutput, structured_llm.invoke(messages))

    # Save output to iteration folder (e.g., test_run_1/0)
    _save_ixd_files(response, output_dir=iter_dir)

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