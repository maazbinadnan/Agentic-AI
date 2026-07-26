"""Single Agent Final — CLI Runner.

Usage
─────
    python -m single_agent_final.run --output-dir single_agent_outputs
"""

import argparse
from global_layer.functions import _data_file
from single_agent_final._common_ import _session_dir, save_state
from single_agent_final.main import create_graph
from single_agent_final.local_states._state_ import AgentState


def main() -> None:
    parser = argparse.ArgumentParser(description="Single Agent Final CLI Runner")
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
            "Output directory path is required. Example: python -m single_agent_final.run --output-dir my_outputs"
        )

    initial_state: AgentState = {
        "messages": [],
        "ba_output": None,
        "ixd_output": None,
        "input": _data_file(),
        "output_dir": _session_dir(output_dir),
        "phase": "ba",
    }

    print("Launching Single Agent Final System pipeline...")
    print(f"Output Directory: {initial_state['output_dir']}\n")

    graph = create_graph()
    final_state = graph.invoke(initial_state)
    save_state(final_state)


if __name__ == "__main__":
    main()
