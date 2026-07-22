"""Coordinator Agent — routes work to the right team.

Inspects the conversation history and decides the next step in the pipeline.
"""

from orchestrator_worker.state.states import CoordinatorState, CoordinatorDecision
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from orchestrator_worker.agents._common import llm, _stream_llm, _save_output, load_prompt


def coordinator_node(state: CoordinatorState) -> dict:
    """Coordinator — analyse the conversation and decide the next step."""
    system_prompt = load_prompt("coordinator.md")

    messages = [
        SystemMessage(content=system_prompt),
        *state["messages"],
    ]

    # Use structured output for the routing decision
    structured_llm = llm.with_structured_output(CoordinatorDecision)
    decision: CoordinatorDecision = structured_llm.invoke(messages)

    print(f"\n🎯  Coordinator decision: {decision.next_agent} — {decision.justification}\n")

    return {
        "messages": [
            AIMessage(content=f"[COORDINATOR] Routing to **{decision.next_agent}**. Reason: {decision.justification}")
        ],
        "next_agent": decision.next_agent,
        "current_phase": decision.next_agent,
    }
