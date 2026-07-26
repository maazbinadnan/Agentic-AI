"""Single Agent — Linear Workflow Definition (BA -> IxD -> Compile)."""

from pathlib import Path
from langgraph.graph import StateGraph, START, END
from single_agent.local_states._state_ import AgentState, OutputState
import single_agent.agents.business_analyst as ba
import single_agent.agents.interaction_designer as ixd
import single_agent.agents.compile_deliverables as compiler
from global_layer.functions import _draw_graph


def create_graph(checkpointer=None):
    """Build and compile the Single Agent linear workflow graph."""
    workflow = StateGraph(AgentState, output_schema=OutputState)

    # ── Register nodes ────────────────────────────────────────────────────
    workflow.add_node("business_analyst", ba.generate)
    workflow.add_node("interaction_designer", ixd.generate)
    workflow.add_node("compile_deliverables", compiler.generate)

    # ── Linear Edges ──────────────────────────────────────────────────────
    workflow.add_edge(START, "business_analyst")
    workflow.add_edge("business_analyst", "interaction_designer")
    workflow.add_edge("interaction_designer", "compile_deliverables")
    workflow.add_edge("compile_deliverables", END)

    return workflow.compile(checkpointer=checkpointer)


# Default export — used by deployment / langgraph.json
app = create_graph()

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    try:
        _draw_graph(app, output_path=Path(root / "graph.png"))
    except Exception as e:
        print(f"Could not render graph image: {e}")
