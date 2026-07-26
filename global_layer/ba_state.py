from typing import List, Literal
from pydantic import BaseModel, Field


# ==========================================
# 1. High-Level User Needs (Phase 1)
# ==========================================
class UserNeed(BaseModel):
    """Phase 1: High-level RE User Needs specification."""

    id: str = Field(
        default="UN-001",
        description="Unique identifier for the user need (e.g., 'UN-001')",
    )
    user_group_type: Literal["Overarching", "Primary", "Secondary"] = Field(
        alias="UserGroupType",
        description="Categorization of the targeted user group",
    )
    user_group: str = Field(
        alias="UserGroup",
        description="Name or role of the target group (e.g., 'Store Manager')",
    )
    user_need: str = Field(
        alias="UserNeed",
        description="High-level need statement (e.g., 'I need to view daily sales reports')",
    )
    demand: Literal["High", "Medium", "Low"] = Field(
        alias="Demand", description="Priority or demand level of the need"
    )
    user_journey: str = Field(
        alias="UserJourney",
        description="Summary of the user journey or process context",
    )


# ==========================================
# 2. Functional Requirements (Phase 2)
# ==========================================
class FunctionalRequirement(BaseModel):
    """Phase 2: Functional Requirement derived from User Needs."""

    

    id: str = Field(
        default="FR-001",
        description="Unique identifier for the functional requirement (e.g., 'FR-001')",
    )
    requirement: str = Field(
        description="Detailed functional requirement statement specifying system behavior"
    )
    source: str = Field(
        description="Identifier of the source User Need (e.g., 'UN-001')"
    )
    priority: Literal["High", "Medium", "Low"] = Field(
        description="Priority ranking for implementation"
    )


# ==========================================
# 3. Non-Functional Requirements (Phase 3)
# ==========================================
class NonFunctionalRequirement(BaseModel):
    """Phase 3: Non-Functional Requirement (quality attributes, security, performance, etc.)."""

    

    id: str = Field(
        default="NFR-001",
        description="Unique identifier for the non-functional requirement (e.g., 'NFR-001')",
    )
    requirement: str = Field(
        description="Quality, performance, security, or constraint requirement"
    )
    source: str = Field(
        description="Identifier of the source User Need or FR (e.g., 'UN-001')"
    )
    priority: Literal["High", "Medium", "Low"] = Field(
        description="Priority ranking for compliance"
    )


# ==========================================
# 4. User Stories & Acceptance Criteria (Phase 4)
# ==========================================
class _Scenario(BaseModel):
    """Gherkin-style Acceptance Criteria Scenario (Private to module)."""

    

    scenario: str = Field(
        alias="Scenario",
        description="Brief description of the test scenario",
    )
    given: str = Field(
        description="Precondition state before action (e.g., 'Given I am logged in as Admin')"
    )
    when: str = Field(
        description="Action triggered by the user (e.g., 'When I click Export PDF')"
    )
    then: str = Field(
        description="Expected outcome or system state (e.g., 'Then the report downloads automatically')"
    )


class UserStory(BaseModel):
    """Phase 4: Agile User Story with linked BDD Acceptance Criteria."""

    

    id: str = Field(
        default="US-001",
        description="Unique identifier for the user story (e.g., 'US-001')",
    )
    user_story: str = Field(
        alias="User_story",
        description="Agile user story in format: 'As a <role>, I want <goal> so that <benefit>'",
    )
    source: str = Field(
        alias="Source",
        description="Identifier of the source FR or User Need (e.g., 'FR-001')",
    )
    priority: Literal["High", "Medium", "Low"] = Field(
        alias="Priority", description="Agile backlog priority ranking"
    )
    acceptance_criteria: List[_Scenario] = Field(
        alias="AcceptanceCriteria",
        description="List of Gherkin scenarios forming the definition of done",
    )


