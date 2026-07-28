from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from global_layer.functions import _draw_graph

from single_agent_2._common_ import llm, load_prompt
from single_agent_2.tools import save_report_file, save_html_mockup, read_file

__all__ = ["create_agent_pipeline", "app"]


def create_agent_pipeline():
    """Creates the Single Agent 2 pipeline using langchain.agents.create_agent."""
    tools = [save_report_file, save_html_mockup, read_file]
    checkpointer = InMemorySaver()

    system_prompt = load_prompt("single_agent_master.md")

    agent_graph = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
        checkpointer=checkpointer,
        name="Single_Agent_2",
    )
    return agent_graph

app = create_agent_pipeline()
