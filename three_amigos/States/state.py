"""Three Amigos workflow state definition.

Defines the central TypedDict state schema that flows through all phases
of the requirements engineering workflow.
"""

from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages


class ThreeAmigosState(TypedDict):
    """Central state for the Three Amigos requirements engineering workflow.

    This state flows through all phases of the pipeline:

    1. **Supervisor analysis** — initial assessment of user research
    2. **Elicitation** — extract structured user needs (with optional
       human-in-the-loop clarification)
    3. **Requirements engineering** — derive formal FRs and NFRs
    4. **Story writing** — create user stories with BDD acceptance criteria
    5. **Three Amigos discussion** — iterative refinement by PO, Dev, QA
    6. **Human review** — final human approval or revision
    7. **Final compilation** — comprehensive Markdown report
    """

    # ── Core Message History (LangGraph reducer: appends) ──────────
    messages: Annotated[list, add_messages]

    # ── Input ──────────────────────────────────────────────────────
    user_research: str

    # ── Elicitation Phase ──────────────────────────────────────────
    extracted_user_needs: str
    clarification_questions: str
    needs_clarification: bool

    # ── Requirements Phase ─────────────────────────────────────────
    functional_requirements: str
    non_functional_requirements: str

    # ── Story Writing Phase ────────────────────────────────────────
    user_stories: str

    # ── Three Amigos Discussion ────────────────────────────────────
    po_feedback: str
    dev_feedback: str
    qa_feedback: str
    discussion_history: list[str]
    discussion_round: int
    max_discussion_rounds: int
    consensus_reached: bool

    # ── Human Review ───────────────────────────────────────────────
    human_approved: bool

    # ── Final Output ───────────────────────────────────────────────
    final_output: str
    current_phase: str

    # ── File I/O ───────────────────────────────────────────────────
    output_dir: str
