"""Three Amigos Multi-Agent System — Node Functions & Routing Logic.

Contains all LangGraph node functions for the requirements engineering
workflow, plus conditional-edge routing helpers.

Architecture
────────────
  Supervisor → Elicitation ⇄ Human Clarification
    → Requirements Engineer → Story Writer
    → PO Review → Dev Review → QA Review → Consensus Check ⇄ (loop)
    → Human Review → Final Compiler
"""

from three_amigos.States.state import ThreeAmigosState
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.types import interrupt
from dotenv import load_dotenv
import os

load_dotenv()


# ─── LLM Client ─────────────────────────────────────────────────────────────
def get_llm(
    model: str | None = None,
    temperature: float = 0,
) -> ChatOpenAI:
    """Create a ChatOpenAI instance using the project's OpenAI-compatible endpoint.

    Reads ``AZURE_OPENAI_ENDPOINT`` and ``AZURE_OPENAI_API_KEY`` from the
    environment (same variables used by the existing ``Global_Client_Layer``).
    The model defaults to ``gpt-4o-mini`` but can be overridden via the
    ``THREE_AMIGOS_MODEL`` env-var or the *model* parameter.
    """
    model = model or os.getenv("THREE_AMIGOS_MODEL", "gpt-4o-mini")
    return ChatOpenAI(
        base_url=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        model=model,
        temperature=temperature,
    )


# Module-level singleton — reused across all node calls
llm = get_llm()


# ─── Prompt Loader ───────────────────────────────────────────────────────────
PROMPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Prompts")


def load_prompt(prompt_name: str) -> str:
    """Load a prompt template from the ``Prompts/`` directory."""
    prompt_path = os.path.join(PROMPTS_DIR, prompt_name)
    with open(prompt_path, "r", encoding="utf-8") as fh:
        return fh.read()


# ═══════════════════════════════════════════════════════════════════════════════
#  NODE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════


def supervisor_agent(state: ThreeAmigosState) -> dict:
    """Phase 1 — Orchestrator: analyse user research, set the work plan."""
    system_prompt = load_prompt("supervisor.md")
    user_research = state["user_research"]

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(
            content=(
                "Analyse the following user research and provide your "
                "assessment:\n\n"
                f"{user_research}"
            )
        ),
    ]

    response = llm.invoke(messages)
    print("\n✅  Supervisor analysis complete.")

    return {
        "messages": [
            AIMessage(content=f"[SUPERVISOR ANALYSIS]\n{response.content}")
        ],
        "current_phase": "elicitation",
    }


# ── Elicitation ──────────────────────────────────────────────────────────────


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

    response = llm.invoke(messages)
    response_text: str = response.content

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


# ── Requirements Engineering ─────────────────────────────────────────────────


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

    response = llm.invoke(messages)
    response_text: str = response.content

    # Try to split FR / NFR sections for downstream agents
    fr_section = response_text
    nfr_section = response_text

    for heading in ("### Non-Functional Requirements", "## Non-Functional Requirements"):
        if heading in response_text:
            parts = response_text.split(heading, 1)
            fr_section = parts[0]
            nfr_section = heading + parts[1]
            break

    print("\n✅  Functional & non-functional requirements derived.")

    return {
        "messages": [
            AIMessage(content=f"[REQUIREMENTS ENGINEER]\n{response_text}")
        ],
        "functional_requirements": fr_section,
        "non_functional_requirements": nfr_section,
        "current_phase": "requirements",
    }


# ── Story Writing ────────────────────────────────────────────────────────────


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

    response = llm.invoke(messages)
    print("\n✅  User stories with BDD acceptance criteria created.")

    return {
        "messages": [
            AIMessage(content=f"[STORY WRITER]\n{response.content}")
        ],
        "user_stories": response.content,
        "current_phase": "stories",
    }


# ── Three Amigos Reviews ────────────────────────────────────────────────────


def _build_discussion_context(
    state: ThreeAmigosState,
    *,
    include_po: bool = False,
    include_dev: bool = False,
) -> str:
    """Helper: build the context string for a Three Amigos reviewer."""
    round_num = state.get("discussion_round", 0) + 1
    parts = [
        f"## Discussion Round: {round_num}\n",
        f"## Original User Research\n\n{state['user_research']}\n",
        f"## Current User Stories\n\n{state.get('user_stories', '')}\n",
    ]
    if include_po:
        parts.append(f"## Product Owner's Feedback\n\n{state.get('po_feedback', '')}\n")
    if include_dev:
        parts.append(f"## Developer's Feedback\n\n{state.get('dev_feedback', '')}\n")

    history = state.get("discussion_history") or []
    if history:
        parts.append(
            "## Previous Discussion History\n\n"
            + "\n\n---\n\n".join(history)
        )
    return "\n".join(parts)


def product_owner_review(state: ThreeAmigosState) -> dict:
    """Three Amigos — Product Owner / BA perspective."""
    system_prompt = load_prompt("product_owner.md")
    round_num = state.get("discussion_round", 0) + 1
    context = _build_discussion_context(state)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response = llm.invoke(messages)
    print(f"\n🧑‍💼  Product Owner review complete (round {round_num}).")

    return {
        "messages": [
            AIMessage(
                content=f"[PRODUCT OWNER — Round {round_num}]\n{response.content}"
            )
        ],
        "po_feedback": response.content,
    }


def developer_review(state: ThreeAmigosState) -> dict:
    """Three Amigos — Developer / Architect perspective."""
    system_prompt = load_prompt("developer.md")
    round_num = state.get("discussion_round", 0) + 1
    context = _build_discussion_context(state, include_po=True)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response = llm.invoke(messages)
    print(f"\n👩‍💻  Developer review complete (round {round_num}).")

    return {
        "messages": [
            AIMessage(
                content=f"[DEVELOPER — Round {round_num}]\n{response.content}"
            )
        ],
        "dev_feedback": response.content,
    }


