from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from plan_and_execute.local_states._state_ import AgentState, OutputState
from plan_and_execute.agents.elicitation import generate_elicitation, ask_human
# from plan_and_execute.agents.planner import generate_plan


def create_graph():
    builder = StateGraph(AgentState, output_schema=OutputState)
    checkpointer = InMemorySaver()

    # Nodes
    builder.add_node("elicitation", generate_elicitation)
    builder.add_node("ask_human", ask_human)
    # builder.add_node("planner", generate_plan)

    # 2-Node HITL Flow: START -> elicitation -> ask_human -> END
    builder.add_edge(START, "elicitation")
    builder.add_edge("elicitation", "ask_human")
    builder.add_edge("ask_human", END)
    # builder.add_edge("ask_human", "planner")
    # builder.add_edge("planner", END)

    return builder.compile(checkpointer=checkpointer)


app = create_graph()
