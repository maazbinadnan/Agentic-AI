"""Orchestrator-Worker Coordinator workflow state definition.

Defines the central TypedDict state schema that flows through all phases
of the coordinator pipeline.
"""

from typing import Annotated, Literal, TypedDict
from pydantic import BaseModel, Field
from langgraph.graph.message import add_messages


# ── Structured output for the coordinator's routing decision ──────────────

class CoordinatorDecision(BaseModel):
    next_agent: Literal["ba_team", "interaction_designers", "FINISH"] = Field(
        description="The next team to route to, or FINISH if all work is done."
    )
    justification: str = Field(
        description="Brief explanation of why this routing choice was made."
    )


# ── Structured output for the compiler's story-mockup extraction ──────────
class StoryMockup(BaseModel):
    story_number: int = Field(
        description="The user story number (e.g. 1, 2, 3)."
    )
    story_title: str = Field(
        description="A short title for the user story."
    )
    html_content: str = Field(
        description="The complete, self-contained HTML mockup for this story."
    )


class CompilerExtraction(BaseModel):
    story_mockups: list[StoryMockup] = Field(
        description="A list of user story to HTML mockup mappings."
    )


# ── Central workflow state ────────────────────────────────────────────────

class GlobalState(TypedDict):
    """Central state for the Orchestrator-Worker coordinator pipeline.

    Flows through all phases:
      1. **Coordinator** — routes work to the right team
      2. **BA Team** — formalises raw research into user stories & acceptance criteria
      3. **Interaction Designers** — designs HTML mockups from the stories
      4. **Compiler** — assembles a final consolidated report
    """

    # ── Core message history (LangGraph reducer: appends) ──────────
    messages: Annotated[list, add_messages] | None

    # ── Input ──────────────────────────────────────────────────────
    input: str | None

    # ── Routing ────────────────────────────────────────────────────
    next_agent: str | None
    current_phase: str

    # ── BA Team output ─────────────────────────────────────────────
    user_stories: str | None

    # ── IxD Team output ────────────────────────────────────────────
    html_mockups: str | None

    # ── Final output ───────────────────────────────────────────────
    final_output: str | None

    # ── File I/O ───────────────────────────────────────────────────
    output_dir: str | None