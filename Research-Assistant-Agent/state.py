from typing_extensions import TypedDict,Annotated
from langchain.messages import AnyMessage
import operator

class TaggerState(TypedDict):
    filepath: list[str]
    tagged_files: list[str]
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int



