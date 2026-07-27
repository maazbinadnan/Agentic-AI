from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent

from ba_team_agent.tools import task
from ba_team_agent._common_ import llm,load_prompt


__all__ = ["create_agent_pipeline", "app"]



def create_agent_pipeline():
    """Creates the Main Task Dispatcher Agent using langchain.agents.create_agent exclusively."""
    # Register sub-agent tools into the dispatcher's registry
    tools = [task]
    checkpointer = InMemorySaver()

    dispatcher_prompt = load_prompt("dispatcher.md")

    dispatcher_graph = create_agent(
        model=llm,
        tools=tools,
        system_prompt=dispatcher_prompt,
        checkpointer=checkpointer,
        name="Main_BA_Task_Dispatcher_Agent",
    )
    return dispatcher_graph


app = create_agent_pipeline()
