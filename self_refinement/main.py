import argparse
from datetime import date
from pathlib import Path
import json

from langgraph.graph import StateGraph, START, END

from self_refinement.functions import (
    generate_requirements,
    evaluate_requirements,
    regenerate_requirements,
    human_approval,
)

from self_refinement.states.state import GraphState
from self_refinement.testing.fake_client import FakeLLMClient

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
    workflow.add_edge("generate_requirements", "evaluate_requirements")

    if with_human_gate:
        workflow.add_edge("evaluate_requirements", "human_approval")
        workflow.add_edge("human_approval", END)
    else:
        workflow.add_edge("evaluate_requirements", END)

    return workflow.compile()


def _build_state(project_root: Path, run_number: str) -> GraphState:
    
    #output directory for the generated file
    output_dir = project_root / "self_refinement" / run_number

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
        "stop_requested": False,
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
        state["llm_client"] = FakeLLMClient()

    app = _build_workflow(with_human_gate=args.with_human_gate)
    final_state = app.invoke(state)

    print("Run complete")
    print(f"mode={args.mode}")
    print(f"run_number={args.run_number}")
    print(f"feedback_written={final_state.get('feedback', False)}")


if __name__ == "__main__":
    main()
