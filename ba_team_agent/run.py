"""ba_team_agent Module — CLI Runner for Task Dispatcher (using create_agent exclusively).

Usage:
    python -m ba_team_agent.run --output-dir outputs_ba_agent -tid "dispatcher_1"
"""

import argparse
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from ba_team_agent.tools import SUBAGENTS

from global_layer.functions import _data_file
from ba_team_agent._common_ import _session_dir, save_state
from ba_team_agent.main import create_agent_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="ba_team_agent Task Dispatcher CLI Runner")
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
    print("Launching ba_team_agent (create_agent Task Dispatcher)...")
    print(f"Sub-Agent Registry: {SUBAGENTS.keys()}")
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

    seen_messages = set()

    # Real-time streaming loop
    for chunk in pipeline.stream(initial_state, config=config, stream_mode="updates"):  # type: ignore
        if isinstance(chunk, dict):
            for node_name, state_update in chunk.items():
                if isinstance(state_update, dict) and "messages" in state_update:
                    for msg in state_update["messages"]:
                        msg_id = getattr(msg, "id", None) or id(msg)
                        if msg_id not in seen_messages:
                            seen_messages.add(msg_id)

                            if isinstance(msg, AIMessage):
                                if msg.content:
                                    print(f"\n[Agent Message / Dispatch]:\n{msg.content}\n")
                                if hasattr(msg, "tool_calls") and msg.tool_calls:
                                    for tc in msg.tool_calls:
                                        print(f" -> [Tool / SubAgent Call]: `{tc['name']}`")

                            elif isinstance(msg, ToolMessage):
                                print(f" <- [SubAgent Result]: {msg.content}")

    state_snapshot = pipeline.get_state(config)
    final_values = state_snapshot.values

    # Accumulate token metrics
    tot_in, tot_out = 0, 0
    for msg in final_values.get("messages", []):
        usage = getattr(msg, "usage_metadata", {}) or {}
        tot_in += usage.get("input_tokens", 0)
        tot_out += usage.get("output_tokens", 0)

    print("\n=======================================================")
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
