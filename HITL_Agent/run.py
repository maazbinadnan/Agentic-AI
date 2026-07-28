"""ba_team_agent Module — CLI Runner for Task Dispatcher with Live Token Streaming (using create_agent).

Usage:
    python -m ba_team_agent.run --output-dir outputs_ba_agent -tid "dispatcher_1"
"""

import argparse
import sys, json
from langchain_core.messages import HumanMessage, AIMessageChunk, ToolMessage
from langchain_core.runnables import RunnableConfig
from ba_team_agent.tools import SUBAGENTS

from global_layer.functions import _data_file
from ba_team_agent._common_ import _session_dir, save_state
from ba_team_agent.main import create_agent_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="ba_team_agent Task Dispatcher CLI Runner with Live Streaming")
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
    print("Launching ba_team_agent (Token-by-Token Live Streaming)...")
    print(f"Sub-Agent Registry: {list(SUBAGENTS.keys())}")
    print(f"Output Directory:   {out_dir}")
    print("=======================================================\n")

    pipeline = create_agent_pipeline()

    instruction = (
        f"Target Output Directory: '{out_dir}'\n\n"
        f"Raw Operational Requirements Document:\n{raw_input}\n\n"
        f"GOAL: Generate a complete Business Analysis deliverables package into '{out_dir}' including:\n"
        f"1. Elicitation Report (01_elicitation_report.md)\n"
        f"2. User Needs Specification (02_user_needs_report.md)\n"
        f"3. Functional Requirements (03_functional_requirements.md)\n"
        f"4. Non-Functional Requirements (04_non_functional_requirements.md)\n"
        f"5. User Stories with Acceptance Criteria (05_user_stories.md)\n"
        f"6. UI Mockups and Interaction Design (06_ui_mockups.md)"
    )

    initial_state = {
        "messages": [HumanMessage(content=instruction)],
    }

    print("\n--- Live Stream (Token-by-Token & Tool Arguments) ---")

    tool_call_buffer = {}

    def flush_tool_calls():
        if tool_call_buffer:
            for idx, tc in list(tool_call_buffer.items()):
                t_name = tc.get("name", "tool")
                t_args = tc.get("args", "")
                sys.stdout.write(f"\n\n -> [Tool / SubAgent Call]: `{t_name}`\n")
                if t_args:
                    try:
                        parsed = json.loads(t_args)
                        formatted_args = json.dumps(parsed, indent=4)
                        sys.stdout.write(f"    Arguments:\n{formatted_args}\n")
                    except Exception:
                        sys.stdout.write(f"    Arguments: {t_args}\n")
                sys.stdout.flush()
            tool_call_buffer.clear()

    # Real-time token-by-token streaming loop using stream_mode="messages"
    for chunk, metadata in pipeline.stream(initial_state, config=config, stream_mode="messages"):  # type: ignore
        if isinstance(chunk, AIMessageChunk):
            if chunk.content:
                flush_tool_calls()
                if isinstance(chunk.content, str):
                    sys.stdout.write(chunk.content)
                    sys.stdout.flush()
                elif isinstance(chunk.content, list):
                    for part in chunk.content:
                        if isinstance(part, dict) and part.get("type") == "text":
                            sys.stdout.write(part.get("text", ""))
                            sys.stdout.flush()
                        elif isinstance(part, str):
                            sys.stdout.write(part)
                            sys.stdout.flush()

            if hasattr(chunk, "tool_call_chunks") and chunk.tool_call_chunks:
                for tc in chunk.tool_call_chunks:
                    idx = tc.get("index", 0)
                    if idx not in tool_call_buffer:
                        tool_call_buffer[idx] = {"name": tc.get("name") or "", "args": tc.get("args") or ""}
                    else:
                        if tc.get("name"):
                            tool_call_buffer[idx]["name"] += tc.get("name")
                        if tc.get("args"):
                            tool_call_buffer[idx]["args"] += tc.get("args")

        elif isinstance(chunk, ToolMessage):
            flush_tool_calls()
            sys.stdout.write(f"\n <- [SubAgent Result]: {chunk.content}\n\n")
            sys.stdout.flush()

    flush_tool_calls()
    print("\n--- End of Live Stream ---\n")

    state_snapshot = pipeline.get_state(config)
    final_values = state_snapshot.values

    # Accumulate token metrics
    tot_in, tot_out = 0, 0
    for msg in final_values.get("messages", []):
        usage = getattr(msg, "usage_metadata", {}) or {}
        tot_in += usage.get("input_tokens", 0)
        tot_out += usage.get("output_tokens", 0)

    print("=======================================================")
    print("ba_team_agent Task Dispatcher Execution Finished!")
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
