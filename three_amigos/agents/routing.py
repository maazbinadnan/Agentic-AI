"""Routing functions — conditional-edge selectors for the LangGraph workflow.

These pure functions inspect the current state and return a string key
that tells LangGraph which edge to follow.
"""

from three_amigos.States.state import ThreeAmigosState


def route_clarification(state: ThreeAmigosState) -> str:
    """Does the elicitation agent need human clarification?"""
    if state.get("needs_clarification", False):
        return "needs_clarification"
    return "proceed"


def route_consensus(state: ThreeAmigosState) -> str:
    """Have the Three Amigos reached consensus, or should they loop?"""
    max_rounds = state.get("max_discussion_rounds", 3)
    current_round = state.get("discussion_round", 0)
    consensus = state.get("consensus_reached", False)

    if consensus or current_round >= max_rounds:
        return "review"
    return "continue_discussion"


def route_human_approval(state: ThreeAmigosState) -> str:
    """Did the human approve the output?"""
    if state.get("human_approved", False):
        return "approved"
    return "revise"
