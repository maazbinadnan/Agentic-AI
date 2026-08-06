"""hitl_agent Module — CLI Runner for Task Dispatcher with Live Token Streaming (using create_agent).

Usage:
    python -m hitl_agent.run --output-dir outputs_ba_agent -tid "dispatcher_1"
"""

import argparse
import textwrap
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain.agents.middleware.types import _InputAgentState
from hitl_agent.tools import SUBAGENTS

from global_layer.functions import _data_file
from hitl_agent._common_ import _session_dir, save_state
from hitl_agent.main import create_agent_pipeline


def main() :
    parser = argparse.ArgumentParser(description="hitl_agent Task Dispatcher CLI Runner with Live Streaming")
    parser.add_argument("--output-dir", "-o", type=str, default="outputs_ba_agent", help="Output directory path.")
    parser.add_argument("--thread-id", "-tid", type=str, default="dispatcher_1", help="Thread ID for graph checkpointing.")
    args = parser.parse_args()

    config: RunnableConfig = {
        "configurable": {"thread_id": args.thread_id},
        "recursion_limit": 50,
    }

    out_dir = _session_dir(args.output_dir)
    raw_input = _data_file()

    print("=======================================================")
    print("Launching hitl_agent (Token-by-Token Live Streaming)...")
    print(f"Sub-Agent Registry: {list(SUBAGENTS.keys())}")
    print(f"Output Directory:   {out_dir}")
    print("=======================================================\n")

    pipeline = create_agent_pipeline()

    instruction = (
        f"Target Output Directory: '{out_dir}'\n\n"
        f"Raw Operational Requirements Document:\n{raw_input}\n\n"
        f"GOAL: Generate a complete Business Analysis deliverables package into '{out_dir}' including:\n"
        f"user stories, functional/non requirements html mockups, the whole suite"
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
            print(f"\nTool call: {item.tool_name}({textwrap.shorten(str(item.input), width=200, placeholder='...')})")
            for delta in item.output_deltas:
                print(delta, end="", flush=True)
            print(f"\nTool result: {textwrap.shorten(str(item.output),width=200,placeholder="...")}")

    final_state = stream.output  
    state_snapshot = pipeline.get_state(config)
    final_values = state_snapshot.values

    from hitl_agent.tools import SUBAGENT_TOKENS

    # Accumulate token metrics (Dispatcher + Subagents)
    disp_in, disp_out = 0, 0
    for msg in final_values.get("messages", []):
        usage = getattr(msg, "usage_metadata", {}) or {}
        disp_in += usage.get("input_tokens", 0)
        disp_out += usage.get("output_tokens", 0)

    tot_in = disp_in + SUBAGENT_TOKENS["input_tokens"]
    tot_out = disp_out + SUBAGENT_TOKENS["output_tokens"]

    print("=======================================================")
    print("hitl_agent Task Dispatcher Execution Finished!")
    print(f"- Output Directory: {out_dir}")
    print("\nToken Usage Breakdown:")
    print(f"- Dispatcher Tokens:   {disp_in} in / {disp_out} out")
    print(f"- Subagents Tokens:    {SUBAGENT_TOKENS['input_tokens']} in / {SUBAGENT_TOKENS['output_tokens']} out")
    print(f"\nTotal Combined Token Usage:")
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