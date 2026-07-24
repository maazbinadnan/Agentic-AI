"""BA Team Agent — formalises raw user research into user stories.

Produces structured User Stories with Given-When-Then BDD acceptance
criteria from the raw research input.
"""

import re
from orchestrator_worker.state.states import GlobalState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from orchestrator_worker.agents._common import _stream_llm, _save_output, load_prompt


def _extract_ba_sections(response_text: str) -> dict[str, str]:
    """Extract individual artifacts from the Business Analyst markdown output."""
    un_pattern = r"(?i)#+\s*(?:1\.\s*)?Discovered User Needs"
    fr_pattern = r"(?i)#+\s*(?:2\.\s*)?Functional Requirements"
    nfr_pattern = r"(?i)#+\s*(?:3\.\s*)?Non-Functional Requirements"
    us_pattern = r"(?i)#+\s*(?:4\.\s*)?Agile User Stories"

    match_un = re.search(un_pattern, response_text)
    match_fr = re.search(fr_pattern, response_text)
    match_nfr = re.search(nfr_pattern, response_text)
    match_us = re.search(us_pattern, response_text)

    user_needs = response_text
    functional_requirements = response_text
    non_functional_requirements = response_text
    user_stories = response_text

    if match_un and match_fr and match_nfr and match_us:
        pos_un = match_un.start()
        pos_fr = match_fr.start()
        pos_nfr = match_nfr.start()
        pos_us = match_us.start()

        if pos_un < pos_fr < pos_nfr < pos_us:
            user_needs = response_text[pos_un:pos_fr].strip()
            functional_requirements = response_text[pos_fr:pos_nfr].strip()
            non_functional_requirements = response_text[pos_nfr:pos_us].strip()
            user_stories = response_text[pos_us:].strip()

    return {
        "user_needs": user_needs,
        "functional_requirements": functional_requirements,
        "non_functional_requirements": non_functional_requirements,
        "user_stories": user_stories,
    }


def ba_team_node(state: GlobalState) -> dict:
    """BA Team — formalise raw research into user stories and acceptance criteria."""
    system_prompt = load_prompt("business_analyst.md")
    data = state["input"]

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(
            content=(
                f"{data}"
            )
        ),
    ]

    response_text = _stream_llm(messages, agent_label="BA TEAM")
    sections = _extract_ba_sections(response_text)

    # Save full BA report file along with 4 separate artifact files
    _save_output(state, "full_ba_analysis.md", response_text, title="Business Analysis & Requirements Specification")
    _save_output(state, "user_needs.md", sections["user_needs"], title="Discovered User Needs")
    _save_output(state, "functional_requirements.md", sections["functional_requirements"], title="Functional Requirements")
    _save_output(state, "non_functional_requirements.md", sections["non_functional_requirements"], title="Non-Functional Requirements")
    _save_output(state, "user_stories.md", sections["user_stories"], title="User Stories & Acceptance Criteria")

    print("✅  BA Team analysis complete.")

    return {
        "messages": [
            AIMessage(content=f"[BA TEAM]\n{response_text}")
        ],
        "full_ba_analysis": response_text,
        "user_needs": sections["user_needs"],
        "functional_requirements": sections["functional_requirements"],
        "non_functional_requirements": sections["non_functional_requirements"],
        "user_stories": sections["user_stories"],
        "current_phase": "ba_complete",
    }
