"""Story Writer Agent — Phase 4: create user stories with BDD criteria.

Transforms functional and non-functional requirements into user stories
with Behaviour-Driven Development acceptance criteria.
"""

from three_amigos.States.state import ThreeAmigosState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from three_amigos.agents._common import _stream_llm, _save_output, load_prompt


def story_writer_agent(state: ThreeAmigosState) -> dict:
    """Phase 4 — Create user stories with BDD acceptance criteria."""
    system_prompt = load_prompt("story_writer.md")
    fr = state.get("functional_requirements", "")
    nfr = state.get("non_functional_requirements", "")

    context = (
        f"## Functional Requirements\n\n{fr}\n\n"
        f"## Non-Functional Requirements\n\n{nfr}"
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response_text = _stream_llm(messages, agent_label="STORY WRITER")
    _save_output(state, "user_stories", response_text, title="User Stories with BDD Acceptance Criteria")
    print("✅  User stories with BDD acceptance criteria created.")

    return {
        "messages": [
            AIMessage(content=f"[STORY WRITER]\n{response_text}")
        ],
        "user_stories": response_text,
        "current_phase": "stories",
    }
