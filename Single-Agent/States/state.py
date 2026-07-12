from typing import TypedDict
from pydantic import BaseModel, Field


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

class output_format(BaseModel):
    functional_reqs: list[functional_requirement] | None
    non_functional_reqs: list[non_functional_requirement] | None

class GraphState(TypedDict):
    model:str
    filepath:str
    output_functional_path:str
    output_non_functional_path:str
