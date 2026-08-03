"""Single Agent 2 — CLI Runner with Live Token Streaming and Tool Call Arguments (using create_agent).

Usage:
    python -m single_agent_2.run --output-dir single_agent_2_outputs -tid "sa2_1"
"""

import argparse
import sys, json
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain.agents.middleware.types import _InputAgentState
import textwrap

from global_layer.functions import _data_file
from single_agent._common_ import _session_dir, save_state
from single_agent.main import create_agent_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Single Agent 2 CLI Runner with Live Streaming & Tool Call Arguments")
    parser.add_argument("--output-dir", "-o", type=str, default="single_agent_2_outputs", help="Output directory path.")
    parser.add_argument("--thread-id", "-tid", type=str, default="sa2_1", help="Thread ID for graph checkpointing.")
    args = parser.parse_args()

    config: RunnableConfig = {
        "configurable": {"thread_id": args.thread_id},
        "recursion_limit": 50,
    }

    out_dir = _session_dir(args.output_dir)
    raw_input = _data_file()

    print("=======================================================")
    print("Launching single_agent_2 (Live Token & Tool Arguments Streaming)...")
    print(f"Output Directory: {out_dir}")
    print("=======================================================\n")

    pipeline = create_agent_pipeline()

    instruction = (
        f"Target Output Directory: '{out_dir}'\n\n"
        f"Raw Operational Requirements Document:\n{raw_input}\n\n"
        f"GOAL: Autonomously analyze the raw research and generate all BA and IxD deliverables into '{out_dir}' including:\n"
        f"1. Functional Requirements (03_functional_requirements.md)\n"
        f"2. Non-Functional Requirements (04_non_functional_requirements.md)\n"
        f"3. User Stories with Acceptance Criteria (05_user_stories.md)\n"
        f"4. Interactive HTML Mockup files in the 'html/' subfolder (save_html_mockup)\n"
        f"5. UI Mockups and Interaction Design Report (06_ui_mockups.md)\n"
        f"6. Deliverables Summary Index (INDEX.md)"
    )

    initial_state:_InputAgentState = {
        "messages": [HumanMessage(content=instruction)],
    }

    print("\n--- Live Stream (Token-by-Token & Tool Arguments) ---")
   
    stream = pipeline.stream_events(
           initial_state,
           config = config,
           version ="v3"
       )
   
    for kind, item in stream.interleave("messages", "tool_calls"):
        if kind == "messages":
            for token in item.text:
                print(token, end="", flush=True)
            for token in item.reasoning:
                print(f"[thinking] {token}", end="")
        elif kind == "tool_calls":
            print(f"\nTool call: {item.tool_name}({textwrap.shorten(str(item.input), width=100, placeholder='...')})")
            for delta in item.output_deltas:
                print(delta, end="", flush=True)
            print(f"\nTool result: {item.output}")

    final_state = stream.output  
    state_snapshot = pipeline.get_state(config)
    final_values = state_snapshot.values
    print("\n--- End of Live Stream ---\n")

    state_snapshot = pipeline.get_state(config)
    final_values = state_snapshot.values

    tot_in, tot_out = 0, 0
    for msg in final_values.get("messages", []):
        usage = getattr(msg, "usage_metadata", {}) or {}
        tot_in += usage.get("input_tokens", 0)
        tot_out += usage.get("output_tokens", 0)

    print("=======================================================")
    print("single_agent_2 Execution Finished!")
    print(f"- Output Directory: {out_dir}")
    print("\nTotal Accumulated Token Usage:")
    print(f"- Total Input Tokens:  {tot_in}")
    print(f"- Total Output Tokens: {tot_out}")
    print(f"- Total Tokens:        {tot_in + tot_out}")
    print("=======================================================\n")

    save_state({
        "output_dir": out_dir,
        "input_tokens": tot_in,
        "output_tokens": tot_out,
        "total_tokens": tot_in + tot_out,
        "messages": [m.content for m in final_values.get("messages", []) if hasattr(m, "content")],
    })


if __name__ == "__main__":
    main()
