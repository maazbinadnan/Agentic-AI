"""Supervisor-Worker Pattern — LangGraph workflow definition."""

from pathlib import Path
from langgraph.graph import StateGraph, START, END
from supervisor_worker.local_states._state_ import AgentState
import supervisor_worker.agents.business_analyst as ba
import supervisor_worker.agents.supervisor as supervisor
import supervisor_worker.agents.routing as router
from global_layer.functions import _draw_graph


def create_graph(checkpointer=None):
    """Build and compile the Supervisor-Worker workflow graph."""
    workflow = StateGraph(AgentState)

    # ── Register nodes ────────────────────────────────────────────────────
    workflow.add_node("business_analyst", ba.generate)
    workflow.add_node("supervisor", supervisor.generate)

    # ── Edges ────────────────────────────────────────────────────────────
    workflow.add_edge(START, "business_analyst")
    workflow.add_edge("business_analyst", "supervisor")

    # ── Conditional edges based on supervisor review ─────────────────────
    workflow.add_conditional_edges(
        "supervisor",
        router.route,
        {
            "business_analyst": "business_analyst",
            "FINISH": END,
        },
    )

    return workflow.compile(checkpointer=checkpointer)


# Default export — used by deployment / langgraph.json
app = create_graph()

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    try:
        _draw_graph(app, output_path=Path(root / "graph.png"))
    except Exception as e:
        print(f"Could not render graph image: {e}")
