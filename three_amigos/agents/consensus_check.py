"""Consensus Check — evaluate Three Amigos feedback.

Determines whether the Product Owner, Developer, and QA Engineer have
reached consensus, and refines stories if they have not.
"""

from three_amigos.States.state import ThreeAmigosState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from three_amigos.agents._common import _stream_llm, _save_output, load_prompt


def check_consensus(state: ThreeAmigosState) -> dict:
    """Evaluate Three Amigos feedback; refine stories if no consensus."""
    system_prompt = load_prompt("consensus_checker.md")
    round_num = state.get("discussion_round", 0) + 1

    context = (
        f"## Round {round_num} Discussion Summary\n\n"
        f"## Current User Stories\n\n{state.get('user_stories', '')}\n\n"
        f"## Product Owner Feedback\n\n{state.get('po_feedback', '')}\n\n"
        f"## Developer Feedback\n\n{state.get('dev_feedback', '')}\n\n"
        f"## QA Engineer Feedback\n\n{state.get('qa_feedback', '')}"
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response_text = _stream_llm(messages, agent_label="CONSENSUS CHECK")

    consensus = "CONSENSUS: YES" in response_text.upper()

    # Append a round summary to the discussion history
    round_summary = (
        f"### Round {round_num}\n"
        f"**PO highlights:** {state.get('po_feedback', '')[:400]}…\n\n"
        f"**Dev highlights:** {state.get('dev_feedback', '')[:400]}…\n\n"
        f"**QA highlights:** {state.get('qa_feedback', '')[:400]}…\n\n"
        f"**Consensus:** {'✅ Reached' if consensus else '❌ Not reached'}\n"
    )
    history = list(state.get("discussion_history") or [])
    history.append(round_summary)

    # Extract refined / final stories from the response
    updated_stories = state.get("user_stories", "")
    for marker in ("### Refined User Stories", "### Final User Stories"):
        if marker in response_text:
            parts = response_text.split(marker, 1)
            if len(parts) > 1:
                updated_stories = marker + parts[1]
            break

    _save_output(state, f"consensus_round_{round_num}", response_text,
                 title=f"Consensus Check — Round {round_num}")

    status = "✅  Consensus reached!" if consensus else f"🔄  Round {round_num} — no consensus; refining…"
    print(f"\n{status}")

    return {
        "messages": [
            AIMessage(
                content=f"[CONSENSUS CHECK — Round {round_num}]\n{response_text}"
            )
        ],
        "consensus_reached": consensus,
        "discussion_round": round_num,
        "discussion_history": history,
        "user_stories": updated_stories,
        "current_phase": "consensus_check",
    }
