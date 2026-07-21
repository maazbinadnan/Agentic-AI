"""Shared helper for the Three Amigos discussion-round reviewers.

The ``_build_discussion_context`` function is used by the Product Owner,
Developer, and QA Engineer review agents to assemble a consistent
context string.
"""

from three_amigos.States.state import ThreeAmigosState


def _build_discussion_context(
    state: ThreeAmigosState,
    *,
    include_po: bool = False,
    include_dev: bool = False,
) -> str:
    """Helper: build the context string for a Three Amigos reviewer."""
    round_num = state.get("discussion_round", 0) + 1
    parts = [
        f"## Discussion Round: {round_num}\n",
        f"## Original User Research\n\n{state['user_research']}\n",
        f"## Current User Stories\n\n{state.get('user_stories', '')}\n",
    ]
    if include_po:
        parts.append(f"## Product Owner's Feedback\n\n{state.get('po_feedback', '')}\n")
    if include_dev:
        parts.append(f"## Developer's Feedback\n\n{state.get('dev_feedback', '')}\n")

    history = state.get("discussion_history") or []
    if history:
        parts.append(
            "## Previous Discussion History\n\n"
            + "\n\n---\n\n".join(history)
        )
    return "\n".join(parts)
