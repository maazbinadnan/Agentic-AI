"""Routing functions — conditional-edge selectors for the coordinator workflow.

These pure functions inspect the current state and return a string key
that tells LangGraph which edge to follow.
"""

from orchestrator_worker.state.states import GlobalState


def route_after_coordinator(state: GlobalState) -> str:
    """Route to the team the coordinator chose, or to the compiler if finished."""
    next_agent = state.get("next_agent", "FINISH")
    assert next_agent is not None
    if next_agent == "FINISH":
        return "FINISH"
    return next_agent 
