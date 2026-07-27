"""react_agent Module — CLI Runner for ReAct Single-Agent Baseline.

Usage:
    python -m react_agent.run --output-dir outputs_react -tid "react_1"
"""

import argparse
from pathlib import Path
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig

from global_layer.functions import _data_file
from react_agent._common_ import _session_dir, save_state
from react_agent.main import build_react_graph


def main() -> None:
    parser = argparse.ArgumentParser(description="ReAct Agent CLI Runner")
    parser.add_argument("--output-dir", "-o", type=str, default="outputs_react", help="Output directory path.")
    parser.add_argument("--thread-id", "-tid", type=str, default="react_run_1", help="Thread ID for graph checkpointing.")
    args = parser.parse_args()

    config: RunnableConfig = {"configurable": {"thread_id": args.thread_id}}

    out_dir = _session_dir(args.output_dir)
    raw_input = _data_file()

    print("=======================================================")
    print("Launching ReAct Agent (Thought-Action-Observation Loop)...")
    print(f"Output Directory: {out_dir}")
    print("=======================================================\n")

    graph = build_react_graph()

    instruction = (
        f"Read the raw operational requirements document below. Interleave your reasoning (Thought) "
        f"with tool execution (Action) to save all 5 required RE markdown files into output directory '{out_dir}'.\n\n"
        f"Raw Requirements Document:\n{raw_input}"
    )

    initial_state = {
        "messages": [HumanMessage(content=instruction)],
        "output_dir" :out_dir
    }

    # Execute ReAct stream loop
    for event in graph.stream(initial_state, config=config):
        pass

    state_snapshot = graph.get_state(config)
    final_values = state_snapshot.values

    # Calculate token metrics
    tot_in, tot_out = 0, 0
    for msg in final_values.get("messages", []):
        usage = getattr(msg, "usage_metadata", {}) or {}
        tot_in += usage.get("input_tokens", 0)
        tot_out += usage.get("output_tokens", 0)

    print("\n=======================================================")
    print("ReAct Agent Execution Finished!")
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
