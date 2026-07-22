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
import sys
from datetime import datetime

from langgraph.checkpoint.memory import MemorySaver

from orchestrator_worker.main import create_graph


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _default_research_path() -> str:
    """Return the path to the sample user research shipped with the repo."""
    return os.path.normpath(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "Data",
            "requirements.md",
        )
    )


def _outputs_dir() -> str:
    """Return (and create) the Outputs directory for this module."""
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(d, exist_ok=True)
    return d


def _session_dir() -> str:
    """Create and return a timestamped session subdirectory inside outputs/."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    d = os.path.join(_outputs_dir(), f"session_{timestamp}")
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
        "--input", "-i",
        type=str,
        default=None,
        help="Path to user research text file.  Defaults to Data/requirements.md.",
    )
    parser.add_argument(
        "--thread-id", "-t",
        type=str,
        default="coordinator-session-1",
        help="LangGraph thread ID for checkpointing (default: coordinator-session-1).",
    )
    args = parser.parse_args()

    # ── Read user research ────────────────────────────────────────────────
    research_path = args.input or _default_research_path()
    if not os.path.isfile(research_path):
        print(f"❌  File not found: {research_path}")
        sys.exit(1)

    with open(research_path, "r", encoding="utf-8") as fh:
        user_research = fh.read()

    print(_separator())
    print("  ORCHESTRATOR-WORKER — Coordinator Pipeline")
    print(_separator())
    print(f"  📄  Input:       {research_path}")
    print(f"  🧵  Thread ID:   {args.thread_id}")
    print(_separator())
    print()

    # ── Create session output directory ──────────────────────────────────
    session_out = _session_dir()
    print(f"  📂  Output dir:  {session_out}")
    print(_separator())
    print()

    # ── Build graph with checkpointer ────────────────────────────────────
    memory = MemorySaver()
    graph = create_graph(checkpointer=memory)
    config = {"configurable": {"thread_id": args.thread_id}}

    initial_state = {
        "user_research": user_research,
        "messages": [],
        "next_agent": None,
        "current_phase": "start",
        "output_dir": session_out,
    }

    # ── Run the pipeline ─────────────────────────────────────────────────
    print("🚀  Starting the Coordinator pipeline…\n")
    graph.invoke(initial_state, config)

    # ── Save final output ────────────────────────────────────────────────
    final_state = graph.get_state(config)
    final_vals = final_state.values
    final_output = final_vals.get("final_output", "")

    if not final_output:
        print("\n⚠️  No final output was generated.")
        sys.exit(1)

    # ── Write the combined final report ──────────────────────────────────
    final_report_path = os.path.join(session_out, "final_report.md")
    with open(final_report_path, "w", encoding="utf-8") as fh:
        fh.write(final_output)

    # ── Write separate artifact files from the final state ───────────────
    artifacts = {
        "user_stories":  ("User Stories & Acceptance Criteria", "user_stories"),
        "html_mockups":  ("HTML Mockups",                       "html_mockups"),
    }

    artifacts_dir = os.path.join(session_out, "artifacts")
    os.makedirs(artifacts_dir, exist_ok=True)

    for state_key, (title, fname) in artifacts.items():
        value = final_vals.get(state_key, "")
        if value:
            path = os.path.join(artifacts_dir, f"{fname}.md")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(f"# {title}\n\n{value}")
            print(f"  💾  {title:40s} → {path}")

    print(f"\n{_separator()}")
    print(f"  ✅  PIPELINE COMPLETE")
    print(f"  📄  Full report:  {final_report_path}")
    print(f"  📂  Artifacts:    {artifacts_dir}")
    print(f"  📂  Session dir:  {session_out}")
    print(_separator())


if __name__ == "__main__":
    main()
