"""Supervisor-Worker Pattern — CLI Runner.

Usage
─────
    python -m supervisor_worker.run --output_dir output_folder
    python supervisor_worker/run.py output_folder
"""

import argparse
from global_layer.functions import _data_file
from supervisor_worker._common_ import _session_dir,save_state
from supervisor_worker.main import create_graph
from supervisor_worker.local_states._state_ import AgentState,OutputState


def main() -> None:
    parser = argparse.ArgumentParser(description="Supervisor-Worker CLI Runner")
    parser.add_argument(
        "--output-dir", "-o",
        type=str,
        default=None,
        help="Output directory path for requirement files.",
    )
    args = parser.parse_args()

    output_dir = args.output_dir or args.positional_output_dir
    if not output_dir:
        parser.error(
            "Output directory path is required. Example: python -m supervisor_worker.run --output_dir my_outputs"
        )

    initial_state: AgentState = {
        "messages": [],
        "ba_output": None,
        "ixd_output":None,
        "supervisor_feedback":None,
        "input": _data_file(),
        "output_dir": _session_dir(output_dir),
        "phase" : "ba",
        "iteration_count": 0,
        "max_iterations":3,
        "verdict":None
    }

    graph = create_graph()
    final_state = graph.invoke(initial_state)
    save_state(final_state)

if __name__ == "__main__":
    main()
