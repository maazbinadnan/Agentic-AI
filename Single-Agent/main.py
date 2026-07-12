from langgraph.graph import StateGraph, MessagesState, START, END
from States.state import GraphState
from functions import generate_requirements
import os,sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_path not in sys.path:
    sys.path.insert(0, root_path)


#-----Defining the Workflow-----#
workflow = StateGraph(GraphState)

workflow.add_node("generate_requirements",generate_requirements)

workflow.add_edge(START,"generate_requirements")
workflow.add_edge("generate_requirements",END)

state:GraphState ={
    "filepath":r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Data\requirements.md",
    "output_functional_path": r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Single-Agent\Outputs\output_gpt_5.4_functional.json',
    "output_non_functional_path":r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Single-Agent\Outputs\output_gpt_5.4_functional.md',
    "model":"gpt-5.4"
}

app = workflow.compile()
final_state = app.invoke(state)
# print(final_state)