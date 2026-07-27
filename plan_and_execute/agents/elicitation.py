import os
import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.types import interrupt

from plan_and_execute._common_ import llm, load_prompt
from plan_and_execute.local_states._state_ import AgentState
from plan_and_execute.local_states.elicitation_state import ElicitationOutput
from global_layer.functions import token_counter


__all__ = ["generate_elicitation", "ask_human"]


def _save_elicitation_markdown(result: ElicitationOutput, user_answers: dict, output_dir: str):
    """Saves elicitation output and user clarifications to 01_elicitation.md inside output_dir."""
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / "01_elicitation.md"

    lines = [
        "# Requirements Elicitation Report\n",
        "## 1. Discovered Target Personas\n",
    ]

    for p in result.personas:
        lines.append(f"### {p.name} ({p.user_group_type})")
        lines.append(f"{p.description}\n")

    lines.append("## 2. High-Level User Needs\n")
    for un in result.user_needs:
        lines.append(f"### {un.id}: {un.user_need}")
        lines.append(f"- **Target User Group :** {un.id}: {un.user_group_type}")
        lines.append(f"- **Target Persona:** {un.user_group}")
        lines.append(f"- **User Journey Context:** {un.user_journey}\n")
        lines.append(f"- **User Need Demand:** {un.demand}\n")

    if result.questions:
        lines.append("## 3. Elicitation Clarifying Questions & Stakeholder Responses\n")
        for q in result.questions:
            ans = user_answers.get(q.id, "No response provided (Default assumptions applied).")
            lines.append(f"### Question [{q.id}] - Topic: {q.topic}")
            lines.append(f"- **Context / Reason:** {q.context_reason}")
            lines.append(f"- **Question Posed:** {q.question}")
            lines.append(f"- **Stakeholder Answer:** *{ans}*\n")

    file_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[Elicitation Agent] Saved report to '{file_path.resolve()}'")


def generate_elicitation(state: AgentState):
    print("[Plan-and-Execute] Elicitation Agent extracting personas, user needs, and clarifying questions...")

    system_prompt = load_prompt("elicitation.md")
    input_text = state.get("input", "")
    user_answers = state.get("user_clarifications") or {}

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Raw Requirements Document:\n{input_text}"),
    ]

    structured_llm = llm.with_structured_output(ElicitationOutput, include_raw=True)
    response = structured_llm.invoke(messages)

    if isinstance(response, dict):
        result = cast(ElicitationOutput, response["parsed"])
        in_tokens, out_tokens, tot_tokens = token_counter(response, "Elicitation")
    else:
        result = cast(ElicitationOutput, response)
        in_tokens, out_tokens, tot_tokens = 0, 0, 0

    output_dir = state.get("output_dir", "outputs")
    _save_elicitation_markdown(result, user_answers, output_dir)

    return {
        "elicitation_output": result.model_dump(),
        "input_tokens": in_tokens,
        "output_tokens": out_tokens,
        "total_tokens": tot_tokens,
        "messages": [
            AIMessage(
                content=(
                    f"[Elicitation Agent] Elicited requirements:\n"
                    f"- Personas: {len(result.personas)}\n"
                    f"- User Needs: {len(result.user_needs)}\n"
                    f"- Clarifying Questions: {len(result.questions)}\n"
                    f"[Tokens: {in_tokens} in / {out_tokens} out]"
                )
            )
        ],
    }


def ask_human(state: AgentState):
    """Pure interrupt node: emits all questions in a single interrupt call, returning user answers."""
    elicitation = state.get("elicitation_output") or {}
    questions = elicitation.get("questions", [])

    if not questions:
        print("[Human-In-The-Loop] No clarifying questions generated. Proceeding...")
        return {}

    print(f"[Human-In-The-Loop] Emitting {len(questions)} clarifying question(s) via interrupt...")
    
    # Emit ALL questions at once in a single interrupt
    user_answers = interrupt({
        "type": "clarifying_questions",
        "questions": questions
    })

    print(f"[Human-In-The-Loop] Received user clarifications: {user_answers}")

    # Re-save 01_elicitation.md with updated answers
    if isinstance(elicitation, dict):
        try:
            parsed_elicitation = ElicitationOutput.model_validate(elicitation)
            output_dir = state.get("output_dir", "outputs")
            _save_elicitation_markdown(parsed_elicitation, user_answers, output_dir)
        except Exception as e:
            print(f"[Human-In-The-Loop] Error saving updated elicitation report: {e}")

    # Save to state["user_clarifications"]
    return {"user_clarifications": user_answers}