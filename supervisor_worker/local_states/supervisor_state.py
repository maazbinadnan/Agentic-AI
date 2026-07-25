from pydantic import BaseModel, Field
from typing import List, Literal

class SupervisorReview(BaseModel):
    verdict: Literal["APPROVED_BA", "REVISE","APPROVED"]
    score: int = Field(ge=1, le=5, description="Overall quality score: 1=poor, 5=excellent")
    phase: Literal["ba","ixd"]  = Field(
        description= "the phase that should be executed based on the review status"
    )
    issues: List[str] = Field(
        default_factory=list,
        description="Specific issues found, each citing an ID (UN-XXX, FR-XXX, US-XXX, screen name, etc). Empty if approved with no notes."
    )
    feedback: str = Field(description="Detailed, actionable feedback. Cite specific IDs. If approving, briefly note strengths.")