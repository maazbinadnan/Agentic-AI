import os, sys
from langgraph.graph import StateGraph, MessagesState, START, END
from single_agent.states.state import GraphState
from single_agent.functions import generate_requirements
from evaluation.LLM_as_a_judge import evaluate_user_stories
from evaluation.Metrics import metrics_user_stories
MODEL = "gpt-5.4"
#change to whatever run number u want, it is currebntly using dd/mm//yy
run_number = "7-18-2026"

#-----Defining the Workflow-----#
workflow = StateGraph(GraphState)

workflow.add_node("generate_requirements",generate_requirements)

workflow.add_edge(START,"generate_requirements")
workflow.add_edge("generate_requirements",END)

state:GraphState ={
    "messages" : None,
    "requirements_filepath":r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Data\requirements.md",
    "think_file" :rf'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Single_Agent\{run_number}\thinking.json',
    "output_functional_path": rf'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Single_Agent\{run_number}\output_{MODEL}_functional.json',
    "output_non_functional_path":rf'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Single_Agent\{run_number}\output_{MODEL}_non_functional.json',
    "model":"gpt-5.4"
}

app = workflow.compile()
final_state = app.invoke(state)


## calling llm as a judge evaluation
evaluation_filepath =rf'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\evaluation\single_agent\{run_number}\{state['model']}\evaluation.json'
evaluate_user_stories(state['requirements_filepath'],state['output_functional_path'],state['output_non_functional_path'],evaluation_filepath,"gpt-5.4")

## calling USER METRICS
ground_truth_file =r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Data\functional_requirements.json"
generated_file = rf"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\single_agent\7-18-2026\output_{state['model']}_functional.json"
metrics_file = rf"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\evaluation\single_agent\7-18-2026\{state['model']}\metrics_functional.json"
metrics_user_stories(ground_truth_file,generated_file,metrics_file,"gpt-5.4")

ground_truth_file =r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Data\non_functional_requirements.json"
generated_file = rf"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\single_agent\7-18-2026\output_{state['model']}_non_functional.json"
metrics_file = rf"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\evaluation\single_agent\7-18-2026\{state['model']}\metrics_non_functional.json"
metrics_user_stories(ground_truth_file,generated_file,metrics_file,"gpt-5.4")