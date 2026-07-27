import os
import json
from pathlib import Path
from typing import cast
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain.tools import tool
from deepagents import create_deep_agent,FilesystemPermission
from deepagents.backends import FilesystemBackend

from plan_and_execute._common_ import llm, load_prompt
from plan_and_execute.local_states._state_ import AgentState
from plan_and_execute.local_states.planner_state import PlanOutput
from global_layer.functions import token_counter

ROOT_DIR = r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\plan_and_execute\outputs"
__all__ = ["generate_plan"]

@tool
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

    # 1. Initialize your Deep Agent instance (or construct it if pre-configured)
    # Deep agents typically manage their own internal thinking loop or tools
    deep_agent = create_deep_agent(
        model=llm,
        response_format=PlanOutput,  # Enforce structured Pydantic schema
        system_prompt=system_prompt,
        backend=FilesystemBackend(root_dir=ROOT_DIR),
        permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/**"],
            mode="allow",
        ),
    ],
    )

    messages = [
        {"role":"user","content": f"Raw Input Requirements Document:\n{input_text}"}
    ]

    # 2. Invoke the deep agent loop
    result = deep_agent.invoke({"messages": messages})

    # in_tokens, out_tokens, tot_tokens = token_counter(result, "Planner")
    # output_dir = state.get("output_dir", "outputs")
    print(result)


    # return {
    #     "plan_output": plan.model_dump(),
    #     "input_tokens": in_tokens,
    #     "output_tokens": out_tokens,
    #     "total_tokens": tot_tokens,
    #     "messages": [
    #         AIMessage(
    #             content=(
    #                 f"[Planner Agent] Created Requirements Engineering Plan:\n"
    #                 f"- Project Summary: {plan.project_summary[:100]}...\n"
    #                 f"- Total RE Steps: {len(plan.steps)}\n"
    #                 f"[Tokens: {in_tokens} in / {out_tokens} out]"
    #             )
    #         )
    #     ],
    # }
