from langgraph.graph import StateGraph, START, END
from self_refinement.states.state import GraphState
from self_refinement.functions import generate_requirements,evaluate_requirements,regenerate_requirements
from global_functions.functions import _write_json_file
import json
GENERATOR_MODEL = "gpt-4.1"
EVALUATOR_MODEL = "gpt-5.4"
RUN_NUMBER = "7-19-2026"

#-----Defining the Workflow-----#
workflow = StateGraph(GraphState)

workflow.add_node("generate_requirements",generate_requirements)
workflow.add_node("evaluate_requirements",evaluate_requirements)
workflow.add_node("regenerate_requirements",regenerate_requirements)

workflow.add_edge(START,"regenerate_requirements")
# workflow.add_edge("generate_requirements","evaluate_requirements")
# workflow.add_edge("evaluate_requirements","regenerate_requirements")
workflow.add_edge("regenerate_requirements",END)


state:GraphState ={
    "messages" : [],
    "requirements_filepath":r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Data\requirements.md",
    "think_file" :rf'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\{RUN_NUMBER}\thinking.json',
    "output_functional_path": rf'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\{RUN_NUMBER}\output_{GENERATOR_MODEL}_functional.json',
    "output_non_functional_path":rf'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\{RUN_NUMBER}\output_{GENERATOR_MODEL}_non_functional.json',
    "feedback_path":rf'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\{RUN_NUMBER}\feedback_{EVALUATOR_MODEL}.json',
    "generation_model": "gpt-4.1",
    "evaluator_model" : "gpt-5.4",
    "feedback" : False,
    "evaluation_count": 0,
    "stop_requested": False
}

app = workflow.compile()

final_state = app.invoke(state)
_write_json_file(filepath=r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\states\messages.json",content=final_state['messages'])