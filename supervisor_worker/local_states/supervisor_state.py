from pydantic import BaseModel, Field
from typing import List, Literal

class SupervisorReview(BaseModel):
    verdict: Literal["APPROVE", "REVISE"] = Field(
        description="Return 'APPROVE' if quality standards are met, otherwise 'REVISE'"
    )
    completeness_score: str = Field(
        description="Rating from 1-10 on coverage of user needs, functional and non-functional requirements and if anything is missing"
    )
    traceability_passed: bool = Field(
        description="True if all User Needs are mapped to FRs and User Stories"
    )
    actionable_feedback: List[str] = Field(
        description="List of specific, actionable revision requests for the BA if verdict is REVISE"
    )