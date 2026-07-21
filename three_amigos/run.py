"""Three Amigos Multi-Agent System — CLI Runner.

Interactive command-line runner that:
  1. Reads user research from a file path (or the default sample data).
  2. Creates a LangGraph workflow with a ``MemorySaver`` checkpointer so
     that ``interrupt()`` pauses work correctly for human-in-the-loop.
  3. Runs the graph, pausing at interrupt points.
  4. Prompts the human in the terminal for clarifications and approvals.
  5. Resumes the graph with human input.
  6. Saves the final Markdown report to ``three_amigos/Outputs/``.

Usage
─────
    python -m three_amigos.run
    python -m three_amigos.run --input path/to/research.md
    python -m three_amigos.run --input path/to/research.md --max-rounds 5
"""

import argparse
import os
import sys
from datetime import datetime

from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command

from three_amigos.main import create_graph


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
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Outputs")
    os.makedirs(d, exist_ok=True)
    return d


def _session_dir() -> str:
    """Create and return a timestamped session subdirectory inside Outputs/."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    d = os.path.join(_outputs_dir(), f"session_{timestamp}")
    os.makedirs(d, exist_ok=True)
    return d


def _separator(char: str = "═", width: int = 70) -> str:
    return char * width


# ─── Main ────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Three Amigos Requirements Engineering — CLI Runner",
    )
    parser.add_argument(
        "--input", "-i",
        type=str,
        default=None,
        help="Path to user research text file.  Defaults to Data/requirements.md.",
    )
    parser.add_argument(
        "--max-rounds", "-r",
        type=int,
        default=3,
        help="Maximum Three Amigos discussion rounds (default: 3).",
    )
    parser.add_argument(
        "--thread-id", "-t",
        type=str,
        default="three-amigos-session-1",
        help="LangGraph thread ID for checkpointing (default: three-amigos-session-1).",
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
    print("  THREE AMIGOS — Requirements Engineering System")
    print(_separator())
    print(f"  📄  Input:       {research_path}")
    print(f"  🔄  Max rounds:  {args.max_rounds}")
    print(f"  🧵  Thread ID:   {args.thread_id}")
    print(_separator())
    print()

    # ── Create session output directory ──────────────────────────────────────
    session_out = _session_dir()
    print(f"  📂  Output dir:  {session_out}")
    print(_separator())
    print()

    # ── Build graph with checkpointer ────────────────────────────────────────
    memory = MemorySaver()
    graph = create_graph(checkpointer=memory)
    config = {"configurable": {"thread_id": args.thread_id}}

    initial_state = {
        "user_research": user_research,
        "messages": [],
        "discussion_round": 0,
        "max_discussion_rounds": args.max_rounds,
        "needs_clarification": False,
        "consensus_reached": False,
        "human_approved": False,
        "discussion_history": [],
        "output_dir": session_out,
    }

    # ── First invocation ─────────────────────────────────────────────────
    print("🚀  Starting the Three Amigos pipeline…\n")
    graph.invoke(initial_state, config)

    # ── Handle interrupts in a loop ──────────────────────────────────────
    while True:
        snapshot = graph.get_state(config)

        # If no next nodes, the graph has completed
        if not snapshot.next:
            break

        # Inspect the interrupt payload
        interrupt_data = None
        if snapshot.tasks:
            for task in snapshot.tasks:
                if hasattr(task, "interrupts") and task.interrupts:
                    interrupt_data = task.interrupts[0].value
                    break

        if interrupt_data is None:
            # Safety: no interrupt found but graph is not done — shouldn't happen
            print("\n⚠️  Graph paused but no interrupt data found. Exiting.")
            break

        # ── Display interrupt to the user ────────────────────────────────
        interrupt_type = interrupt_data.get("type", "input")
        print(f"\n{_separator('─')}")
        print(f"  🛑  HUMAN INPUT REQUIRED  ({interrupt_type.upper()})")
        print(_separator("─"))

        if interrupt_type == "clarification":
            print("\n" + interrupt_data.get("message", ""))
            print()
            questions = interrupt_data.get("questions", "")
            print(questions)
            print()
        elif interrupt_type == "review":
            print("\n" + interrupt_data.get("message", ""))
            print()
            summary = interrupt_data.get("summary", "")
            # Truncate long summaries for terminal display
            if len(summary) > 3000:
                print(summary[:3000])
                print(f"\n  … [truncated — {len(summary)} chars total]")
            else:
                print(summary)
            print()

        print(_separator("─"))

        # ── Collect multi-line input ─────────────────────────────────────
        print("📝  Enter your response (press Enter twice to submit):\n")
        lines: list[str] = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line == "" and lines and lines[-1] == "":
                lines.pop()  # remove trailing blank
                break
            lines.append(line)

        user_input = "\n".join(lines).strip()
        if not user_input:
            user_input = "APPROVED"
            print("  (empty input — treating as APPROVED)")

        print(f"\n▶️  Resuming pipeline with your input…\n")

        # ── Resume the graph ─────────────────────────────────────────────
        graph.invoke(Command(resume=user_input), config)

    # ── Save final output ────────────────────────────────────────────────
    final_state = graph.get_state(config)
    final_vals = final_state.values
    final_output = final_vals.get("final_output", "")

    if not final_output:
        print("\n⚠️  No final output was generated.")
        sys.exit(1)

    # ── Write the combined final report ───────────────────────────────────
    final_report_path = os.path.join(session_out, "final_report.md")
    with open(final_report_path, "w", encoding="utf-8") as fh:
        fh.write(final_output)

    # ── Write separate artifact files from the final state ────────────────
    artifacts = {
        "extracted_user_needs":       ("Extracted User Needs",          "extracted_user_needs"),
        "functional_requirements":    ("Functional Requirements",       "functional_requirements"),
        "non_functional_requirements":("Non-Functional Requirements",   "non_functional_requirements"),
        "user_stories":              ("User Stories",                   "user_stories"),
        "po_feedback":               ("Product Owner Feedback (Final)", "po_feedback_final"),
        "dev_feedback":              ("Developer Feedback (Final)",     "dev_feedback_final"),
        "qa_feedback":               ("QA Engineer Feedback (Final)",   "qa_feedback_final"),
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

    # Save discussion history as a single file
    disc_history = final_vals.get("discussion_history") or []
    if disc_history:
        disc_path = os.path.join(artifacts_dir, "discussion_history.md")
        with open(disc_path, "w", encoding="utf-8") as fh:
            fh.write("# Three Amigos Discussion History\n\n")
            fh.write("\n\n---\n\n".join(disc_history))
        print(f"  💾  {'Discussion History':40s} → {disc_path}")

    print(f"\n{_separator()}")
    print(f"  ✅  PIPELINE COMPLETE")
    print(f"  📄  Full report:  {final_report_path}")
    print(f"  📂  Artifacts:    {artifacts_dir}")
    print(f"  📂  Session dir:  {session_out}")
    print(_separator())


if __name__ == "__main__":
    main()
