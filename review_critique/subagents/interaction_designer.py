"""Interaction Designer Subagent — Uses langchain.create_agent to generate IxD deliverables and handle feedback revisions.

Generates HTML UI mockups and interaction design deliverables (07_ui_mockups_and_interaction_design.md) and can take feedback
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
import textwrap


from review_critique._common_ import llm, load_prompt, _session_dir, _outputs_dir
from global_layer.functions import _data_file
from global_layer.llm_client import get_llm

eval_llm = get_llm(model=os.environ['EVAL_MODEL'])

__all__ = ["run_interaction_designer"]

@tool
def save_report_file(filename: str, report_markdown: str, output_dir: str = "outputs") -> str:
    """Saves a formal Markdown report deliverable directly into output_dir.

    Expected filenames include:
    - '07_ui_mockups_and_interaction_design.md'
    - '08_ixd_review_summary.md'

    Parameters
    ----------
    filename : str
        Target report filename (e.g. '07_ui_mockups_and_interaction_design.md').
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
    
    print(f"\n[Interaction Designer] Successfully saved deliverable '{filename}' to '{file_path.resolve()}'")
    return f"Successfully saved '{filename}' to '{file_path.resolve()}'"


@tool
def save_html_mockup(filename: str, html_content: str, output_dir: str = "outputs") -> str:
    """Saves an HTML mockup file directly into output_dir/html/.

    Parameters
    ----------
    filename : str
        Name of HTML file (e.g. 'login.html', 'dashboard.html').
    html_content : str
        The complete HTML/CSS mockup content.
    output_dir : str
        Target output directory path.
    """
    out_path = Path(output_dir) / "html"
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / filename
    file_path.write_text(html_content, encoding="utf-8")
    
    print(f"\n[Interaction Designer] Successfully saved HTML mockup '{filename}' to '{file_path.resolve()}'")
    return f"Successfully saved HTML mockup '{filename}' to '{file_path.resolve()}'"


@tool
def read_file(filename: str, output_dir: str = "outputs") -> str:
    """Reads a report deliverable file directly from output_dir to inspect existing content when revising based on feedback.

    Parameters
    ----------
    filename : str
        Name of the file to read (e.g. '04_user_stories.md').
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


@tool
def read_html_files(filename: str,output_dir: str = "outputs") -> str:
    """Reads HTML mockup files directly from output_dir/html/.

    If filename is specified (e.g., 'login.html'), reads that specific HTML file.
    If filename is omitted or None, lists and reads all HTML mockup files located in output_dir/html/.

    Parameters
    ----------
    output_dir : str
        Target output directory path.
    filename : str, optional
        Specific HTML mockup filename to read (e.g. 'login.html'). If omitted, reads all HTML mockups.
    """
    html_dir = Path(output_dir) / "html"
    if not html_dir.exists():
        if Path(output_dir).exists():
            html_files = sorted(list(Path(output_dir).rglob("*.html")))
            if html_files:
                combined = []
                for hf in html_files:
                    combined.append(f"=== File: {hf.name} ===\n{hf.read_text(encoding='utf-8')}")
                return "\n\n".join(combined)
        return f"No HTML mockup files found in '{html_dir.resolve()}'."

    if filename:
        file_path = html_dir / filename
        if not file_path.exists():
            return f"HTML file '{filename}' not found in '{html_dir.resolve()}'."
        return file_path.read_text(encoding="utf-8")

    html_files = sorted(list(html_dir.glob("*.html")))
    if not html_files:
        return f"No HTML mockup files found in '{html_dir.resolve()}'."

    combined = []
    for hf in html_files:
        combined.append(f"=== File: html/{hf.name} ===\n{hf.read_text(encoding='utf-8')}")

    return "\n\n".join(combined)


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
    ixd_prompt = load_prompt("ixd.md")
    critique_prompt = load_prompt("ixd_critique.md")
    checkpointer = InMemorySaver()

    ixd_subagent = create_agent(
        model=llm,
        checkpointer=checkpointer,
        tools=[save_report_file, save_html_mockup, read_file, read_html_files],
        system_prompt=ixd_prompt,
        name="Interaction_Designer_Subagent",
    )

    ixd_critique_subagent = create_agent(
        model=eval_llm,
        checkpointer=checkpointer,
        tools=[save_report_file, read_file, read_html_files],
        system_prompt=critique_prompt,
        name="IxD_Critique_Subagent",
    )

    return ixd_subagent, ixd_critique_subagent


def run_interaction_designer(task: str, max_rounds: int = 3, thread_id: str = "ixd_reflect_1", output_dir: str = "outputs") -> dict:
    """Generates initial HTML mockups & design report with Interaction Designer, then iteratively critiques and improves in-place."""

    ixd, critic = define_agents()
    gen_config: RunnableConfig = {"configurable": {"thread_id": f"{thread_id}_gen"}}
    critique_config: RunnableConfig = {"configurable": {"thread_id": f"{thread_id}_critique"}}

    gen_in, gen_out = 0, 0
    eval_in, eval_out = 0, 0

    # Iteration 1: Initial IxD draft
    first_prompt = (
        f"Target Output Directory: '{output_dir}'\n"
        f"Task: {task}\n"
        f"Critique: (none — first draft)\n\n"
        f"CRITICAL REQUIREMENT: Inspect requirements files ('04_user_stories.md', '02_functional_requirements.md') "
        f"in '{output_dir}' using read_file, generate HTML mockup files using save_html_mockup, "
        f"and save the Interaction Design Report '07_ui_mockups_and_interaction_design.md' into '{output_dir}' using save_report_file."
    )
    _, t_in, t_out = _stream_agent(ixd, first_prompt, gen_config, "Initial Interaction Designer Draft")
    gen_in += t_in
    gen_out += t_out

    # Reflection loop
    for round_num in range(1, max_rounds + 1):
        critique_prompt_msg = (
            f"Target Output Directory: '{output_dir}'\n"
            f"Task: {task}\n"
            f"Draft to review: Inspect all generated HTML mockups in '{output_dir}/html' using read_html_files, "
            f"and read '07_ui_mockups_and_interaction_design.md' using read_file.\n\n"
            f"Evaluate against the checklist and save your evaluation to '08_ixd_review_summary.md' in '{output_dir}' using save_report_file."
        )

        critique_text, c_in, c_out = _stream_agent(critic, critique_prompt_msg, critique_config, f"Round {round_num}: IxD Quality Review")
        eval_in += c_in
        eval_out += c_out

        if "approved" in critique_text.lower():
            print(f"APPROVED AFTER REVISION ROUND {round_num} since critique text was {critique_text}")
            break

        # Revision step
        revise_prompt_msg = (
            f"Target Output Directory: '{output_dir}'\n"
            f"Task: {task}\n"
            f"Please read '08_ixd_review_summary.md' in '{output_dir}' using read_file and revise the HTML mockups and design report "
            f"to resolve all identified issues.\n\n"
            f"CRITICAL INSTRUCTIONS:\n"
            f"1. You MUST invoke save_html_mockup and save_report_file to update all affected deliverables directly in '{output_dir}'.\n"
            f"2. DO NOT just reply with text explanations without invoking save tools for each modified file."
        )
        _, r_in, r_out = _stream_agent(ixd, revise_prompt_msg, gen_config, f"Round {round_num}: Interaction Designer Revision")
        gen_in += r_in
        gen_out += r_out

    print(f"\nExecution complete. Final IxD deliverables available in '{output_dir}'.")

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

