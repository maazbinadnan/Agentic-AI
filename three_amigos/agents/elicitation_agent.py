"""Elicitation Agent — Phase 2: extract structured user needs.

Also contains the ``human_clarification_node`` interrupt point that
allows the human to answer ambiguity questions raised by this agent.
"""

from three_amigos.States.state import ThreeAmigosState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.types import interrupt

from three_amigos.agents._common import _stream_llm, _save_output, load_prompt


def elicitation_agent(state: ThreeAmigosState) -> dict:
    """Phase 2 — Extract structured user needs; flag ambiguities."""
    system_prompt = load_prompt("elicitation.md")
    user_research = state["user_research"]

    # Build context — include any prior human clarification responses
    context = f"## User Research\n\n{user_research}"

    prior_messages = state.get("messages") or []
    clarification_responses = [
        m.content
        for m in prior_messages
        if isinstance(m, HumanMessage)
        and "[CLARIFICATION RESPONSE]" in m.content
    ]
    if clarification_responses:
        context += (
            "\n\n## Clarification Responses from User\n\n"
            + "\n\n".join(clarification_responses)
        )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response_text = _stream_llm(messages, agent_label="ELICITATION")

    # Determine whether the agent flagged ambiguities
    needs_clarification = "CLARIFICATION_NEEDED: YES" in response_text.upper()

    # Parse out clarification questions (if any)
    clarification_questions = ""
    if needs_clarification and "### Clarification Questions" in response_text:
        parts = response_text.split("### Clarification Questions", 1)
        if len(parts) > 1:
            # Grab everything up to the next heading
            q_section = parts[1].split("\n###")[0].strip()
            clarification_questions = q_section

    status = "⚠️  Clarification needed" if needs_clarification else "✅  User needs extracted"
    _save_output(state, "extracted_user_needs", response_text, title="Extracted User Needs")
    print(f"\n{status}")

    return {
        "messages": [
            AIMessage(content=f"[ELICITATION AGENT]\n{response_text}")
        ],
        "extracted_user_needs": response_text,
        "needs_clarification": needs_clarification,
        "clarification_questions": clarification_questions,
        "current_phase": "elicitation",
    }


def human_clarification_node(state: ThreeAmigosState) -> dict:
    """Interrupt: pause for the human to answer clarification questions."""
    questions = state.get("clarification_questions", "No specific questions.")

    human_response = interrupt(
        {
            "type": "clarification",
            "questions": questions,
            "message": (
                "The elicitation agent has identified ambiguities in the "
                "user research.  Please answer the following questions:"
            ),
        }
    )

    return {
        "messages": [
            HumanMessage(content=f"[CLARIFICATION RESPONSE]\n{human_response}")
        ],
        "needs_clarification": False,
    }
