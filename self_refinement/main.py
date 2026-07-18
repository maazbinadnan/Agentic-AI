import os, sys
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command
from langchain_core.runnables import RunnableConfig
from self_refinement.states.state import GraphState
from self_refinement.functions import generate_requirements,evaluate_requirements


#-----Defining the Workflow-----#
workflow = StateGraph(GraphState)

workflow.add_node("generate_requirements",generate_requirements)
workflow.add_node("evaluate_requirements",evaluate_requirements)


workflow.add_edge(START,"generate_requirements")

def route_after_generation(state: GraphState):
    return END if state["stop_requested"] == 1 else "evaluate_requirements"

def route_after_finish_execution(state: GraphState):
    return END if state["stop_requested"] else "generate_requirements"

workflow.add_conditional_edges("generate_requirements", route_after_generation)
workflow.add_edge("evaluate_requirements","generate_requirements")

state:GraphState ={
    "messages" : None,
    "requirements_filepath":r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Data\requirements.md",
    "think_file" :r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\1\thinking.json',
    "output_functional_path": r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\1\output_gpt_5.4_functional.json',
    "output_non_functional_path":r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\1\output_gpt_5.4_non_functional.json',
    "feedback_path":r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\1\feedback_gpt_5.4.json',
    "generation_model": "gpt-4.1",
    "evaluator_model" : "gpt-5.4",
    "feedback" : False,
    "evaluation_count": 0,
    "stop_requested": False
}

app = workflow.compile(checkpointer=MemorySaver())
config: RunnableConfig = {"configurable": {"thread_id": "self-refinement-run"}}

final_state = app.invoke(state, config=config)

while "__interrupt__" in final_state:
    user_choice = input("Stop after first evaluation? (true/false): ").strip()
    final_state = app.invoke(Command(resume=user_choice), config=config)

print(final_state["messages"])