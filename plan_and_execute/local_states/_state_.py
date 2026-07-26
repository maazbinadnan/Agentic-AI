import operator
from typing import Annotated, Optional, TypedDict, Any, Dict
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    input: str
    output_dir: str
    plan_output: Optional[dict[str, Any]]
    elicitation_output: Optional[dict[str, Any]]
    user_clarifications: Optional[Dict[str, str]]
    messages: Annotated[list, add_messages]
    input_tokens: Annotated[int, operator.add]
    output_tokens: Annotated[int, operator.add]
    total_tokens: Annotated[int, operator.add]


class OutputState(TypedDict):
    plan_output: Optional[dict[str, Any]]
    elicitation_output: Optional[dict[str, Any]]
    user_clarifications: Optional[Dict[str, str]]
    output_dir: str
    messages: list
    input_tokens: int
    output_tokens: int
    total_tokens: int
