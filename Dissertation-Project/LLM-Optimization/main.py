"""Module: main

Simple workflow runner for generating requirements, writing outputs,
and upserting vectors. Only documentation was added in this pass.
"""

from langgraph.graph import StateGraph, MessagesState, START, END
from States.State import GraphState
from Functions.agent_functions import Agent_functions
from Functions.helper_functions import evaluate_user_stories
from Client_Layer.AzureClient import ChatClient
from Client_Layer.PineconeClient import PineconeClient
from pathlib import Path
import json 
from IPython.display import Image

with open(r"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\config.json","r") as jsonfile:
    data = json.load(jsonfile)
    

pc = PineconeClient()
az = ChatClient()
# create the graph
workflow = StateGraph(GraphState)
agent = Agent_functions(pinecone_client=pc,azure_client=az)
# add nodes

workflow.add_node("create_user_stories", agent.generate_user_stories)
# workflow.add_node("write_generated_to_file", agent.write_to_csv)
# workflow.add_node("write_generated_to_vector_store", agent.upsert_vectors)
workflow.add_node("evaluate_user_stories",agent.evaluate_user_stories)

# edges
workflow.add_edge(START, "create_user_stories")
workflow.add_edge("create_user_stories" , "evaluate_user_stories")
workflow.add_edge("evaluate_user_stories", END)
# workflow.add_edge("create_user_stories", "write_generated_to_file")
# workflow.add_edge("write_generated_to_file", "write_generated_to_vector_store")
# workflow.add_edge("write_generated_to_vector_store", END)


# 

# compile
app = workflow.compile()

#draw graph
# 1. Get the raw PNG bytes from your LangGraph app
image_data = app.get_graph().draw_mermaid_png()

# 2. Save the bytes to a file
output_path = r"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\LLM-Optimization\langgraph_workflow.png"

with open(output_path, "wb") as f:
    f.write(image_data)

print(f"Workflow graph successfully saved to: {output_path}")


initial_state: GraphState = {
	"namespace": "requirements",
	"model": data["$model"],
	"requirements": None,
    "evaluation" :None,
	"filepath": r"C:\\Users\\OMNI BOOK\\OneDrive\\Personal-Projects\\Agent-Learning\\Dissertation-Project\\LLM-Optimization\\Data\\LLM_Outputs",
}

#uncomment to run app
final_state = app.invoke(initial_state)
serializable_state = {}
for key, value in final_state.items():
    if hasattr(value, "model_dump"):  # Check if it's a Pydantic v2 model
        serializable_state[key] = value.model_dump()
    elif hasattr(value, "dict"):      # Fallback for Pydantic v1 models
        serializable_state[key] = value.dict()
    else:
        serializable_state[key] = value
state_path = r"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\LLM-Optimization\States\final_state.json"
# 3. Open the file in text mode ("w") and dump the data cleanly
with open(state_path, "w", encoding="utf-8") as f:
    json.dump(serializable_state, f, indent=4)



data_path = r"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\LLM-Optimization\Data\Ground_truths\functional_requirements.csv"

# score_threshold = [0,0.6,0.7,0.8,0.9]
# for score in score_threshold:
# 	evaluate_user_stories(pc=pc,az=az,filepath=Path(data_path),type='Functional Requirements',score_threshold=score)

