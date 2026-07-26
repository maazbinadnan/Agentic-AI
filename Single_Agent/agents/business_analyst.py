import os
import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage, AIMessage

from single_agent_final._common_ import llm, load_prompt
from single_agent_final.local_states._state_ import AgentState
from global_layer.ba_state import RequirementsPipelineOutput
from global_layer.functions import _save__requirement_files

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

    print("[Single Agent Final] Generating Business Analyst Requirements...")

    structured_llm = llm.with_structured_output(RequirementsPipelineOutput)
    response = cast(RequirementsPipelineOutput, structured_llm.invoke(messages))

    # Save output files using global layer function
    _save__requirement_files(response, output_dir=str(phase_dir))

    return {
        "ba_output": response.model_dump(),
        "phase": "ixd",
        "messages": [
            AIMessage(
                content=(
                    "[Business Analyst] Generated requirements specification:\n"
                    f"- {len(response.user_needs)} User Needs\n"
                    f"- {len(response.functional_requirements)} Functional Requirements\n"
                    f"- {len(response.non_functional_requirements)} Non-Functional Requirements\n"
                    f"- {len(response.user_stories)} User Stories"
                )
            )
        ],
    }
