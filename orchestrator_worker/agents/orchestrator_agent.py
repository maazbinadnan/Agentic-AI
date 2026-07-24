"""Coordinator Agent — routes work to the right team.

Inspects the conversation history and decides the next step in the pipeline.
"""

from orchestrator_worker.state.states import GlobalState, CoordinatorDecision
from langchain_core.messages import SystemMessage, AIMessage
from orchestrator_worker.agents._common import llm, load_prompt
from pydantic import ValidationError


def coordinator_node(state: GlobalState) -> dict:
    """Coordinator — analyse the conversation and decide the next step."""
    system_prompt = load_prompt("coordinator.md")

    messages = [
        SystemMessage(content=system_prompt),
        state["messages"][-1], #type:ignore
    ]

    full_response = ""
    for chunk in llm.stream(messages):
        if chunk.content:
            # Stream to the UI if desired
            print(chunk.content, end="", flush=True)

            # Accumulate the text
            full_response += chunk.content #type: ignore

    print()

    # Parse into your Pydantic model
    try:
        decision = CoordinatorDecision.model_validate_json(full_response)
    except ValidationError as e:
        raise RuntimeError(f"Failed to parse coordinator output:\n{e}")

    print(
        f"\n🎯 Coordinator decision: "
        f"{decision.next_agent} — {decision.justification}\n"
    )

    return {
        "messages": [
            AIMessage(content=full_response)
        ],
        "next_agent": decision.next_agent,
        "current_phase": decision.next_agent,
    }
