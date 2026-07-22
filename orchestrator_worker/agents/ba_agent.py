"""BA Team Agent — formalises raw user research into user stories.

Produces structured User Stories with Given-When-Then BDD acceptance
criteria from the raw research input.
"""

from orchestrator_worker.state.states import GlobalState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from orchestrator_worker.agents._common import _stream_llm, _save_output, load_prompt


def ba_team_node(state: GlobalState) -> dict:
    """BA Team — formalise raw research into user stories and acceptance criteria."""
    system_prompt = load_prompt("ba_team.md")
    user_research = state["user_research"]

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(
            content=(
                "Formalise the following user research into user stories "
                "with BDD acceptance criteria:\n\n"
                f"{user_research}"
            )
        ),
    ]

    response_text = _stream_llm(messages, agent_label="BA TEAM")
    _save_output(state, "user_stories", response_text, title="User Stories & Acceptance Criteria")
    print("✅  BA Team analysis complete.")

    return {
        "messages": [
            AIMessage(content=f"[BA TEAM]\n{response_text}")
        ],
        "user_stories": response_text,
        "current_phase": "ba_complete",
    }