# ==========================================
# 5. Requirements & Story Traceability Matrix (Phase 5)
# ==========================================
class TraceabilityEntry(BaseModel):
    """A single row mapping a User Need to its derived Requirements and Stories."""

    

    user_need_id: str = Field(
        alias="UserNeedID",
        description="ID of the source User Need (e.g., 'UN-001')",
    )
    derived_requirement_ids: List[str] = Field(
        alias="DerivedRequirementIDs",
        description="List of derived FR and NFR IDs (e.g., ['FR-001', 'NFR-001'])",
    )
    mapped_user_story_ids: List[str] = Field(
        alias="MappedUserStoryIDs",
        description="List of mapped User Story IDs (e.g., ['US-001', 'US-002'])",
    )
    primary_domain_area: str = Field(
        alias="PrimaryDomainArea",
        description="Domain or functional area (e.g., 'Authentication', 'Reporting')",
    )


# ==========================================
# 6. Gaps & BA Recommendations (Phase 6)
# ==========================================
class GapRecommendation(BaseModel):
    """An identified gap, ambiguity, or recommendation for stakeholders."""

    

    title: str = Field(
        alias="Title",
        description="Concise title for the gap or ambiguity",
    )
    observation: str = Field(
        alias="Observation",
        description="Detailed description of missing info, edge cases, or ambiguous business rules",
    )
    recommendation: str = Field(
        alias="Recommendation",
        description="Suggested question or recommended action for stakeholders",
    )


# ==========================================
# 7. Summary Statistics (Phase 7)
# ==========================================
class PriorityBreakdown(BaseModel):
    """Quantitative count breakdown by priority/demand level."""

    

    high: int = Field(default=0, alias="High", description="Count of High priority items")
    medium: int = Field(default=0, alias="Medium", description="Count of Medium priority items")
    low: int = Field(default=0, alias="Low", description="Count of Low priority items")


class SummaryStatistics(BaseModel):
    """Summary metrics of the generated requirements artifacts."""

    

    total_user_needs: int = Field(
        alias="TotalUserNeeds", description="Total count of UN items"
    )
    total_functional_requirements: int = Field(
        alias="TotalFunctionalRequirements", description="Total count of FR items"
    )
    total_non_functional_requirements: int = Field(
        alias="TotalNonFunctionalRequirements", description="Total count of NFR items"
    )
    total_user_stories: int = Field(
        alias="TotalUserStories", description="Total count of US items"
    )
    priority_breakdown: PriorityBreakdown = Field(
        alias="PriorityBreakdown", description="Priority counts across all artifacts"
    )
    user_needs_coverage: str = Field(
        alias="UserNeedsCoverage",
        description="Coverage fraction string (e.g., '5/5')",
    )


# ==========================================
# Master Pipeline Container Model
# ==========================================
class RequirementsPipelineOutput(BaseModel):
    """Master container schema for structured LLM generation across all 7 phases."""

    user_needs: List[UserNeed] = Field(
        description="Phase 1: High-level User Needs"
    )
    functional_requirements: List[FunctionalRequirement] = Field(
        description="Phase 2: Functional Requirements"
    )
    non_functional_requirements: List[NonFunctionalRequirement] = Field(
        description="Phase 3: Non-Functional Requirements"
    )
    user_stories: List[UserStory] = Field(
        description="Phase 4: Agile User Stories with BDD Acceptance Criteria"
    )
    traceability_matrix: List[TraceabilityEntry] = Field(
        alias="TraceabilityMatrix",
        description="Phase 5: Matrix mapping UN to FR/NFR and US",
    )
    gaps_and_recommendations: List[GapRecommendation] = Field(
        alias="GapsAndRecommendations",
        description="Phase 6: Identified gaps, ambiguities, and BA advice",
    )
    summary_statistics: SummaryStatistics = Field(
        alias="SummaryStatistics",
        description="Phase 7: Quantitative summary metrics of all generated artifacts",
    )