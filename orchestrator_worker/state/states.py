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

# ------- designer output ------- #
class html_mockups(BaseModel):
    file_name:str = Field(
        description= "The file name relating to the html mockup such as 'login_mockup.html' based on the user stories"
    )
    html:str = Field(
        description= 'The formatted HTML relating to the file name and user story'
    )

class HtmlMapping(BaseModel):
    architecture_mapping: str = Field(
        description=(
            "Markdown table or mapping string connecting HTML screen filenames "
            "to their corresponding User Stories (US-XXX) / Requirements (FR-XXX) "
            "and key interactions visualized."
        )
    )
    design_tradeoff: str = Field(
        description=(
            "Markdown section detailing UI/UX design choices, layout rationale, "
            "and state handling explanations."
        )
    )

class ixd_output(BaseModel):
    html_files: list[html_mockups] = Field(
        description= "a  list of the generated HTML files"
    )
    html_mapping: HtmlMapping = Field(
        description= "markdown of the architecture and design trade_off"
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
    full_ba_analysis: str | None
    user_needs: str | None
    functional_requirements: str | None
    non_functional_requirements: str | None
    user_stories: str | None

    # ── IxD Team output ────────────────────────────────────────────
    html_mockups: str | None

    # ── Final output ───────────────────────────────────────────────
    final_output: str | None

    # ── File I/O ───────────────────────────────────────────────────
    output_dir: str | None