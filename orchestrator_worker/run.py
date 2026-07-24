"""Orchestrator-Worker Coordinator — CLI Runner.

Interactive command-line runner that:
  1. Reads user research from a file path (or the default sample data).
  2. Creates a LangGraph workflow with a ``MemorySaver`` checkpointer.
  3. Runs the graph to completion.
  4. Saves the final Markdown report to ``orchestrator_worker/outputs/``.

Usage
─────
    python -m orchestrator_worker
    python -m orchestrator_worker --input path/to/research.md
"""

import argparse
import os
from datetime import datetime

from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.runnables import RunnableConfig

from orchestrator_worker.main import create_graph
from orchestrator_worker.state.states import GlobalState
from global_functions.functions import DATA_FILE, _data_file


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _outputs_dir() -> str:
    """Return (and create) the Outputs directory for this module."""
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(d, exist_ok=True)
    return d


def _session_dir(run_number:str) -> str:
    """Create and return a timestamped session subdirectory inside outputs/."""
    d = os.path.join(_outputs_dir(), f"session_{run_number}")
    os.makedirs(d, exist_ok=True)
    return d


def _separator(char: str = "═", width: int = 70) -> str:
    return char * width


# ─── Main ────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Orchestrator-Worker Coordinator — CLI Runner",
    )
    parser.add_argument(
        "--thread-id", "-t",
        type=str,
        default="coordinator-session-1",
        help="LangGraph thread ID for checkpointing (default: coordinator-session-1).",
    )
    parser.add_argument(
        "--run", "-r",
        type=str,
        default=None,
        help="run number for making output directory",
    )
    args = parser.parse_args()
    run_number = args.run if args.run else datetime.now().strftime("%Y%m%d_%H%M%S")

    # ── Read user research ────────────────────────────────────────────────


    print(_separator())
    print("  ORCHESTRATOR-WORKER — Coordinator Pipeline")
    print(_separator())
    print(f"  📄  Input:       {DATA_FILE}")
    print(f"  🧵  Thread ID:   {args.thread_id}")
    print(_separator())
    print()

    # ── Create session output directory ──────────────────────────────────
    session_out = _session_dir(args.run)
    print(f"  📂  Output dir:  {session_out}")
    print(_separator())
    print()

    # ── Build graph with checkpointer ────────────────────────────────────
    memory = MemorySaver()
    graph = create_graph(checkpointer=memory)
    config:RunnableConfig = {"configurable": {"thread_id": args.thread_id}}

    # ---- Build Initial Message ---- #
    initial_message = HumanMessage(content="could you please extract requirements from this data file:" \
    f"{_data_file()}")


    # ---- Build Initial State ---- #
    initial_state:GlobalState = {
        "messages": [initial_message],
        "input": _data_file(),
        "next_agent": None,
        "current_phase": "start",
        "output_dir": session_out,
        "final_output": None,
        "html_mockups": None,
        "full_ba_analysis": None,
        "user_needs": None,
        "functional_requirements": None,
        "non_functional_requirements": None,
        "user_stories": None
    }



    # ── Run the pipeline ─────────────────────────────────────────────────
    print("🚀  Starting the Coordinator pipeline…\n")
    graph.invoke(initial_state, config)


if __name__ == "__main__":
    main()
