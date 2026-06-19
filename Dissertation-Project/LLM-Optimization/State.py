from typing import List, Literal,TypedDict
from pydantic import BaseModel, Field
from pathlib import Path

class output_requirement(BaseModel):
    requirement_no: str = Field(
        description="The unique ID. Strictly use 'FR-XXX' for Functional and 'NFR-XXX' for Non-Functional."
    )
    requirement_text: str = Field(
        description="The testable requirement statement."
    )
    requirement_reference: str = Field(
        description="What original line in the user research was this requirement extracted from"
    )
    requirement_reasoning: str = Field(
        description="What reasoning is there for this requirements"
    )

class output_format(BaseModel):
    requirement_type: Literal["Functional Requirements", "Non-Functional Requirements"] = Field(
        description="You MUST categorize everything into only these two types. Do not invent sub-categories."
    )
    requirements: List[output_requirement]

class output_format_final(BaseModel):
    final: List[output_format]

class GraphState(TypedDict):
    namespace: str
    model : str
    requirements: output_format_final | None
    filepath: Path
