"""Module: main

Simple workflow runner for generating requirements, writing outputs,
and upserting vectors. Only documentation was added in this pass.
"""

from langgraph.graph import StateGraph, MessagesState, START, END
from States.State import GraphState
from Functions.Agent_functions import Agent_functions
from Functions.helper_functions import evaluate_user_stories
from Client_Layer.AzureClient import ChatClient
from Client_Layer.PineconeClient import PineconeClient
from pathlib import Path

pc = PineconeClient()
az = ChatClient()
# create the graph
workflow = StateGraph(GraphState)
agent = Agent_functions(pinecone_client=pc,azure_client=az)
# add nodes

workflow.add_node("create_user_stories", agent.generate_user_stories)
workflow.add_node("write_to_file", agent.write_to_csv)
workflow.add_node("write_vector", agent.upsert_vectors)

# edges
workflow.add_edge(START, "create_user_stories")
workflow.add_edge("create_user_stories", "write_to_file")
workflow.add_edge("write_to_file", "write_vector")
workflow.add_edge("write_vector", END)


# compile
app = workflow.compile()

initial_state: GraphState = {
	"namespace": "requirements",
	"model": "gpt-4.1",
	"requirements": None,
	"filepath": Path(
		r"C:\\Users\\OMNI BOOK\\OneDrive\\Personal-Projects\\Agent-Learning\\Dissertation-Project\\LLM-Optimization\\Data\\LLM_Outputs"
	),
}

# final_state = app.invoke(initial_state)
data_path = r"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\LLM-Optimization\Data\Ground_truths\functional_requirements.csv"
score_threshold = [0,0.6,0.7,0.8,0.9]
for score in score_threshold:
	evaluate_user_stories(pc=pc,az=az,filepath=Path(data_path),type='Functional Requirements',score_threshold=score)