def qa_review(state: ThreeAmigosState) -> dict:
    """Three Amigos — QA Engineer perspective."""
    system_prompt = load_prompt("qa_engineer.md")
    round_num = state.get("discussion_round", 0) + 1
    context = _build_discussion_context(state, include_po=True, include_dev=True)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response = llm.invoke(messages)
    print(f"\n🧪  QA Engineer review complete (round {round_num}).")

    return {
        "messages": [
            AIMessage(
                content=f"[QA ENGINEER — Round {round_num}]\n{response.content}"
            )
        ],
        "qa_feedback": response.content,
    }


# ── Consensus Check ──────────────────────────────────────────────────────────


def check_consensus(state: ThreeAmigosState) -> dict:
    """Evaluate Three Amigos feedback; refine stories if no consensus."""
    system_prompt = load_prompt("consensus_checker.md")
    round_num = state.get("discussion_round", 0) + 1

    context = (
        f"## Round {round_num} Discussion Summary\n\n"
        f"## Current User Stories\n\n{state.get('user_stories', '')}\n\n"
        f"## Product Owner Feedback\n\n{state.get('po_feedback', '')}\n\n"
        f"## Developer Feedback\n\n{state.get('dev_feedback', '')}\n\n"
        f"## QA Engineer Feedback\n\n{state.get('qa_feedback', '')}"
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    response = llm.invoke(messages)
    response_text: str = response.content

    consensus = "CONSENSUS: YES" in response_text.upper()

    # Append a round summary to the discussion history
    round_summary = (
        f"### Round {round_num}\n"
        f"**PO highlights:** {state.get('po_feedback', '')[:400]}…\n\n"
        f"**Dev highlights:** {state.get('dev_feedback', '')[:400]}…\n\n"
        f"**QA highlights:** {state.get('qa_feedback', '')[:400]}…\n\n"
        f"**Consensus:** {'✅ Reached' if consensus else '❌ Not reached'}\n"
    )
    history = list(state.get("discussion_history") or [])
    history.append(round_summary)

    # Extract refined / final stories from the response
    updated_stories = state.get("user_stories", "")
    for marker in ("### Refined User Stories", "### Final User Stories"):
        if marker in response_text:
            parts = response_text.split(marker, 1)
            if len(parts) > 1:
                updated_stories = marker + parts[1]
            break

    status = "✅  Consensus reached!" if consensus else f"🔄  Round {round_num} — no consensus; refining…"
    print(f"\n{status}")

    return {
        "messages": [
            AIMessage(
                content=f"[CONSENSUS CHECK — Round {round_num}]\n{response_text}"
            )
        ],
        "consensus_reached": consensus,
        "discussion_round": round_num,
        "discussion_history": history,
        "user_stories": updated_stories,
        "current_phase": "consensus_check",
    }


# ── Human Review ─────────────────────────────────────────────────────────────


def human_review_node(state: ThreeAmigosState) -> dict:
    """Interrupt: pause for the human to approve or request revisions."""
    user_stories = state.get("user_stories", "")
    fr = state.get("functional_requirements", "")
    nfr = state.get("non_functional_requirements", "")
    discussion_round = state.get("discussion_round", 0)

    review_summary = (
        f"## Three Amigos Discussion Complete  (Round {discussion_round})\n\n"
        f"### Functional Requirements\n\n{fr}\n\n"
        f"### Non-Functional Requirements\n\n{nfr}\n\n"
        f"### User Stories with Acceptance Criteria\n\n{user_stories}\n\n"
        "---\n\n"
        "**Please review and respond with:**\n"
        "- Type **APPROVED** to accept these requirements.\n"
        "- Or provide specific feedback for further refinement.\n"
    )

    human_response = interrupt(
        {
            "type": "review",
            "summary": review_summary,
            "message": (
                "The Three Amigos discussion is complete. "
                "Please review the output above."
            ),
        }
    )

    approved = "APPROVED" in str(human_response).upper()

    result: dict = {
        "messages": [
            HumanMessage(content=f"[HUMAN REVIEW]\n{human_response}")
        ],
        "human_approved": approved,
    }

    if not approved:
        # Feed human feedback into the next discussion round
        result["po_feedback"] = f"Human reviewer feedback: {human_response}"

    return result


# ── Final Compilation ────────────────────────────────────────────────────────


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

    response = llm.invoke(messages)
    print("\n📄  Final requirements report compiled.")

    return {
        "messages": [
            AIMessage(content=f"[FINAL OUTPUT]\n{response.content}")
        ],
        "final_output": response.content,
        "current_phase": "complete",
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  ROUTING FUNCTIONS  (used as conditional-edge selectors)
# ═══════════════════════════════════════════════════════════════════════════════


def route_clarification(state: ThreeAmigosState) -> str:
    """Does the elicitation agent need human clarification?"""
    if state.get("needs_clarification", False):
        return "needs_clarification"
    return "proceed"


def route_consensus(state: ThreeAmigosState) -> str:
    """Have the Three Amigos reached consensus, or should they loop?"""
    max_rounds = state.get("max_discussion_rounds", 3)
    current_round = state.get("discussion_round", 0)
    consensus = state.get("consensus_reached", False)

    if consensus or current_round >= max_rounds:
        return "review"
    return "continue_discussion"


def route_human_approval(state: ThreeAmigosState) -> str:
    """Did the human approve the output?"""
    if state.get("human_approved", False):
        return "approved"
    return "revise"
