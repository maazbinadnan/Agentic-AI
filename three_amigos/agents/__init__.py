"""Three Amigos agent nodes and routing logic.

Re-exports every node function and routing helper so that downstream
modules can still do::

    from three_amigos.agents import supervisor_agent, route_consensus, ...
"""

# ── Node functions ──────────────────────────────────────────────────────────
from three_amigos.agents.supervisor_agent import supervisor_agent
from three_amigos.agents.elicitation_agent import (
    elicitation_agent,
    human_clarification_node,
)
from three_amigos.agents.requirements_engineer_agent import requirements_engineer_agent
from three_amigos.agents.story_writer_agent import story_writer_agent
from three_amigos.agents.product_owner_review import product_owner_review
from three_amigos.agents.developer_review import developer_review
from three_amigos.agents.qa_review import qa_review
from three_amigos.agents.consensus_check import check_consensus
from three_amigos.agents.human_review import human_review_node
from three_amigos.agents.final_compiler import compile_final_output

# ── Routing helpers ─────────────────────────────────────────────────────────
from three_amigos.agents.routing import (
    route_clarification,
    route_consensus,
    route_human_approval,
)

__all__ = [
    "supervisor_agent",
    "elicitation_agent",
    "human_clarification_node",
    "requirements_engineer_agent",
    "story_writer_agent",
    "product_owner_review",
    "developer_review",
    "qa_review",
    "check_consensus",
    "human_review_node",
    "compile_final_output",
    "route_clarification",
    "route_consensus",
    "route_human_approval",
]
