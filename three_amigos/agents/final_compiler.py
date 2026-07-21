"""Final Compiler — Phase 7: compile the comprehensive report.

Assembles all artefacts (user needs, requirements, stories, discussion
history) into a single polished Markdown document.
"""

from three_amigos.States.state import ThreeAmigosState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from three_amigos.agents._common import _stream_llm, _save_output, load_prompt


def compile_final_output(state: ThreeAmigosState) -> dict:
    """Phase 7 — Compile all artefacts into a comprehensive Markdown report."""
    system_prompt = load_prompt("final_compiler.md")

    context = (
        f"## Original User Research\n\n{state['user_research']}\n\n"
        f"## Extracted User Needs\n\n{state.get('extracted_user_needs', '')}\n\n"
        f"## Functional Requirements\n\n{state.get('functional_requirements', '')}\n\n"
        f"## Non-Functional Requirements\n\n{state.get('non_functional_requirements', '')}\n\n"
        f"## User Stories with Acceptance Criteria\n\n{state.get('user_stories', '')}\n\n"
        f"## Three Amigos Discussion History\n\n"
        + "\n\n".join(state.get("discussion_history") or ["(none)"])
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response_text = _stream_llm(messages, agent_label="FINAL COMPILER")
    _save_output(state, "final_report", response_text, title="Final Requirements Report")
    print("📄  Final requirements report compiled.")

    return {
        "messages": [
            AIMessage(content=f"[FINAL OUTPUT]\n{response_text}")
        ],
        "final_output": response_text,
        "current_phase": "complete",
    }
