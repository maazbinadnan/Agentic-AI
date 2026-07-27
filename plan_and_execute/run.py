"""Plan-and-Execute Pattern — CLI Runner with Interactive Elicitation Agent.

Usage
─────
    python -m plan_and_execute.run --output-dir plan_outputs/test_run_1 -tid "1"
"""

import argparse
from langgraph.types import Command
from langchain_core.runnables import RunnableConfig

from global_layer.functions import _data_file
from plan_and_execute._common_ import _session_dir, save_state, answer_elicitation_qs
from plan_and_execute.main import create_graph
from plan_and_execute.local_states._state_ import AgentState


def main() -> None:
    parser = argparse.ArgumentParser(description="Plan-and-Execute CLI Runner")
    parser.add_argument("--output-dir", "-o", type=str, default="plan_outputs", help="Output directory path.")
    parser.add_argument("--thread-id", "-tid", type=str, default="test_run_1", help="Thread ID for graph checkpointing.")
    args = parser.parse_args()

    config: RunnableConfig = {"configurable": {"thread_id": args.thread_id}}

    initial_state: AgentState = {
        "messages": [],
        "plan_output": None,
        "elicitation_output": None,
        "user_clarifications": {},
        "input": _data_file(),
        "output_dir": _session_dir(args.output_dir),
        "input_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0,
    }

    print("Launching Plan-and-Execute pipeline...")
    print(f"Output Directory: {initial_state['output_dir']}\n")

    graph = create_graph()
    current_input = initial_state

    
    # Graph stream loop: repeat while graph execution is interrupted
    while True:
        interrupted = False
        for event in graph.stream(current_input, config=config):
            if "__interrupt__" in event:
                interrupted = True
                payload = event["__interrupt__"][0].value
                # Collect user answers via CLI
                user_answers = answer_elicitation_qs(payload)
                # Prepare resume Command for the next iteration of the while loop
                current_input = Command(resume=user_answers)
                break
        if not interrupted:
            break
    
    state_snapshot = graph.get_state(config)
    final_state = state_snapshot.values

    elicitation = final_state.get("elicitation_output") or {}
    user_clarifications = final_state.get("user_clarifications") or {}

    print("\n=======================================================")
    print("Plan-and-Execute HITL Pipeline Finished!")
    print(f"- Discovered Personas:        {len(elicitation.get('personas', []))}")
    print(f"- Extracted User Needs:      {len(elicitation.get('user_needs', []))}")
    print(f"- Stakeholder Answers Saved: {len(user_clarifications)}")

    if user_clarifications:
        print("\nSaved Stakeholder Answers:")
        for q_id, ans in user_clarifications.items():
            print(f"  [{q_id}]: {ans}")

    print("\nTotal Accumulated Token Usage:")
    print(f"- Total Input Tokens:  {final_state.get('input_tokens', 0)}")
    print(f"- Total Output Tokens: {final_state.get('output_tokens', 0)}")
    print(f"- Total Tokens:        {final_state.get('total_tokens', 0)}")
    print("=======================================================\n")

    save_state(final_state)


if __name__ == "__main__":
    main()
