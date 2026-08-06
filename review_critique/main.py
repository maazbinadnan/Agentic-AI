"""Supervisor-Worker Agent — Pipeline definition using LangGraph StateGraph."""

from typing import TypedDict, Annotated, Sequence
import operator
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import BaseMessage, AIMessage

from review_critique.subagents.business_analyst import run_business_analyst
from review_critique.subagents.interaction_designer import run_interaction_designer

__all__ = ["create_agent_pipeline", "app", "PipelineState"]


class PipelineState(TypedDict, total=False):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    output_dir: str
    generator_model: str
    generator_input_tokens: Annotated[int, operator.add]
    generator_output_tokens: Annotated[int, operator.add]
    generator_total_tokens: Annotated[int, operator.add]
    eval_model: str
    eval_input_tokens: Annotated[int, operator.add]
    eval_output_tokens: Annotated[int, operator.add]
    eval_total_tokens: Annotated[int, operator.add]
    input_tokens: Annotated[int, operator.add]
    output_tokens: Annotated[int, operator.add]
    total_tokens: int


def business_analyst_node(state: PipelineState) -> dict:
    """LangGraph node that executes the Business Analyst reflection & improvement loop."""
    messages = state.get("messages", [])
    output_dir = state.get("output_dir", "outputs")

    if not messages:
        return {}

    first_msg = messages[0].content
    if isinstance(first_msg, list):
        first_msg = "\n".join([str(m) for m in first_msg])
    
    # Run the Business Analyst subagent runner
    m = run_business_analyst(task=first_msg, output_dir=output_dir)

    tot_in = m["generator_input_tokens"] + m["eval_input_tokens"]
    tot_out = m["generator_output_tokens"] + m["eval_output_tokens"]

    return {
        "messages": [AIMessage(content=f"Business Analyst subagent pipeline finished successfully with deliverables in {output_dir}.")],
        "generator_model": m["generator_model"],
        "generator_input_tokens": m["generator_input_tokens"],
        "generator_output_tokens": m["generator_output_tokens"],
        "generator_total_tokens": m["generator_total_tokens"],
        "eval_model": m["eval_model"],
        "eval_input_tokens": m["eval_input_tokens"],
        "eval_output_tokens": m["eval_output_tokens"],
        "eval_total_tokens": m["eval_total_tokens"],
        "input_tokens": tot_in,
        "output_tokens": tot_out,
    }


def interaction_designer_node(state: PipelineState) -> dict:
    """LangGraph node that executes the Interaction Designer reflection & improvement loop."""
    messages = state.get("messages", [])
    output_dir = state.get("output_dir", "outputs")

    if not messages:
        return {}

    first_msg = messages[0].content
    if isinstance(first_msg, list):
        first_msg = "\n".join([str(m) for m in first_msg])

    # Run the Interaction Designer subagent runner
    m = run_interaction_designer(task=first_msg, output_dir=output_dir)

    tot_in = m["generator_input_tokens"] + m["eval_input_tokens"]
    tot_out = m["generator_output_tokens"] + m["eval_output_tokens"]

    return {
        "messages": [AIMessage(content=f"Interaction Designer subagent pipeline finished successfully with deliverables in {output_dir}.")],
        "generator_model": m["generator_model"],
        "generator_input_tokens": m["generator_input_tokens"],
        "generator_output_tokens": m["generator_output_tokens"],
        "generator_total_tokens": m["generator_total_tokens"],
        "eval_model": m["eval_model"],
        "eval_input_tokens": m["eval_input_tokens"],
        "eval_output_tokens": m["eval_output_tokens"],
        "eval_total_tokens": m["eval_total_tokens"],
        "input_tokens": tot_in,
        "output_tokens": tot_out,
    }


def create_agent_pipeline():
    """Creates the Supervisor-Worker pipeline as a LangGraph StateGraph."""
    workflow = StateGraph(PipelineState)

    # Add nodes
    workflow.add_node("business_analyst", business_analyst_node)
    workflow.add_node("interaction_designer", interaction_designer_node)

    # Set workflow edges: START -> business_analyst -> interaction_designer -> END
    workflow.add_edge(START, "business_analyst")
    workflow.add_edge("business_analyst", "interaction_designer")
    workflow.add_edge("interaction_designer", END)

    checkpointer = InMemorySaver()
    return workflow.compile(checkpointer=checkpointer)


app = create_agent_pipeline()
