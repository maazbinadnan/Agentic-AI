"""Interaction Designers Agent — designs HTML mockups from user stories.

Takes the formalised user stories and produces wireframe-level HTML
mockups covering the key screens and interactions.
"""

from orchestrator_worker.state.states import GlobalState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from orchestrator_worker.agents._common import _stream_llm, _save_output, load_prompt


def interaction_designers_node(state: GlobalState) -> dict:
    """IxD Team — design HTML mockups from the formalised user stories."""
    system_prompt = load_prompt("ixd_team.md")
    user_stories = state.get("user_stories", "")

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(
            content=(
                "Design HTML mockups based on the following user stories "
                "and acceptance criteria:\n\n"
                f"{user_stories}"
            )
        ),
    ]

    response_text = _stream_llm(messages, agent_label="INTERACTION DESIGNERS")
    _save_output(state, "html_mockups", response_text, title="HTML Mockups")
    print("✅  Interaction Designers complete.")

    return {
        "messages": [
            AIMessage(content=f"[INTERACTION DESIGNERS]\n{response_text}")
        ],
        "html_mockups": response_text,
        "current_phase": "ixd_complete",
    }
