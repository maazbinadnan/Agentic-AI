import os
import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage, AIMessage

from plan_and_execute._common_ import llm, load_prompt
from plan_and_execute.local_states._state_ import AgentState
from plan_and_execute.local_states.planner_state import PlanOutput
from global_layer.functions import token_counter

__all__ = ["generate_plan"]


def _save_plan_markdown(plan: PlanOutput, output_dir: str):
    """Saves the generated execution plan to 00_plan.md inside output_dir."""
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / "00_plan.md"

    lines = [
        "# Execution Plan (Plan-and-Execute Architecture)\n",
        f"## Executive Project Summary\n{plan.project_summary}\n",
        f"## RE Execution Strategy\n{plan.execution_strategy}\n",
        "---\n",
        "## Requirements Engineering Process Lifecycle Plan (DAG)\n",
    ]

    for step in plan.steps:
        deps = ", ".join(step.dependencies) if step.dependencies else "None (Initial Step)"
        lines.append(f"### {step.step_id}: {step.title}")
        lines.append(f"- **RE Lifecycle Phase:** `{step.re_phase}`")
        lines.append(f"- **Target Deliverable:** `{step.target_deliverable}`")
        lines.append(f"- **Dependencies:** {deps}")
        lines.append(f"- **Task Description:** {step.task_description}\n")

    file_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[Planner Agent] Saved execution plan to '{file_path.resolve()}'")


def generate_plan(state: AgentState):
    print("[Plan-and-Execute] Planner Agent generating dynamic execution plan...")

    system_prompt = load_prompt("planner.md")
    input_text = state.get("input", "")

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Raw Input Requirements Document:\n{input_text}"),
    ]

    structured_llm = llm.with_structured_output(PlanOutput, include_raw=True)
    response = structured_llm.invoke(messages)

    if isinstance(response, dict):
        plan = cast(PlanOutput, response["parsed"])
        in_tokens, out_tokens, tot_tokens = token_counter(response, "Planner")
    else:
        plan = cast(PlanOutput, response)
        in_tokens, out_tokens, tot_tokens = 0, 0, 0

    output_dir = state.get("output_dir", "outputs")
    _save_plan_markdown(plan, output_dir)

    return {
        "plan_output": plan.model_dump(),
        "input_tokens": in_tokens,
        "output_tokens": out_tokens,
        "total_tokens": tot_tokens,
        "messages": [
            AIMessage(
                content=(
                    f"[Planner Agent] Created Requirements Engineering Plan:\n"
                    f"- Project Summary: {plan.project_summary[:100]}...\n"
                    f"- Total RE Steps: {len(plan.steps)}\n"
                    f"[Tokens: {in_tokens} in / {out_tokens} out]"
                )
            )
        ],
    }
