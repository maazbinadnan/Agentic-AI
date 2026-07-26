from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class DeterministicMetrics(BaseModel):
    total_requirements: int = Field(description="Total number of generated requirements evaluated.")
    bdd_compliant_count: int = Field(description="Number of requirements meeting strict Given-When-Then BDD syntax.")
    bdd_compliance_percentage: float = Field(description="Percentage of requirements complying with BDD format (0-100%).")
    total_words: int = Field(description="Total word count across all generated requirements.")
    avg_word_count_per_requirement: float = Field(description="Average length in words per generated requirement.")
    ambiguous_words_found: int = Field(description="Total count of vague/ambiguous terms detected.")
    ambiguity_density_per_100_words: float = Field(description="Density of ambiguous words per 100 words.")
    redundancy_score: float = Field(description="Redundancy index (0.0 = completely distinct, 1.0 = highly redundant).")
    ambiguous_terms_breakdown: Dict[str, int] = Field(default_factory=dict, description="Frequency map of detected ambiguous words.")


class SingleRequirementAlignment(BaseModel):
    ground_truth_id: str = Field(description="The unique identifier or index of the ground truth requirement.")
    ground_truth_text: str = Field(description="The exact ground truth requirement text.")
    matched: bool = Field(description="True if the semantic meaning is captured in generated output, otherwise False.")
    match_score: float = Field(description="Semantic similarity score between 0.0 and 1.0.")
    matched_generated_requirement: Optional[str] = Field(default=None, description="The closest matching generated requirement text, or None.")
    explanation: str = Field(description="Detailed explanation highlighting captured meaning or missing constraints.")


class AlignmentReport(BaseModel):
    alignments: List[SingleRequirementAlignment] = Field(description="Per-ground-truth semantic alignment metrics.")
    recall: float = Field(description="Semantic Recall: fraction of ground truth requirements covered (0.0 - 1.0).")
    precision: float = Field(description="Semantic Precision: fraction of generated requirements matching ground truth (0.0 - 1.0).")
    macro_f1: float = Field(description="Harmonic mean of Recall and Precision.")


class GEvalRequirementEvaluation(BaseModel):
    requirement_id: str = Field(description="Identifier or number of the generated requirement.")
    requirement_text: str = Field(description="Text of the requirement evaluated.")
    invest_score: int = Field(description="INVEST criteria adherence score (1-5).")
    bdd_score: int = Field(description="BDD Given-When-Then quality score (1-5).")
    completeness_score: int = Field(description="Functional completeness and edge case coverage score (1-5).")
    feasibility_score: int = Field(description="Technical feasibility and realism score (1-5).")
    overall_score: int = Field(description="Final overall quality score (1-5).")
    feedback: str = Field(description="Actionable, critical feedback pinpointing flaws, missing constraints, or vagueness.")


class GEvalReport(BaseModel):
    evaluations: List[GEvalRequirementEvaluation] = Field(description="List of G-Eval rubric evaluations per requirement.")
    mean_invest_score: float = Field(description="Average INVEST score across all requirements.")
    mean_bdd_score: float = Field(description="Average BDD quality score across all requirements.")
    mean_completeness_score: float = Field(description="Average completeness score across all requirements.")
    mean_feasibility_score: float = Field(description="Average feasibility score across all requirements.")
    mean_overall_score: float = Field(description="Average overall score across all requirements.")


class IxDMetrics(BaseModel):
    total_mockup_files: int = Field(description="Total count of HTML mockup screen files generated.")
    total_interactive_components: int = Field(description="Total count of interactive DOM elements (buttons, inputs, forms, tables).")
    buttons_count: int = Field(description="Total count of button and link elements.")
    inputs_count: int = Field(description="Total count of form input and select elements.")
    containers_count: int = Field(description="Total count of form, table, section, and card layout containers.")
    story_mapping_coverage_percentage: float = Field(description="Percentage of User Stories mapped to at least one HTML mockup screen.")
    mapped_stories_count: int = Field(description="Count of user stories with mapped HTML mockups.")
    unmapped_stories_count: int = Field(description="Count of orphan user stories missing HTML mockups.")
    tradeoffs_count: int = Field(description="Count of documented UI/UX design tradeoffs.")


class TraceabilityMetrics(BaseModel):
    total_user_needs: int = Field(description="Total count of User Needs.")
    total_functional_reqs: int = Field(description="Total count of Functional Requirements.")
    total_user_stories: int = Field(description="Total count of User Stories.")
    matrix_entries_count: int = Field(description="Total rows in the traceability matrix.")
    matrix_completeness_percentage: float = Field(description="Percentage of User Needs mapped in the matrix.")


class SystemEfficiencyMetrics(BaseModel):
    total_iterations: int = Field(description="Total revision iterations across all phases.")
    ba_iterations: int = Field(description="Number of Business Analysis revision iterations.")
    ixd_iterations: int = Field(description="Number of Interaction Design revision iterations.")
    feedback_rounds_count: int = Field(description="Total feedback rounds logged in feedback_history.")
    verdict: Optional[str] = Field(default=None, description="Final supervisor verdict (Approved / Rejected).")


class EvaluationV2Summary(BaseModel):
    architecture_name: str = Field(description="Name of the multi-agent design pattern (e.g. Single Agent, Supervisor-Worker).")
    target_type: str = Field(description="Target requirement type (Functional vs Non-Functional).")
    deterministic_metrics: DeterministicMetrics = Field(description="Deterministic syntax and complexity metrics.")
    alignment_metrics: AlignmentReport = Field(description="Semantic recall, precision, and F1 metrics against ground truth.")
    g_eval_metrics: GEvalReport = Field(description="LLM-as-a-Judge G-Eval rubric scores and feedback.")
    ixd_metrics: Optional[IxDMetrics] = Field(default=None, description="Phase 2 HTML Mockup & IxD evaluation metrics.")
    traceability_metrics: Optional[TraceabilityMetrics] = Field(default=None, description="Requirements traceability matrix metrics.")
    system_metrics: Optional[SystemEfficiencyMetrics] = Field(default=None, description="Multi-agent iteration and efficiency metrics.")
