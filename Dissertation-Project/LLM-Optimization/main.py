from langgraph.graph import StateGraph, MessagesState, START, END
from State import GraphState
from Agent_functions import generate_user_stories,write_to_file
from pathlib import Path

#create the graph 
workflow = StateGraph(GraphState)

#add nodes
# workflow.add_node("parse_file",parse_input)
workflow.add_node("create_user_stories",generate_user_stories)
workflow.add_node("write_to_file", write_to_file)

#edges
workflow.add_edge(START,"create_user_stories")
workflow.add_edge("create_user_stories","write_to_file")
workflow.add_edge("write_to_file",END)

#compile
app = workflow.compile()

initial_state:GraphState = {"model":"gpt-4.1","requirements":None,"filepath":Path("C:\\Users\\OMNI BOOK\\OneDrive\\Personal-Projects\\Agent-Learning\\Dissertation-Project\\LLM-Optimization\\LLM_Outputs")}

final_state = app.invoke(initial_state)