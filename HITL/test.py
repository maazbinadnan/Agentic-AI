from langgraph.types import interrupt, Command
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from typing_extensions import TypedDict

class State(TypedDict):
    input: str
    user_feedback: str

def step_1(state):
    print("---Step 1---")
    pass

def human_feedback(state):
    print("---Waiting for human feedback---")
    
    # This pauses execution and waits for input
    feedback = interrupt("Please provide feedback:")
    
    return {"user_feedback": feedback}

def step_3(state):
    print("---Step 3---")
    pass


builder = StateGraph(State)
builder.add_node("step_1", step_1)
builder.add_node("human_feedback", human_feedback)
builder.add_node("step_3", step_3)

builder.add_edge(START, "step_1")
builder.add_edge("step_1", "human_feedback")
builder.add_edge("human_feedback", "step_3")
builder.add_edge("step_3", END)

# Checkpointer is required for interrupts
memory = InMemorySaver()
graph = builder.compile(checkpointer=memory)


initial_input = {"input": "hello world"}
thread = {"configurable": {"thread_id": "1"}}

# Run until interrupt
for event in graph.stream(initial_input, thread, stream_mode="updates"):
    print(event)
    print("\n")