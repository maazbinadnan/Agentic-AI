from typing import TypedDict, List, Annotated, Optional
from langchain_core.messages import AnyMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    input: str
    output_dir: str
    ba_output: Optional[dict]
    ixd_output: Optional[dict]
    input_tokens: Annotated[int, operator.add]
    output_tokens: Annotated[int, operator.add]
    total_tokens: Annotated[int, operator.add]

class OutputState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    input: str
    output_dir: str
    ba_output: Optional[dict]
    ixd_output: Optional[dict]
    input_tokens: int
    output_tokens: int
    total_tokens: int