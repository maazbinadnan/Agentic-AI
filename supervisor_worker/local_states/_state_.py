from typing import TypedDict, List, Annotated,Optional,Literal
from langchain_core.messages import AnyMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    ba_output: Optional[dict]
    ixd_output:Optional[dict]
    supervisor_feedback: Optional[str]
    output_dir: str    
    input: str
    phase: Literal["ba","ixd"] 
    iteration_count: int
    max_iterations: int
    verdict: Optional[str]

class OutputState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    output_dir: str    
    input: str
    phase: Literal["ba","ixd"] 
    iteration_count: int
    max_iterations: int
    verdict: Optional[str]