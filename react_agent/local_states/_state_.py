import operator
from typing import Annotated, Optional, TypedDict, Any, Dict, List
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    input: str
    output_dir: str
    saved_reports: Annotated[List[str], operator.add]
    messages: Annotated[list, add_messages]
    input_tokens: Annotated[int, operator.add]
    output_tokens: Annotated[int, operator.add]
    total_tokens: Annotated[int, operator.add]


class OutputState(TypedDict):
    output_dir: str
    saved_reports: List[str]
    messages: list
    input_tokens: int
    output_tokens: int
    total_tokens: int
