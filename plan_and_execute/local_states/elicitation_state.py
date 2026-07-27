from typing import List, Optional
from pydantic import BaseModel, Field
from global_layer.ba_state import UserNeed

class ClarifyingQuestion(BaseModel):
    id: str = Field(
        description="Unique identifier for the question (e.g. 'Q-01', 'Q-02')."
    )
    topic: str = Field(
        description="The domain area or feature topic requiring clarification (e.g. 'Broadcast Rights', 'Offline Mode')."
    )
    question: str = Field(
        description="The clear, specific question posed to the stakeholder."
    )
    context_reason: str = Field(
        description="Explanation of why this detail is ambiguous or missing in the source text."
    )

class DiscoveredPersona(BaseModel):
    name: str = Field(description="Name or title of the user persona (e.g. 'Football Fan').")
    user_group_type: str = Field(description="Type of user group (All Users, Primary, Secondary).")
    description: str = Field(description="Core motivations and usage habits.")

class ElicitationOutput(BaseModel):
    has_ambiguities: bool = Field(
        description="True if critical ambiguities or missing details were identified in the source text."
    )
    personas: List[DiscoveredPersona] = Field(
        description="Target user personas discovered during elicitation."
    )
    user_needs: List[UserNeed] = Field(
        description="Initial set of high-level user needs extracted from the source document."
    )
    questions: List[ClarifyingQuestion] = Field(
        default_factory=list,
        description="Targeted clarifying questions to present to the user if ambiguities exist."
    )
