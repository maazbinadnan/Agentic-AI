"""Three Amigos Multi-Agent System — LangGraph Workflow Definition.

Defines the ``StateGraph`` that wires together all agent nodes, conditional
edges, and human-in-the-loop interrupts.

Graph topology
──────────────
  START
    → supervisor
    → elicitation  ─┬─ (clarification needed?) ─→ human_clarification ─┐
                     │                                                   │
                     │  ←────────────────────────────────────────────────┘
                     └─ (proceed) ─→ requirements_engineer
                                       → story_writer
                                       → po_review
                                       → dev_review
                                       → qa_review
                                       → consensus_check ─┬─ (continue) ─→ po_review (loop)
                                                           └─ (review)   ─→ human_review
                                                                             ├─ (revise)   ─→ po_review
                                                                             └─ (approved) ─→ compile_final
                                                                                                → END
"""

from langgraph.graph import StateGraph, START, END
from three_amigos.States.state import ThreeAmigosState
from three_amigos.functions import (
    supervisor_agent,
    elicitation_agent,
    human_clarification_node,
    requirements_engineer_agent,
    story_writer_agent,
    product_owner_review,
    developer_review,
    qa_review,
    check_consensus,
    human_review_node,
    compile_final_output,
    # routing helpers
    route_clarification,
    route_consensus,
    route_human_approval,
)


def create_graph(checkpointer=None):
    """Build and compile the Three Amigos LangGraph workflow.

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

    workflow = StateGraph(ThreeAmigosState)

    # ── Register nodes ────────────────────────────────────────────────────
    workflow.add_node("supervisor", supervisor_agent)
    workflow.add_node("elicitation", elicitation_agent)
    workflow.add_node("human_clarification", human_clarification_node)
    workflow.add_node("requirements_engineer", requirements_engineer_agent)
    workflow.add_node("story_writer", story_writer_agent)
    workflow.add_node("po_review", product_owner_review)
    workflow.add_node("dev_review", developer_review)
    workflow.add_node("qa_review", qa_review)
    workflow.add_node("consensus_check", check_consensus)
    workflow.add_node("human_review", human_review_node)
    workflow.add_node("compile_final", compile_final_output)

    # ── Phase 1: Supervisor → Elicitation ─────────────────────────────────
    workflow.add_edge(START, "supervisor")
    workflow.add_edge("supervisor", "elicitation")

    # ── Phase 2: Elicitation ⇄ Human Clarification ───────────────────────
    workflow.add_conditional_edges(
        "elicitation",
        route_clarification,
        {
            "needs_clarification": "human_clarification",
            "proceed": "requirements_engineer",
        },
    )
    workflow.add_edge("human_clarification", "elicitation")

    # ── Phase 3: Requirements → Stories ───────────────────────────────────
    workflow.add_edge("requirements_engineer", "story_writer")

    # ── Phase 4: Three Amigos Discussion Loop ─────────────────────────────
    workflow.add_edge("story_writer", "po_review")
    workflow.add_edge("po_review", "dev_review")
    workflow.add_edge("dev_review", "qa_review")
    workflow.add_edge("qa_review", "consensus_check")

    workflow.add_conditional_edges(
        "consensus_check",
        route_consensus,
        {
            "continue_discussion": "po_review",  # loop back
            "review": "human_review",             # exit loop
        },
    )

    # ── Phase 5: Human Approval ───────────────────────────────────────────
    workflow.add_conditional_edges(
        "human_review",
        route_human_approval,
        {
            "approved": "compile_final",
            "revise": "po_review",  # loop back for another round
        },
    )

    # ── Phase 6: Final Output → END ──────────────────────────────────────
    workflow.add_edge("compile_final", END)

    # ── Compile ──────────────────────────────────────────────────────────
    return workflow.compile(checkpointer=checkpointer)


# Default export — used by ``langgraph.json`` for deployment.
# The deployment platform supplies its own checkpointer; for local CLI
# usage see ``run.py`` which passes a ``MemorySaver``.
app = create_graph()
