"""Orchestrator-Worker Coordinator — LangGraph Workflow Definition.

Defines the ``StateGraph`` that wires together all agent nodes and
conditional edges.

Graph topology
──────────────
  START
    → coordinator
    → ba_team        → coordinator
    → interaction_designers  → coordinator
    → compile_final
    → END
"""

from pathlib import Path
from global_functions.functions import _draw_graph

from langgraph.graph import StateGraph, START, END
from orchestrator_worker.state.states import GlobalState
from orchestrator_worker.agents import (
    coordinator_node,
    ba_team_node,
    interaction_designers_node,
    compile_final_output,
    route_after_coordinator,
)


def create_graph(checkpointer=None):
    """Build and compile the Orchestrator-Worker coordinator workflow.

    Parameters
    ----------
    checkpointer : langgraph.checkpoint.base.BaseCheckpointSaver, optional
        A checkpointer instance (e.g. ``MemorySaver``) required for
        human-in-the-loop ``interrupt()`` calls.  When deploying via
        ``langgraph.json`` the platform provides its own checkpointer,
        so this can be ``None`` for the default ``app`` export.

    Returns
    -------
    langgraph.graph.state.CompiledStateGraph
        The compiled, ready-to-invoke graph.
    """

    workflow = StateGraph(GlobalState)

    # ── Register nodes ────────────────────────────────────────────────────
    workflow.add_node("coordinator", coordinator_node)
    workflow.add_node("ba_team", ba_team_node)
    workflow.add_node("interaction_designers", interaction_designers_node)
    workflow.add_node("compile_final", compile_final_output)

    # ── Phase 1: START → Coordinator ──────────────────────────────────────
    workflow.add_edge(START, "coordinator")

    # # ── Phase 2: Coordinator routes to workers or compiler ────────────────
    # workflow.add_conditional_edges(
    #     "coordinator",
    #     route_after_coordinator,
    #     {
    #         "ba_team": "ba_team",
    #         "interaction_designers": "interaction_designers",
    #         "compile": "compile_final",
    #     },
    # )

    # # ── Workers always loop back to the coordinator ───────────────────────
    # workflow.add_edge("ba_team", "coordinator")
    # workflow.add_edge("interaction_designers", "coordinator")

    # ── Compiler → END ────────────────────────────────────────────────────
    workflow.add_edge("coordinator", END)

    # ── Compile ──────────────────────────────────────────────────────────
    return workflow.compile(checkpointer=checkpointer)


# Default export — used by ``langgraph.json`` for deployment.
app = create_graph()

root = Path(__file__).resolve().parent

_draw_graph(app, output_path=Path(root / "graph.png"))
