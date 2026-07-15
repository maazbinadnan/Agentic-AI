from typing import TypedDict,Annotated
from pydantic import BaseModel, Field
import operator
from langchain.messages import AnyMessage

class userStory(BaseModel):
    user_story: str = Field(
        description="The user story corresponding to the current requirement with a user story and an acceptance criteria expressed as Behaviour Driven Development Given  Given-When-Then statements"
    )
class functional_requirement(BaseModel):
    requirement_no: str = Field(
        description=(
            "The unique ID. Strictly use 'FR-XXX' for Functional and 'NFR-XXX' "
            "for Non-Functional."
        )
    )

    requirement_text: str = Field(description="The testable requirement statement.")

    requirement_reference: str = Field(
        description=(
            "What original line in the user research was this requirement "
            "extracted from"
        )
    )
    user_story: userStory

class non_functional_requirement(BaseModel):
    requirement_no: str = Field(
        description=(
            "The unique ID. Strictly use 'FR-XXX' for Functional and 'NFR-XXX' "
            "for Non-Functional."
        )
    )

    requirement_text: str = Field(description="The testable requirement statement.")

    requirement_reference: str = Field(
        description=(
            "What original line in the user research was this requirement "
            "extracted from"
        )
    )
    user_story: userStory
class output_format(BaseModel):
    thinking: str = Field(
        description="CRITICAL: Your step-by-step thinking scratchpad. This must be populated first to break down the text, map out candidates, de-duplicate requirements, and plan BDD scenarios before generating the lists."
    )
    functional_reqs: list[functional_requirement] | None
    non_functional_reqs: list[non_functional_requirement] | None

class GraphState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add] | None
    model:str
    requirements_filepath:str
    think_file : str
    output_functional_path:str
    output_non_functional_path:str
