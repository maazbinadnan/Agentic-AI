from typing import List
from pydantic import BaseModel, Field, ConfigDict
from pathlib import Path
from typing import Union


# ==========================================
# 1. HTML Mockups to User Stories Mapping
# ==========================================
class MappingRow(BaseModel):
    """Maps a single generated HTML mockup file to its underlying User Stories and visual elements."""

    html_file: str = Field(
        alias="HTML_file",
        description="Name of the HTML file (e.g., 'login.html')",
        examples=["login.html"],
    )
    user_stories: List[str] = Field(
        alias="UserStory",
        description="List of User Story IDs covered by this mockup (e.g., ['US-001', 'US-002'])",
        examples=[["US-001"]],
    )
    visualizations: List[str] = Field(
        alias="Visualizations",
        description="Key UI components or visualizations present in the layout",
        examples=[["Login form", "OAuth buttons", "Remember me checkbox"]],
    )


class MappingTable(BaseModel):
    """Container for the full HTML mockup mapping matrix."""

    mapping_table: List[MappingRow] = Field(
        alias="Mapping_Table",
        description="List of mapping entries between HTML files and User Stories",
    )


# ==========================================
# 2. UI/UX Design Notes & Trade-offs
# ==========================================
class TradeoffRow(BaseModel):
    """Represents a specific UI/UX design decision and its associated trade-off."""

    tradeoff_name: str = Field(
        alias="tradeoffname",
        description="Name or title of the UI/UX design trade-off (e.g., 'Modal vs. Dedicated Page')",
    )
    tradeoff_data: str = Field(
        alias="tradeoffdata",
        description="Detailed rationale, pros/cons, and impact on usability/performance",
    )


class TradeoffTable(BaseModel):
    """Container for all UI/UX design trade-off considerations."""

    

    table: List[TradeoffRow] = Field(
        alias="table",
        description="List of design trade-off decisions made during mocking",
    )


# ==========================================
# 3. HTML Mockup Files
# ==========================================
class HtmlMockupFile(BaseModel):
    """Represents an individual HTML mockup file."""

    html_filename: str = Field(
        alias="html_filename",
        description="Target filename (e.g., 'dashboard.html')",
    )
    html_content: str = Field(
        alias="html_content",
        description="Complete raw HTML code including inline CSS/JS or modern tailwind/bootstrap CDN references",
    )


class HtmlMockupFiles(BaseModel):
    """Container for all generated HTML mockup files."""

    files: List[HtmlMockupFile] = Field(
        alias="table",
        description="List of generated HTML mockup files",
    )


# ==========================================
# Master IxD Output Container
# ==========================================
class IxdPipelineOutput(BaseModel):
    """Master output container for the Interaction Design (IxD) generation phase."""

    mapping_table: MappingTable = Field(
        alias="mapping_table",
        description="Mapping matrix of HTML files to User Stories",
    )
    tradeoffs: TradeoffTable = Field(
        alias="tradeoffs",
        description="UI/UX design decisions and trade-offs",
    )
    mockup_files: HtmlMockupFiles = Field(
        alias="mockup_files",
        description="Generated HTML code files",
    )
