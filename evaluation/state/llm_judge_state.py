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


class INVESTScores(BaseModel):
    independent: float = Field(description="Score between 0.0 and 1.0 for Independent criterion (I)")
    negotiable: float = Field(description="Score between 0.0 and 1.0 for Negotiable criterion (N)")
    valuable: float = Field(description="Score between 0.0 and 1.0 for Valuable criterion (V)")
    estimable: float = Field(description="Score between 0.0 and 1.0 for Estimable criterion (E)")
    small: float = Field(description="Score between 0.0 and 1.0 for Small criterion (S)")
    testable: float = Field(description="Score between 0.0 and 1.0 for Testable criterion (T)")


class SingleUserStoryINVESTEvaluation(BaseModel):
    us_id: str = Field(description="Unique identifier for the user story (e.g. US-001)")
    user_story: str = Field(description="Text of the user story")
    scores: INVESTScores = Field(description="INVEST scores each rated between 0.0 and 1.0")
    reasoning: str = Field(description="Detailed technical explanation for the scores")

class INVESTEvaluationReport(BaseModel):
    evaluations: List[SingleUserStoryINVESTEvaluation]


# =============================================================================
# ACCS (Acceptance Criteria Coverage Score) Models
# =============================================================================

class AcceptanceCriterion(BaseModel):
    criterion_id: str = Field(
        description="Unique identifier for the acceptance criterion, e.g. 'AC-001-1' or 'a_1'"
    )
    scenario: str = Field(
        default="",
        description="Scenario title or contextual summary"
    )
    given: str = Field(
        default="",
        description="Preconditions / initial context (Given clause)"
    )
    when: str = Field(
        default="",
        description="User action / event trigger (When clause)"
    )
    then: str = Field(
        default="",
        description="Expected result / assertion (Then clause)"
    )
    statement: str = Field(
        description="Complete discrete, testable acceptance criterion statement"
    )


class UserStoryDecomposition(BaseModel):
    us_id: str = Field(
        description="Unique identifier for the user story (e.g. US-001)"
    )
    user_story: str = Field(
        description="Text of the user story statement"
    )
    acceptance_criteria: List[AcceptanceCriterion] = Field(
        default_factory=list,
        description="List of discrete, testable acceptance criteria A = {a_1, a_2, ..., a_n}"
    )


class CriterionVerification(BaseModel):
    criterion_id: str = Field(
        description="Identifier of the criterion a_i being verified"
    )
    criterion_statement: str = Field(
        description="Text of the acceptance criterion"
    )
    verification_score: float = Field(
        description="Verification score v(a_i, C, D) in {0.0, 0.5, 1.0}: 1.0=Full, 0.5=Partial, 0.0=None"
    )
    verdict: Literal["FULL", "PARTIAL", "NONE"] = Field(
        description="Categorical verdict: FULL (1.0), PARTIAL (0.5), or NONE (0.0)"
    )
    dom_evidence: str = Field(
        description="Concrete DOM evidence (elements, attributes, layout, forms, buttons) observed in rendered DOM D"
    )
    code_evidence: str = Field(
        description="Concrete code evidence (event handlers, JS logic, state mutations, functions) observed in generated code C"
    )
    reasoning: str = Field(
        description="Detailed explanation justifying the verification score"
    )


class UserStoryACCS(BaseModel):
    us_id: str = Field(
        description="Unique identifier for the user story (e.g. US-001)"
    )
    user_story: str = Field(
        description="Text of the user story"
    )
    criteria_count: int = Field(
        description="Total number of discrete acceptance criteria |A| = n for this user story"
    )
    sum_verification_score: float = Field(
        description="Sum of verification scores sum_{i=1}^n v(a_i, C, D)"
    )
    accs_score: float = Field(
        description="Acceptance Criteria Coverage Score ACCS = sum(v(a_i, C, D)) / |A|"
    )
    verifications: List[CriterionVerification] = Field(
        default_factory=list,
        description="Per-criterion verification evaluations v(a_i, C, D)"
    )


class ACCSEvaluationReport(BaseModel):
    total_user_stories: int = Field(
        description="Total number of user stories evaluated"
    )
    total_criteria_count: int = Field(
        description="Total number of discrete acceptance criteria evaluated across all user stories"
    )
    total_score_sum: float = Field(
        description="Sum of all verification scores across all criteria"
    )
    overall_accs: float = Field(
        description="Overall suite ACCS score = total_score_sum / total_criteria_count"
    )
    full_count: int = Field(
        description="Count of criteria with full implementation (score 1.0)"
    )
    partial_count: int = Field(
        description="Count of criteria with partial implementation (score 0.5)"
    )
    none_count: int = Field(
        description="Count of criteria with non-implementation (score 0.0)"
    )
    full_ratio: float = Field(
        description="Proportion of criteria with full implementation"
    )
    partial_ratio: float = Field(
        description="Proportion of criteria with partial implementation"
    )
    none_ratio: float = Field(
        description="Proportion of criteria with non-implementation"
    )
    evaluations: List[UserStoryACCS] = Field(
        default_factory=list,
        description="List of ACCS evaluations per user story"
    )
    