import argparse
from datetime import date
from pathlib import Path
import json
import uuid

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command
from langgraph.graph import StateGraph, START, END

from langchain_core.runnables import RunnableConfig

from self_refinement.functions import (
    generate_requirements,
    evaluate_requirements,
    regenerate_requirements,
    human_approval,
    process_interrupt,
    route_after_human
)

from self_refinement.states.state import GraphState

GENERATOR_MODEL = "gpt-4.1"
EVALUATOR_MODEL = "gpt-5.4"


#define the default run_number
def _default_run_number() -> str:
    today = date.today()
    return f"{today.month}-{today.day}-{today.year}"


def _build_workflow(with_human_gate: bool = False):
    workflow = StateGraph(GraphState)

    workflow.add_node("generate_requirements", generate_requirements)
    workflow.add_node("evaluate_requirements", evaluate_requirements)
    workflow.add_node("regenerate_requirements", regenerate_requirements)
    workflow.add_node("human_approval", human_approval)

    workflow.add_edge(START, "generate_requirements")

    if with_human_gate:
        workflow.add_edge("generate_requirements", "human_approval")
        workflow.add_conditional_edges(
            "human_approval", 
            route_after_human,
            {
                "evaluate_requirements": "evaluate_requirements",
                END: END
            }
        )
        workflow.add_edge("evaluate_requirements", "regenerate_requirements")
        workflow.add_edge("regenerate_requirements", "human_approval")
        # Add a checkpointer so interrupt/resume can persist state.
        checkpointer = InMemorySaver()
        return workflow.compile(checkpointer=checkpointer)
    else:
        workflow.add_edge("generate_requirements", END)
        return workflow.compile()


def _build_state(project_root: Path, run_number: str) -> GraphState:
    
    #output directory for the generated file
    output_dir = project_root / "self_refinement" / run_number
    print("output director is ",output_dir)
    #read details from config file
    config_file = project_root/"self_refinement"/ "config.json"
    with open(config_file, 'r') as file:
        config = json.load(file)

    return {
        "messages": [],
        "requirements_filepath": str(project_root / "Data" / "requirements.md"),
        "think_file": str(output_dir / "thinking.json"),
        "output_functional_path": str(output_dir / f"output_{GENERATOR_MODEL}_functional.json"),
        "output_non_functional_path": str(output_dir / f"output_{GENERATOR_MODEL}_non_functional.json"),
        "feedback_path": str(output_dir / f"feedback_{EVALUATOR_MODEL}.json"),
        "generation_model": config['generator_model'],
        "evaluator_model": config['evaluator_model'],
        "feedback": False,
        "evaluation_count": 0,
        "run_evaluation": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run self_refinement pipeline in real or dummy mode."
    )
    parser.add_argument(
        "--mode",
        choices=["real", "dummy"],
        default="dummy",
        help="Use 'dummy' to run deterministic fake LLM calls for safe preflight tests.",
    )
    parser.add_argument(
        "--run-number",
        default=_default_run_number(),
        help="Folder suffix under self_refinement outputs.",
    )
    parser.add_argument(
        "--with-human-gate",
        action="store_true",
        help="Route through the human approval node after evaluation.",
    )
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    state = _build_state(project_root=project_root, run_number=args.run_number)

    if args.mode == "dummy":
        state["llm_mode"] = "dummy"

    graph = _build_workflow(with_human_gate=args.with_human_gate)

    ##define the config
    config: RunnableConfig = {
    "configurable": {
        "thread_id": str(uuid.uuid4()),
        }
    }

    initial_output = graph.invoke(state, config)
    #take user input
    if args.with_human_gate:
        while True:
            # Inspect the compiled graph's active checkpointer state
            graph_info = graph.get_state(config)
            
            # If there are no pending interrupts, the graph has hit END successfully!
            if not graph_info.interrupts:
                print("\nWorkflow completed successfully.")
                break
                
            print("\n--- Graph Paused for Human Approval ---")
            user_response = input("Do we run an evaluation loop? [Y/N]: ")
            
            is_approved = process_interrupt(user_response)
            
            # 3. Resume execution and capture the BRAND NEW snapshot returned by invoke
            print("\n--- Resuming Graph Execution ---")
            current_state_snapshot = graph.invoke(Command(resume=is_approved), config)

    print("Run complete")
    print(f"mode={args.mode}")
    print(f"run_number={args.run_number}")
    # print(f"feedback_written={final_state.get('feedback', False)}")

if __name__ == "__main__":
    main()
