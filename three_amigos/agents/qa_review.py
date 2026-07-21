"""QA Engineer Review — Three Amigos QA perspective.

Reviews user stories from a quality assurance, testability, and edge-case
coverage viewpoint.
"""

from three_amigos.States.state import ThreeAmigosState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from three_amigos.agents._common import _stream_llm, _save_output, load_prompt
from three_amigos.agents._discussion import _build_discussion_context


def qa_review(state: ThreeAmigosState) -> dict:
    """Three Amigos — QA Engineer perspective."""
    system_prompt = load_prompt("qa_engineer.md")
    round_num = state.get("discussion_round", 0) + 1
    context = _build_discussion_context(state, include_po=True, include_dev=True)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response_text = _stream_llm(messages, agent_label=f"QA ENGINEER (Round {round_num})")
    _save_output(state, f"qa_review_round_{round_num}", response_text,
                 title=f"QA Engineer Review — Round {round_num}")
    print(f"🧪  QA Engineer review complete (round {round_num}).")

    return {
        "messages": [
            AIMessage(
                content=f"[QA ENGINEER — Round {round_num}]\n{response_text}"
            )
        ],
        "qa_feedback": response_text,
    }
