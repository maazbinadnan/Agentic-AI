from typing import TypedDict, List, Annotated, Optional, Literal, Dict
from langchain_core.messages import AnyMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    ba_output: Optional[dict]
    ixd_output: Optional[dict]
    supervisor_feedback: Optional[str]
    feedback_history: Annotated[List[dict], operator.add]
    output_dir: str    
    input: str
    phase: Literal["ba", "ixd", "completed", "END"] 
    iterations: Dict[str, int]
    max_iterations_per_phase: int
    verdict: Optional[str]

class OutputState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    output_dir: str    
    input: str
    phase: Literal["ba", "ixd", "completed", "END"] 
    iterations: Dict[str, int]
    max_iterations_per_phase: int
    verdict: Optional[str]