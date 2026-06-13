from typing import TypedDict,Annotated
from operator import add
from pydantic import BaseModel
class UserStory(TypedDict):
    title:str
    content: str
    written: bool

class BusinessAnalystAgentState(TypedDict):
    filename:str
    user_research: str
    user_story: Annotated[list[UserStory],add]

class LLM_response(BaseModel):
    story_title:str
    story_content: str