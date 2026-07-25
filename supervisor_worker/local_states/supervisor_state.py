from pydantic import BaseModel, Field
from typing import List, Literal

class SupervisorReview(BaseModel):
    verdict: Literal["APPROVE", "REVISE"] = Field(
        description="Return 'APPROVE' if output meets quality standards, else 'REVISE'"
    )
    score: int = Field(ge=1, le=5, description="Overall quality score: 1=poor, 5=excellent")
    phase: Literal["ba", "ixd", "END"] = Field(
        description="The phase that should be executed next based on review status ('ba', 'ixd', or 'END')"
    )
    issues: List[str] = Field(
        default_factory=list,
        description="Specific issues found, each citing an ID (UN-XXX, FR-XXX, US-XXX, screen name, etc). Empty if approved with no notes."
    )
    feedback: str = Field(description="Detailed, actionable feedback. Cite specific IDs. If approving, briefly note strengths.")