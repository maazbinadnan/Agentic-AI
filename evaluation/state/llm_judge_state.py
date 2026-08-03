from typing import List,Literal
from pydantic import BaseModel, Field


class MatchedGeneratedRequirement(BaseModel):
    gen_id: int = Field(
         description="Unique identifier for the generated requirement"
    )
    gen_requirement: str = Field(
         description="Text of the generated requirement"
    )
    gen_type: str = Field(
         description="Type/category of the generated requirement"
    )
    individual_coverage_role: str = Field(
         description="Explanation of what specific part this requirement covers"
    )


class GroundTruthCoverage(BaseModel):
    gt_id: int = Field(
         description="Unique identifier for the ground truth requirement"
    )
    ground_truth_requirement: str = Field(
         description="Text of the ground truth requirement"
    )
    ground_truth_type: str = Field(
         description="Type/category of the ground truth requirement"
    )
    matched_generated_requirements: List[MatchedGeneratedRequirement] = Field(
        default_factory=list,
        description="List of generated requirements that match this ground truth requirement",
    )
    coverage_verdict:Literal['FULL','PARTIAL','NONE']
    reasoning: str = Field(
         description="Detailed explanation for the coverage verdict"
    )

class GroundTruthCoverageList(BaseModel):
    coverage: List[GroundTruthCoverage]


class RequirementIssue(BaseModel):
    dimension: Literal["Singularity", "Unambiguity", "Testability", "Categorization", "Completeness"] = Field(
        description="The ISO 29148 quality dimension violated"
    )
    detected_issue: str = Field(
        description="Exact weak word or phrase causing the violation"
    )
    explanation: str = Field(
        description="Detailed explanation of why it violates ISO 29148"
    )
    suggested_fix: str = Field(
        description="Rewritten version of the requirement fixing the issue"
    )


class ISO29148RequirementEvaluation(BaseModel):
    gen_id: int = Field(
        description="Unique identifier of the generated requirement"
    )
    gen_requirement: str = Field(
        description="Original text of the generated requirement"
    )
    is_well_formed: bool = Field(
        description="True if passes all quality criteria without critical issues"
    )
    quality_score: float = Field(
        description="Quality score between 0.0 and 1.0"
    )
    issues: List[RequirementIssue] = Field(
        default_factory=list,
        description="List of detected requirement issues"
    )


class ISO29148EvaluationReport(BaseModel):
    evaluations: List[ISO29148RequirementEvaluation]
    