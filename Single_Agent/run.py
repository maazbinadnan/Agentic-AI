"""Single Agent — CLI Runner with Live Stream Processing.

Usage
─────
    python -m single_agent.run --output-dir single_agent_outputs
"""

import argparse
import sys
from global_layer.functions import _data_file
from single_agent._common_ import _session_dir, save_state
from single_agent.main import create_graph
from single_agent.local_states._state_ import AgentState


def main() -> None:
    parser = argparse.ArgumentParser(description="Single Agent CLI Runner")
    parser.add_argument(
        "--output-dir", "-o",
        type=str,
        default="single_agent_outputs",
        help="Output directory path for generated artifacts.",
    )
    args = parser.parse_args()

    output_dir = args.output_dir
    if not output_dir:
        parser.error(
            "Output directory path is required. Example: python -m single_agent.run --output-dir my_outputs"
        )

    initial_state: AgentState = {
        "messages": [],
        "ba_output": None,
        "ixd_output": None,
        "input": _data_file(),
        "output_dir": _session_dir(output_dir),
        "input_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0,
    }

    print("=======================================================")
    print("Launching Single Agent System pipeline...")
    print(f"Output Directory: {initial_state['output_dir']}")
    print("=======================================================\n")

    graph = create_graph()
    
    print("--- Live Stream ---")
    final_state = dict(initial_state)

    for chunk in graph.stream(initial_state, stream_mode="updates"):
        if isinstance(chunk, dict):
            for node_name, state_update in chunk.items():
                print(f"\n[Node Execution Completed]: `{node_name}`")
                if isinstance(state_update, dict):
                    final_state.update(state_update)
                    if "messages" in state_update and state_update["messages"]:
                        last_msg = state_update["messages"][-1]
                        msg_content = getattr(last_msg, "content", str(last_msg))
                        sys.stdout.write(f"{msg_content}\n")
                        sys.stdout.flush()

    print("\n--- End of Live Stream ---\n")

    print("=======================================================")
    print("Execution Finished! Total Accumulated Token Usage:")
    print(f"- Total Input Tokens:  {final_state.get('input_tokens', 0)}")
    print(f"- Total Output Tokens: {final_state.get('output_tokens', 0)}")
    print(f"- Total Tokens:        {final_state.get('total_tokens', 0)}")
    print("=======================================================\n")

    save_state(final_state)


if __name__ == "__main__":
    main()
