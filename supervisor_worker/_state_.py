from typing import TypedDict, List, Annotated
from langchain_core.messages import AnyMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    output_dir: str    
    input: str