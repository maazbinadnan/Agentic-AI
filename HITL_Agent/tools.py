import os
import re
from pathlib import Path
from enum import Enum
from langchain.tools import tool

from hitl_agent._common_ import read_file
from hitl_agent.subagents.elicitation import elicitation_subagent
from hitl_agent.subagents.design_elicitation import design_elicitation_subagent
from hitl_agent.subagents.user_needs import user_needs_subagent
from hitl_agent.subagents.functional_requirements import functional_requirements_subagent
from hitl_agent.subagents.non_functional_requirements import non_functional_requirements_subagent
from hitl_agent.subagents.user_stories import user_stories_subagent
from hitl_agent.subagents.interaction_designer import ixd_subagent

__all__ = ["task", "read_file", "SubagentType"]


class SubagentType(str, Enum):
    """Registry of available subagent roles."""

    ELICITATION = "elicitation"
    DESIGN_ELICITATION = "design_elicitation"
    USER_NEEDS = "user_needs"
    FUNCTIONAL_REQUIREMENTS = "functional_requirements"
    NON_FUNCTIONAL_REQUIREMENTS = "non_functional_requirements"
    USER_STORIES = "user_stories"
    INTERACTION_DESIGNER = "interaction_designer"


# Mapping Enum values to compiled subagent instances
SUBAGENTS = {
    SubagentType.ELICITATION.value: elicitation_subagent,
    SubagentType.DESIGN_ELICITATION.value: design_elicitation_subagent,
    SubagentType.USER_NEEDS.value: user_needs_subagent,
    SubagentType.FUNCTIONAL_REQUIREMENTS.value: functional_requirements_subagent,
    SubagentType.NON_FUNCTIONAL_REQUIREMENTS.value: non_functional_requirements_subagent,
    SubagentType.USER_STORIES.value: user_stories_subagent,
    SubagentType.INTERACTION_DESIGNER.value: ixd_subagent,
}

EXPECTED_OUTPUT_FILES = {
    SubagentType.ELICITATION.value: "01_elicitation_report.md",
    SubagentType.USER_NEEDS.value: "02_user_needs_report.md",
    SubagentType.FUNCTIONAL_REQUIREMENTS.value: "03_functional_requirements.md",
    SubagentType.NON_FUNCTIONAL_REQUIREMENTS.value: "04_non_functional_requirements.md",
    SubagentType.USER_STORIES.value: "05_user_stories.md",
    SubagentType.DESIGN_ELICITATION.value: "06_design_requirements.md",
    SubagentType.INTERACTION_DESIGNER.value: "07_ui_mockups.md",
}


@tool
def task(agent_name: SubagentType, description: str) -> str:
    """Launch an ephemeral subagent for a task.

    Available agents:
    - elicitation: Clarifies user needs from raw operational requirements documents via stakeholder Q&A.
    - design_elicitation: Conducts stakeholder Q&A for visual/UI preferences (colors, theme, typography, layout) and generates 06_design_requirements.md.
    - user_needs: Generates target user personas and structured User Needs specifications (UN-001, UN-002...).
    - functional_requirements: Generates formal system inputs, workflows, and Functional Requirements (FR-001, FR-002...).
    - non_functional_requirements: Formulates quality attributes, SLA metrics, and Non-Functional Requirements (NFR-001...).
    - user_stories: Formulates Agile User Stories (US-001) with Given/When/Then Acceptance Criteria (AC-001).
    - interaction_designer: Generates UI wireframes/mockups, screen layout specifications, and User Story to UI mapping table (06_ui_mockups.md).
    """
    raw_name = agent_name.value if isinstance(agent_name, Enum) else str(agent_name)
    key = raw_name.lower().strip()
    
    agent = SUBAGENTS.get(key, elicitation_subagent)
    
    # Extract output directory from description if specified
    out_dir_match = re.search(r"Output Directory:\s*['\"]?([^'\"\n]+)['\"]?", description, re.IGNORECASE)
    output_dir = out_dir_match.group(1).strip() if out_dir_match else "outputs"
    
    result = agent.invoke(
        {"messages": [{"role": "user", "content": description}]},
        config={"recursion_limit": 50}
    )
    
    messages = result.get("messages", [])
    last_content = str(messages[-1].content) if messages else "Sub-agent task completed."

    # Programmatic file creation check (Option 2)
    expected_filename = EXPECTED_OUTPUT_FILES.get(key)
    if expected_filename:
        file_path = Path(output_dir) / expected_filename
        if not file_path.exists():
            return (
                f"SUB-AGENT EXECUTION FAILED / INCOMPLETE: The sub-agent '{key}' finished execution, "
                f"but its designated output file '{expected_filename}' was NOT created on disk in '{output_dir}'. "
                f"Please re-invoke the '{key}' sub-agent to properly complete and save '{expected_filename}'.\n\n"
                f"Sub-agent response text: {last_content}"
            )

    return last_content