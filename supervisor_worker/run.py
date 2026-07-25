"""Supervisor-Worker Pattern — CLI Runner.

Usage
─────
    python -m supervisor_worker.run --output-dir outputs/test_run_1
"""

import argparse
from global_layer.functions import _data_file
from supervisor_worker._common_ import _session_dir, save_state
from supervisor_worker.main import create_graph
from supervisor_worker.local_states._state_ import AgentState


def main() -> None:
    parser = argparse.ArgumentParser(description="Supervisor-Worker CLI Runner")
    parser.add_argument(
        "--output-dir", "-o",
        type=str,
        default="supervisor_outputs",
        help="Output directory path for requirement files.",
    )
    args = parser.parse_args()

    output_dir = args.output_dir
    if not output_dir:
        parser.error(
            "Output directory path is required. Example: python -m supervisor_worker.run --output-dir my_outputs"
        )

    initial_state: AgentState = {
        "messages": [],
        "ba_output": None,
        "ixd_output": None,
        "supervisor_feedback": None,
        "feedback_history": [],
        "input": _data_file(),
        "output_dir": _session_dir(output_dir),
        "phase": "ba",
        "iterations": {"ba": 0, "ixd": 0},
        "max_iterations_per_phase": 3,
        "verdict": None,
    }

    print(f"Launching Supervisor-Worker System pipeline...")
    print(f"Output Directory: {initial_state['output_dir']}\n")

    graph = create_graph()
    final_state = graph.invoke(initial_state)
    save_state(final_state)


if __name__ == "__main__":
    main()
