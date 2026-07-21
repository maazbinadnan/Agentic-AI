"""Developer Review — Three Amigos Developer / Architect perspective.

Reviews user stories from a technical feasibility, architecture, and
implementation viewpoint.
"""

from three_amigos.States.state import ThreeAmigosState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from three_amigos.agents._common import _stream_llm, _save_output, load_prompt
from three_amigos.agents._discussion import _build_discussion_context


def developer_review(state: ThreeAmigosState) -> dict:
    """Three Amigos — Developer / Architect perspective."""
    system_prompt = load_prompt("developer.md")
    round_num = state.get("discussion_round", 0) + 1
    context = _build_discussion_context(state, include_po=True)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response_text = _stream_llm(messages, agent_label=f"DEVELOPER (Round {round_num})")
    _save_output(state, f"dev_review_round_{round_num}", response_text,
                 title=f"Developer Review — Round {round_num}")
    print(f"👩‍💻  Developer review complete (round {round_num}).")

    return {
        "messages": [
            AIMessage(
                content=f"[DEVELOPER — Round {round_num}]\n{response_text}"
            )
        ],
        "dev_feedback": response_text,
    }
