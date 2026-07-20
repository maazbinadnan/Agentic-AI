from typing import TypedDict,Annotated,Any,NotRequired
from pydantic import BaseModel, Field
import operator
from typing import Optional
from langchain.messages import AnyMessage

class userStory(BaseModel):
    story: str = Field(
        description="The user story corresponding to the current requirement with a user story"
    )
    Acceptance: str = Field(
        description="The acceptance criteria expressed as Behaviour Driven Development Given  Given-When-Then statements"
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

class regenerated_format(BaseModel):
    functional_reqs: list[functional_requirement] | None
    non_functional_reqs: list[non_functional_requirement] | None

# evaluation output format
class RequirementEvaluation(BaseModel):
    generated_requirements: str = Field(
        description="The text of the generated requirements that is being evaluated"
    )
    passed: bool = Field(
        description="True or False of whether the generated requirements passed the evaluation criteria or need redoing"
    )
    feedback: str = Field(
        description="Explicit reasoning detailing what problems were there in the requirement and what changes are needed"
    )
    action_to_take: str = Field(
        description="Explicit call to action as to what action needs to be taken"
    )
class EvaluationReport(BaseModel):
    evaluations: list[RequirementEvaluation] = Field(
        description="CRITICAL: An explicit 1:1 list containing an evaluation for EVERY single input requirement. Do not truncate."
    )

class GraphState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    evaluator_model:str
    generation_model:str
    requirements_filepath:str
    think_file : str
    output_functional_path:str
    output_non_functional_path:str
    feedback_path :str
    feedback : bool
    evaluation_count: int
    stop_requested: bool
    llm_client: NotRequired[Any]
