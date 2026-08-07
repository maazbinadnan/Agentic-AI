"""Business Analyst Subagent — Uses langchain.create_agent to generate BA deliverables and handle feedback revisions.

Generates the requirements files as in single_agent (01_user_needs.md, 02_functional_requirements.md,
03_non_functional_requirements.md, 04_user_stories.md, 05_analysis_summary.md) and can take feedback
to revise/patch them.
"""

from pathlib import Path
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.middleware.types import _InputAgentState
from langgraph.graph.state import CompiledStateGraph
import os
from dotenv import load_dotenv
load_dotenv()

from review_critique._common_ import llm, load_prompt,save_state
from global_layer.functions import _data_file
from global_layer.llm_client import get_llm

eval_llm = get_llm(model=os.environ['EVAL_MODEL'])

__all__ = ["run_business_analyst"]


@tool
def save_report_file(filename: str, report_markdown: str, output_dir: str = "outputs") -> str:
    """Saves a formal Markdown report deliverable directly into output_dir.

    Expected filenames include:
    - '01_user_needs.md'
    - '02_functional_requirements.md'
    - '03_non_functional_requirements.md'
    - '04_user_stories.md'
    - '05_analysis_summary.md'
    - '06_review_summary.md'

    Parameters
    ----------
    filename : str
        Target report filename (e.g. '01_user_needs.md' or '04_user_stories.md').
    report_markdown : str
        The complete markdown text content of the report.
    output_dir : str
        Target output directory path.
    iteration_num : int, optional
        Optional iteration number for backward compatibility.
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / filename
    file_path.write_text(report_markdown, encoding="utf-8")
    
    print(f"\n[Business Analyst Subagent] Successfully saved deliverable '{filename}' to '{file_path.resolve()}'")
    return f"Successfully saved '{filename}' to '{file_path.resolve()}'"


@tool
def read_file(filename: str, output_dir: str) -> str:
    """Reads a report deliverable file directly from output_dir to inspect existing content when revising based on feedback.

    Parameters
    ----------
    filename : str
        Name of the file to read (e.g. '01_user_needs.md').
    output_dir : str
        Target output directory path.
    iteration_num : int, optional
        Optional iteration number for backward compatibility.
    """
    file_path = Path(output_dir) / filename
    if not file_path.exists():
        # Fallback recursive search if file is in a nested directory
        if Path(output_dir).exists():
            matches = sorted(list(Path(output_dir).rglob(filename)))
            if matches:
                return matches[-1].read_text(encoding="utf-8")
        if Path(filename).exists():
            return Path(filename).read_text(encoding="utf-8")
        return f"File '{filename}' not found in directory '{output_dir}'."
    return file_path.read_text(encoding="utf-8")


def _stream_agent(agent: CompiledStateGraph, prompt_text: str, config: RunnableConfig, role_name: str) -> tuple[str, int, int]:
    """Streams token-by-token text output and tool calls for an agent run, returning captured text and token counts for new messages."""
    state_before = agent.get_state(config)
    prev_msg_count = len(state_before.values.get("messages", [])) if (state_before and state_before.values) else 0

    print(f"\n\n==========================================")
    print(f"[{role_name}]")
    print(f"==========================================")
    stream = agent.stream_events({"messages": [HumanMessage(content=prompt_text)]}, config=config, version="v3")
    full_text = ""
    for kind, item in stream.interleave("messages", "tool_calls"):
        if kind == "messages":
            for token in item.text:
                print(token, end="", flush=True)
                full_text += token
    print()
    state_snapshot = agent.get_state(config)
    final_values = state_snapshot.values if state_snapshot else {}

    # Accumulate token metrics ONLY for new messages generated in this turn
    all_messages = final_values.get("messages", [])
    new_messages = all_messages[prev_msg_count:]

    tot_in, tot_out = 0, 0
    for msg in new_messages:
        usage = getattr(msg, "usage_metadata", {}) or {}
        tot_in += usage.get("input_tokens", 0)
        tot_out += usage.get("output_tokens", 0)

    print(f"turn input tokens: {tot_in}")
    print(f"turn output tokens: {tot_out}")
    print(f"turn total tokens: {tot_in + tot_out}")

    return full_text, tot_in, tot_out



def define_agents():

    # Combine the base Lead BA prompt with single-agent file-saving and feedback instructions
    business_analyst_prompt = load_prompt("business_analyst.md")
    critique_prompt = load_prompt("ba_critique.md")
    checkpointer = InMemorySaver()

    business_analyst_subagent = create_agent(
        model=llm,
        checkpointer=checkpointer,
        tools=[save_report_file, read_file],
        system_prompt=business_analyst_prompt,
        name="Business_Analyst_Subagent",
    )

    # critique sub-agent
    critique_subagent = create_agent(
        model=eval_llm,
        checkpointer=checkpointer,
        tools=[save_report_file, read_file],
        system_prompt=critique_prompt,
        name="Critique_Subagent",
    )

    return business_analyst_subagent,critique_subagent




def run_business_analyst(task: str, max_rounds: int = 3, thread_id: str = "ba_reflect_1", output_dir: str = "outputs") -> dict:
    """Generates an initial draft with Business Analyst, then iteratively critiques and improves it in-place."""

    ba, critic = define_agents()
    gen_config: RunnableConfig = {"configurable": {"thread_id": f"{thread_id}_gen"}}
    critique_config: RunnableConfig = {"configurable": {"thread_id": f"{thread_id}_critique"}}

    gen_in, gen_out = 0, 0
    eval_in, eval_out = 0, 0

    # Iteration 1: Initial draft
    first_prompt = (
        f"Target Output Directory: '{output_dir}'\n"
        f"Task: {task}\n"
        f"into '{output_dir}' using save_report_file."
    )
    _, t_in, t_out = _stream_agent(ba, first_prompt, gen_config, "Initial Business Analyst Draft")
    gen_in += t_in
    gen_out += t_out

    # Reflection loop
    for round_num in range(1, max_rounds + 1):
        critique_prompt_msg = (
            f"Target Output Directory: '{output_dir}'\n"
            f"Task: {task}\n"
            f"Draft to review: Inspect all generated requirements files (01_user_needs.md to 05_analysis_summary.md) in '{output_dir}' using read_file.\n"
            f"NOTE: Focus exclusively on Business Analysis deliverables. HTML mockups and UI code are OUT OF SCOPE for this review (handled downstream by Interaction Designer).\n\n"
            f"Evaluate the files against the checklist and save your evaluation to "
            f"'06_review_summary.md' directly in '{output_dir}' using save_report_file."
        )
        critique_text, c_in, c_out = _stream_agent(critic, critique_prompt_msg, critique_config, f"Round {round_num}: Quality Review")
        eval_in += c_in
        eval_out += c_out

        if "approved" in critique_text.lower():
            print(f"APPROVED AFTER REVISION ROUND {round_num}")
            break

        # Revision step
        revise_prompt_msg = (
            f"Target Output Directory: '{output_dir}'\n"
            f"Task: {task}\n"
            f"Please read '06_review_summary.md' in '{output_dir}' using read_file and revise the requirements deliverables "
            f"to resolve all identified issues.\n\n"
            f"CRITICAL INSTRUCTIONS:\n"
            f"1. You MUST invoke save_report_file to update all affected deliverable files directly in '{output_dir}'.\n"
            f"2. DO NOT just reply with text explanations without invoking save_report_file for each modified file."
        )
        _, r_in, r_out = _stream_agent(ba, revise_prompt_msg, gen_config, f"Round {round_num}: Business Analyst Revision")
        gen_in += r_in
        gen_out += r_out

    print(f"\nExecution complete. Final deliverables available in '{output_dir}'.")

    gen_model = getattr(llm, "model_name", getattr(llm, "model", "default"))
    eval_model = getattr(eval_llm, "model_name", getattr(eval_llm, "model", "gpt-5.4"))

    return {
        "generator_model": gen_model,
        "generator_input_tokens": gen_in,
        "generator_output_tokens": gen_out,
        "generator_total_tokens": gen_in + gen_out,
        "eval_model": eval_model,
        "eval_input_tokens": eval_in,
        "eval_output_tokens": eval_out,
        "eval_total_tokens": eval_in + eval_out,
    }

