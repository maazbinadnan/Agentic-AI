from typing import Literal
from pydantic import BaseModel, Field
from typing import Optional

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

#metrics outputs
class RequirementMetrics(BaseModel):
    ground_truth_requirement: str = Field(
        description="The original ground truth requirement text being evaluated."
    )
    generated_requirements: Optional[str] = Field(
        default=None,
        description="The text of the generated requirement(s) that matched, or None if no match was found."
    )
    matched: bool = Field(
        description="True if the semantic meaning was completely captured, otherwise False."
    )
    matched_score: float = Field(
        description="The confidence score of the evaluation ranging from 0.0 to 1.0."
    )
    explanation: str = Field(
        description="Explicit reasoning detailing which generated requirement covered the meaning, or highlighting the exact nuance/constraint that was dropped."
    )

class MetricsReport(BaseModel):
    Metrics: list[RequirementMetrics] = Field(
        description="CRITICAL: An explicit 1:1 list containing the metrics for EVERY single input requirement. Do not truncate."
    )