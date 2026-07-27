from pathlib import Path
from typing import List
from pydantic import Field
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

from react_agent._common_ import llm, load_prompt
from global_layer.ba_state import (
    UserNeed,
    FunctionalRequirement,
    NonFunctionalRequirement,
    UserStory,
    TraceabilityEntry,
    GapRecommendation,
    SummaryStatistics,
    RequirementsPipelineOutput,
)
from global_layer.functions import _save__requirement_files

__all__ = ["build_react_graph", "app"]


class SaveBARequirementsInput(RequirementsPipelineOutput):
    """Schema for saving complete BA requirements pipeline deliverables into output_dir."""
    output_dir: str = Field(
        default="outputs_react",
        description="Target output directory path where the 5 markdown files must be saved."
    )


# ==========================================
# Structured ReAct Tool using Extended Schema
# ==========================================
@tool(args_schema=SaveBARequirementsInput)
def save_complete_ba_requirements(
    user_needs: List[UserNeed],
    functional_requirements: List[FunctionalRequirement],
    non_functional_requirements: List[NonFunctionalRequirement],
    user_stories: List[UserStory],
    traceability_matrix: List[TraceabilityEntry],
    gaps_and_recommendations: List[GapRecommendation],
    summary_statistics: SummaryStatistics,
    output_dir: str = "outputs_react"
) -> str:
    """Saves the complete structured RequirementsPipelineOutput into all 5 IEEE markdown files in output_dir:
    1. 01_user_needs.md
    2. 02_functional_requirements.md
    3. 03_non_functional_requirements.md
    4. 04_user_stories.md
    5. 05_analysis_summary.md
    """
    pipeline_output = RequirementsPipelineOutput(
        user_needs=user_needs,
        functional_requirements=functional_requirements,
        non_functional_requirements=non_functional_requirements,
        user_stories=user_stories,
        traceability_matrix=traceability_matrix,
        gaps_and_recommendations=gaps_and_recommendations,
        summary_statistics=summary_statistics,
    )
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    _save__requirement_files(pipeline_output, output_dir=str(out_path.resolve()))
    return (
        f"Successfully generated and saved all 5 structured requirements markdown files into '{out_path.resolve()}':\n"
        f"- 01_user_needs.md ({len(user_needs)} items)\n"
        f"- 02_functional_requirements.md ({len(functional_requirements)} items)\n"
        f"- 03_non_functional_requirements.md ({len(non_functional_requirements)} items)\n"
        f"- 04_user_stories.md ({len(user_stories)} items)\n"
        f"- 05_analysis_summary.md (Traceability + Gaps + Stats)"
    )


# ==========================================
# ReAct Graph Builder
# ==========================================
def build_react_graph():
    """Builds and compiles the ReAct agent graph using structured tools."""
    tools = [save_complete_ba_requirements]

    system_prompt = load_prompt("react_prompt.md")
    checkpointer = InMemorySaver()

    react_graph = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt,
        checkpointer=checkpointer,
        name="ReAct_Structured_RE_Agent",
    )
    return react_graph


app = build_react_graph()
