"""Requirements Engineer Agent — Phase 3: derive formal FRs and NFRs.

Takes extracted user needs and produces structured functional and
non-functional requirements.
"""

from three_amigos.States.state import ThreeAmigosState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from three_amigos.agents._common import _stream_llm, _save_output, load_prompt


def requirements_engineer_agent(state: ThreeAmigosState) -> dict:
    """Phase 3 — Derive formal FRs and NFRs from user needs."""
    system_prompt = load_prompt("requirements_engineer.md")
    user_needs = state.get("extracted_user_needs", "")
    user_research = state["user_research"]

    context = (
        f"## Original User Research\n\n{user_research}\n\n"
        f"## Extracted User Needs\n\n{user_needs}"
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response_text = _stream_llm(messages, agent_label="REQUIREMENTS ENGINEER")

    # Try to split FR / NFR sections for downstream agents
    fr_section = response_text
    nfr_section = response_text

    for heading in ("### Non-Functional Requirements", "## Non-Functional Requirements"):
        if heading in response_text:
            parts = response_text.split(heading, 1)
            fr_section = parts[0]
            nfr_section = heading + parts[1]
            break

    # Save the full response, plus separate FR and NFR files
    _save_output(state, "requirements_full", response_text, title="Requirements (Full)")
    _save_output(state, "functional_requirements", fr_section, title="Functional Requirements")
    _save_output(state, "non_functional_requirements", nfr_section, title="Non-Functional Requirements")
    print("\n✅  Functional & non-functional requirements derived.")

    return {
        "messages": [
            AIMessage(content=f"[REQUIREMENTS ENGINEER]\n{response_text}")
        ],
        "functional_requirements": fr_section,
        "non_functional_requirements": nfr_section,
        "current_phase": "requirements",
    }
