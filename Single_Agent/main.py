import os, sys
from langgraph.graph import StateGraph, MessagesState, START, END
from single_agent.states.state import GraphState
from single_agent.functions import generate_requirements
from evaluation.LLM_as_a_judge import evaluate_user_stories

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
    "output_functional_path": rf'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Single_Agent\{run_number}\output_gpt_4.1_functional.json',
    "output_non_functional_path":rf'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Single_Agent\{run_number}\output_gpt_4.1_non_functional.json',
    "model":"gpt-4.1"
}

app = workflow.compile()
# final_state = app.invoke(state)

## calling llm as a judge evaluation
evaluation_filepath =rf'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\evaluation\single_agent\{run_number}\{state['model']}\evaluation.json'
evaluate_user_stories(state['requirements_filepath'],state['output_functional_path'],state['output_non_functional_path'],evaluation_filepath,"gpt-5.4")