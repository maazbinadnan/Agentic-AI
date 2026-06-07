from model import base_model
from functions import openfile
from state import TaggerState
from langgraph.graph import StateGraph, START, END
from langchain.messages import SystemMessage, HumanMessage
import argparse


def tagger(state: dict):
    """LLM decides whether to call a tool or not"""

    return {
        "messages": [
            base_model.invoke(
                [
                    SystemMessage(
                        content="You are a helpful assistant tasked with extracting key topics from the given file contents"
                    )
                ]
                + state["messages"]
            )
        ],
        "llm_calls": state.get('llm_calls', 0) + 1
    }


## building the graph
#build the agent with the state graph
agent_builder = StateGraph(TaggerState)

#add node #1

agent_builder.add_node("read_file",openfile) 

#add node#2
agent_builder.add_node("tagger",tagger)

#add_edge
agent_builder.add_edge(START,"read_file")

#add_edge
agent_builder.add_edge("read_file","tagger")

#add_edge
agent_builder.add_edge("tagger",END)

agent = agent_builder.compile()

# from IPython.display import Image, display
# png_bytes = agent.get_graph(xray=True).draw_mermaid_png()

# with open("graph.png", "wb") as f:
#     f.write(png_bytes)

# print("Graph saved successfully as 'graph2.png'!")


def run_file_via_tagger(filepath: str):
    """Read `filepath`, wrap as a HumanMessage and invoke `tagger` to call the LLM."""
    content = openfile(filepath)
    # Build a minimal state expected by `tagger`
    state = {
        "filepath": [filepath],
        "tagged_files": [],
        "messages": [HumanMessage(content=content)],
        "llm_calls": 0,
    }

    result = tagger(state)
    # `tagger` returns a dict with an LLM invocation inside `messages`.
    print("LLM invocation result:")
    print(result)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Run the research assistant on a file")
    # parser.add_argument("filepath", help="Path to the file to process")
    # args = parser.parse_args()
    filepath ="C:\\Users\\OMNI BOOK\\OneDrive\\Personal-Projects\\Agent-Learning\\prompt.md"
    run_file_via_tagger(filepath)




