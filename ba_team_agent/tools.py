from enum import Enum
from langchain.tools import tool

from ba_team_agent._common_ import read_file
from ba_team_agent.subagents.elicitation import elicitation_subagent
from ba_team_agent.subagents.user_needs import user_needs_subagent
from ba_team_agent.subagents.functional_requirements import functional_requirements_subagent
from ba_team_agent.subagents.non_functional_requirements import non_functional_requirements_subagent
from ba_team_agent.subagents.user_stories import user_stories_subagent

__all__ = ["task", "read_file", "SubagentType"]


class SubagentType(str, Enum):
    """Registry of available subagent roles and their aliases."""

    ELICITATION = "elicitation"
    ELICITATION_SPECIALIST = "elicitation_specialist"

    USER_NEEDS = "user_needs"
    USER_NEEDS_GENERATOR = "user_needs_generator"

    FUNCTIONAL_REQUIREMENTS = "functional_requirements"
    FUNCTIONAL_REQUIREMENTS_GENERATOR = "functional_requirements_generator"

    NON_FUNCTIONAL_REQUIREMENTS = "non_functional_requirements"
    NON_FUNCTIONAL_REQUIREMENTS_GENERATOR = "non_functional_requirements_generator"

    USER_STORIES = "user_stories"
    USER_STORY_WRITER = "user_story_writer"


# Mapping Enum values and string names to compiled subagent instances
SUBAGENTS = {
    SubagentType.ELICITATION.value: elicitation_subagent,
    SubagentType.ELICITATION_SPECIALIST.value: elicitation_subagent,
    SubagentType.USER_NEEDS.value: user_needs_subagent,
    SubagentType.USER_NEEDS_GENERATOR.value: user_needs_subagent,
    SubagentType.FUNCTIONAL_REQUIREMENTS.value: functional_requirements_subagent,
    SubagentType.FUNCTIONAL_REQUIREMENTS_GENERATOR.value: functional_requirements_subagent,
    SubagentType.NON_FUNCTIONAL_REQUIREMENTS.value: non_functional_requirements_subagent,
    SubagentType.NON_FUNCTIONAL_REQUIREMENTS_GENERATOR.value: non_functional_requirements_subagent,
    SubagentType.USER_STORIES.value: user_stories_subagent,
    SubagentType.USER_STORY_WRITER.value: user_stories_subagent,
}


@tool
def task(agent_name: SubagentType, description: str) -> str:
    """Launch an ephemeral subagent for a task.

    Available agents:
    - elicitation: Clarifies user needs from raw operational requirements documents via stakeholder Q&A.
    - user_needs: Generates target user personas and structured User Needs specifications (UN-001, UN-002...).
    - functional_requirements: Generates formal system inputs, workflows, and Functional Requirements (FR-001, FR-002...).
    - non_functional_requirements: Formulates quality attributes, SLA metrics, and Non-Functional Requirements (NFR-001...).
    - user_stories: Formulates Agile User Stories (US-001) with Given/When/Then Acceptance Criteria (AC-001).
    """
    raw_name = agent_name.value if isinstance(agent_name, Enum) else str(agent_name)
    key = raw_name.lower().strip()
    
    agent = SUBAGENTS.get(key, elicitation_subagent)
    
    result = agent.invoke(
        {"messages": [{"role": "user", "content": description}]},
        config={"recursion_limit": 50}
    )
    
    messages = result.get("messages", [])
    if messages:
        return str(messages[-1].content)
    return "Sub-agent task completed."