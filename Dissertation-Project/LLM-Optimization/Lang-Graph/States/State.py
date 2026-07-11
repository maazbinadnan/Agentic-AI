"""Module: State

Data model definitions for requirements outputs and the GraphState
TypedDict. Only documentation added; no functional changes.
"""

from typing import List, Literal, TypedDict,Annotated
from pydantic import BaseModel, Field
from pathlib import Path
import operator

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

    requirement_reasoning: str = Field(description="What reasoning is there for this requirements")

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

    requirement_reasoning: str = Field(description="What reasoning is there for this requirements")


class output_format(BaseModel):
    functional_reqs: List[functional_requirement]
    non_functional_reqs: List[non_functional_requirement]




class evaluator_table(BaseModel):
    original_requirement_id: str = Field(
        description= 'The original requirement ID generaated initially. Simply used for reference, do not change it'       
       )
    original_requirement_text: str = Field(
        description= 'The original requirement text generaated initially for the corresponding. Simply used for reference and evaluation, do not change it'       
       )
    
    issue_identified: str = Field(
        description= 'The issue identified by the agent for this requirement against the original requirements research text.'       
       )
    rewritten_requirement_text: str = Field(
        description= 'based on the error, how should it be rewritten'       
       )
    new_requirement_text: str = Field(
        description= 'If a new requirement that was missing from the original is needed then write it here'       
       )
    
class evaluator_output(BaseModel):
    evaluation :List[evaluator_table]
class GraphState(TypedDict):
    namespace: str
    model: str
    requirements: output_format | None
    evaluation: Annotated[evaluator_output, operator.add] | None
    filepath: str
    read_state: bool
