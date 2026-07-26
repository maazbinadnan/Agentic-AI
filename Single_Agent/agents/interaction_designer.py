import os
import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage, AIMessage

from single_agent._common_ import llm, load_prompt
from single_agent.local_states._state_ import AgentState
from global_layer.ixd_state import IxdPipelineOutput
from global_layer.functions import _save_ixd_files, token_counter


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

    print("[Single Agent] Generating Interaction Designer Mockups...")

    structured_llm = llm.with_structured_output(IxdPipelineOutput, include_raw=True)
    response = structured_llm.invoke(messages)

    #calculate token costs
    if isinstance(response, dict):
        result = response["parsed"]
        in_tokens,out_tokens,tot_tokens = token_counter(response,"Interaction designer")
    else:
        result = cast(IxdPipelineOutput, response)
        in_tokens, out_tokens, tot_tokens = 0, 0, 0

    # Save output files using global layer function
    _save_ixd_files(result, output_dir=str(phase_dir))

    return {
        "ixd_output": result.model_dump(),
        "input_tokens": in_tokens,
        "output_tokens": out_tokens,
        "total_tokens": tot_tokens,
        "messages": [
            AIMessage(
                content=(
                    "[Interaction Designer] Generated IxD Specifications & Mockups:\n"
                    f"- {len(result.mockup_files.files)} HTML Mockup Files\n"
                    f"- {len(result.mapping_table.mapping_table)} User Story Mappings\n"
                    f"- {len(result.tradeoffs.table)} UI/UX Trade-off Decisions\n"
                    f"[Tokens: {in_tokens} in / {out_tokens} out]"
                )
            )
        ],
    }
