from typing import TypedDict, List, Annotated, Optional, Literal
from langchain_core.messages import AnyMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    input: str
    output_dir: str
    ba_output: Optional[dict]
    ixd_output: Optional[dict]
    phase: Literal["ba", "ixd", "completed", "END"]

class OutputState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    input: str
    output_dir: str
    phase: Literal["ba", "ixd", "completed", "END"]
