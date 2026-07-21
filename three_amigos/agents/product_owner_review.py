"""Product Owner Review — Three Amigos PO / BA perspective.

Reviews user stories from a business-value and stakeholder-alignment
viewpoint.
"""

from three_amigos.States.state import ThreeAmigosState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from three_amigos.agents._common import _stream_llm, _save_output, load_prompt
from three_amigos.agents._discussion import _build_discussion_context


def product_owner_review(state: ThreeAmigosState) -> dict:
    """Three Amigos — Product Owner / BA perspective."""
    system_prompt = load_prompt("product_owner.md")
    round_num = state.get("discussion_round", 0) + 1
    context = _build_discussion_context(state)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response_text = _stream_llm(messages, agent_label=f"PRODUCT OWNER (Round {round_num})")
    _save_output(state, f"po_review_round_{round_num}", response_text,
                 title=f"Product Owner Review — Round {round_num}")
    print(f"🧑‍💼  Product Owner review complete (round {round_num}).")

    return {
        "messages": [
            AIMessage(
                content=f"[PRODUCT OWNER — Round {round_num}]\n{response_text}"
            )
        ],
        "po_feedback": response_text,
    }
