from typing import Literal
from pydantic import BaseModel, Field

class RequirementEvaluation(BaseModel):
    requirement_no: str = Field(
        description=(
            "The unique ID matching the input requirement exactly. "
            "Strictly use 'FR-XXX' for Functional and 'NFR-XXX' for Non-Functional."
        )
    )
    requirement_text: str = Field(
        description="The original testable requirement text being evaluated."
    )
    score: Literal[1, 2, 3, 4, 5] = Field(
        description="The evaluation score between 1 and 5 (1 = critical flaws, 5 = production-ready BDD syntax)."
    )
    feedback: str = Field(
        description=(
            "Detailed, highly critical, and actionable feedback. Pinpoint exact ambiguities, "
            "INVEST gaps, or missing BDD steps, and suggest specific technical improvements."
        )
    )

class EvaluationReport(BaseModel):
    evaluations: list[RequirementEvaluation] = Field(
        description="CRITICAL: An explicit 1:1 list containing an evaluation for EVERY single input requirement. Do not truncate."
    )