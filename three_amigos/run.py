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

    # ── Build graph with checkpointer ────────────────────────────────────
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
    final_output = final_state.values.get("final_output", "")

    if not final_output:
        print("\n⚠️  No final output was generated.")
        sys.exit(1)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(_outputs_dir(), f"final_report_{timestamp}.md")

    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(final_output)

    print(f"\n{_separator()}")
    print(f"  ✅  PIPELINE COMPLETE")
    print(f"  📄  Report saved: {output_path}")
    print(_separator())


if __name__ == "__main__":
    main()
