from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent

from hitl_agent.tools import task
from hitl_agent._common_ import llm,load_prompt,read_file
from global_layer.llm_client import get_llm

llm= get_llm("gpt-5.4-mini")

__all__ = ["create_agent_pipeline", "app"]

def create_agent_pipeline():
    """Creates the Main Task Dispatcher Agent using langchain.agents.create_agent exclusively."""
    # Register sub-agent tools into the dispatcher's registry
    tools = [task,read_file]
    checkpointer = InMemorySaver()

    dispatcher_prompt = load_prompt("dispatcher.md")

    dispatcher_graph = create_agent(
        model=llm,
        tools=tools,
        system_prompt=dispatcher_prompt,
        checkpointer=checkpointer,
        name="Task_Dispatcher_Agent",
    )
    return dispatcher_graph


app = create_agent_pipeline()
