from typing import List, Literal
from pydantic import BaseModel, Field


class PlanStep(BaseModel):
    step_id: str = Field(
        description="Unique identifier for the step (e.g. 'STEP-01', 'STEP-02')."
    )
    re_phase: Literal["ELICITATION", "ANALYSIS", "SPECIFICATION", "VALIDATION"] = Field(
        description="The formal Requirements Engineering process phase for this step."
    )
    title: str = Field(
        description="Short concise title of the planned execution step."
    )
    task_description: str = Field(
        description="Detailed description of what the specialized worker must execute during this RE phase."
    )
    target_deliverable: Literal[
        "USER_NEEDS",
        "FUNCTIONAL_REQUIREMENTS",
        "NON_FUNCTIONAL_REQUIREMENTS",
        "USER_STORIES",
        "MOCKUP_MAPPING",
        "HTML_WIREFRAMES",
        "VALIDATION_REPORT"
    ] = Field(
        description="The target deliverable artifact type produced by this step."
    )
    dependencies: List[str] = Field(
        default_factory=list,
        description="List of step_ids that must be completed before this step can execute."
    )


class PlanOutput(BaseModel):
    project_summary: str = Field(
        description="High-level summary of the raw requirement scope and domain goals."
    )
    execution_strategy: str = Field(
        description="Strategic explanation of how the plan structures work across Elicitation, Analysis, Specification, and Validation."
    )
    steps: List[PlanStep] = Field(
        description="Ordered list of execution steps mapped to RE process phases forming a Directed Acyclic Graph (DAG)."
    )