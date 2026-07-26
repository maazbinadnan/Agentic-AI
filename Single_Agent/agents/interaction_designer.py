import os
import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage, AIMessage

from single_agent_final._common_ import llm, load_prompt
from single_agent_final.local_states._state_ import AgentState
from global_layer.ixd_state import IxdPipelineOutput
from global_layer.functions import _save_ixd_files


def generate(state: AgentState):
    phase_dir = Path(state["output_dir"]) / "02_interaction_design"

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

    print("[Single Agent Final] Generating Interaction Designer Mockups...")

    structured_llm = llm.with_structured_output(IxdPipelineOutput)
    response = cast(IxdPipelineOutput, structured_llm.invoke(messages))

    # Save output files using global layer function
    _save_ixd_files(response, output_dir=str(phase_dir))

    return {
        "ixd_output": response.model_dump(),
        "phase": "completed",
        "messages": [
            AIMessage(
                content=(
                    "[Interaction Designer] Generated IxD Specifications & Mockups:\n"
                    f"- {len(response.mockup_files.files)} HTML Mockup Files\n"
                    f"- {len(response.mapping_table.mapping_table)} User Story Mappings\n"
                    f"- {len(response.tradeoffs.table)} UI/UX Trade-off Decisions"
                )
            )
        ],
    }
