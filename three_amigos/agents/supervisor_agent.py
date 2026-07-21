"""Supervisor Agent — Phase 1 orchestrator.

Analyses user research and sets the work plan for downstream agents.
"""

from three_amigos.States.state import ThreeAmigosState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from three_amigos.agents._common import _stream_llm, _save_output, load_prompt


def supervisor_agent(state: ThreeAmigosState) -> dict:
    """Phase 1 — Orchestrator: analyse user research, set the work plan."""
    system_prompt = load_prompt("supervisor.md")
    user_research = state["user_research"]

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(
            content=(
                "Analyse the following user research and provide your "
                "assessment:\n\n"
                f"{user_research}"
            )
        ),
    ]

    response_text = _stream_llm(messages, agent_label="SUPERVISOR")
    _save_output(state, "supervisor_analysis", response_text, title="Supervisor Analysis")
    print("✅  Supervisor analysis complete.")

    return {
        "messages": [
            AIMessage(content=f"[SUPERVISOR ANALYSIS]\n{response_text}")
        ],
        "current_phase": "elicitation",
    }
