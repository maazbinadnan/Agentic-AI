import os
import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage, AIMessage

from single_agent._common_ import llm, load_prompt
from single_agent.local_states._state_ import AgentState
from global_layer.ba_state import RequirementsPipelineOutput
from global_layer.functions import _save__requirement_files,token_counter

__all__ = ["generate"]


def generate(state: AgentState):
    phase_dir = Path(state["output_dir"]) / "01_business_analysis"

    system_prompt = load_prompt("business_analyst.md")
    input_val = state.get("input")
    assert input_val is not None

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Requirements Data:\n{input_val}"),
    ]

    print("[Single Agent] Generating Business Analyst Requirements...")

    structured_llm = llm.with_structured_output(RequirementsPipelineOutput, include_raw=True)
    response = structured_llm.invoke(messages)

    #calculate token costs
    if isinstance(response, dict):
        result = response["parsed"]
        in_tokens,out_tokens,tot_tokens = token_counter(response,"business analyst")
    else:
        raise ValueError("Expected response to be a dict containing raw and parsed outputs")
        
    # Save output files using global layer function
    _save__requirement_files(result, output_dir=str(phase_dir))

    return {
        "ba_output": result.model_dump(),
        "input_tokens": in_tokens,
        "output_tokens": out_tokens,
        "total_tokens": tot_tokens,
        "messages": [
            AIMessage(
                content=(
                    "[Business Analyst] Generated requirements specification:\n"
                    f"- {len(result.user_needs)} User Needs\n"
                    f"- {len(result.functional_requirements)} Functional Requirements\n"
                    f"- {len(result.non_functional_requirements)} Non-Functional Requirements\n"
                    f"- {len(result.user_stories)} User Stories\n"
                    f"[Tokens: {in_tokens} in / {out_tokens} out]"
                )
            )
        ],
    }
