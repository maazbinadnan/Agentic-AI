import os
import json
import re
from typing import Any
from pathlib import Path

from global_layer.ba_state import RequirementsPipelineOutput
from global_layer.ixd_state import IxdPipelineOutput

DATA_FILE = r"Data\dataset3\requirements.md"

def _read_file(filepath:str):
    """Read and return the contents of a Markdown file.
    Returns a string with an error message on failure.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file at '{filepath}' was not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
def _write_json_file(filepath: str, content: Any):
    """Writes content (dict, list, Pydantic model, or JSON string) to a JSON file safely.
    
    Returns a success message on completion, or an error message on failure.
    """
    try:
        target_dir = os.path.dirname(filepath)
        
        # Create the directory structure if it doesn't exist (does nothing if it exists)
        if target_dir:
            os.makedirs(target_dir, exist_ok=True)

        # 1. Convert Pydantic models automatically
        if hasattr(content, "model_dump"):
            content = content.model_dump()
        elif hasattr(content, "dict"):
            content = content.dict()

        # 2. Parse raw JSON strings to avoid double-encoding or markdown fences
        if isinstance(content, str):
            clean_str = re.sub(r"^```json\s*|```$", "", content.strip(), flags=re.MULTILINE).strip()
            try:
                content = json.loads(clean_str)
            except Exception:
                pass  # Keep as string if it's plain text
            
        with open(filepath, "w", encoding="utf-8") as file:
            formatted_json = json.dumps(content, indent=4, ensure_ascii=False, default=str)
            file.write(formatted_json)
        return f"wrote file {filepath} successfully"
    except FileNotFoundError:
        return f"Error: The directory for '{filepath}' was not found."
    except PermissionError:
        return f"Error: Permission denied when trying to write to '{filepath}'."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
def _draw_graph(graph,output_path = Path(__file__).resolve().parent/"graph.png"):
    image_bytes = graph.get_graph(xray=True).draw_mermaid_png() 
    # Save the binary data to a file
    with open(output_path, "wb") as f:
        f.write(image_bytes)       
    print(f"Graph successfully saved to {output_path}")

def _data_file(filepath:str = DATA_FILE):
    return _read_file(filepath)

## save initial requirement files
def _save__requirement_files(response: RequirementsPipelineOutput, output_dir: str = "output"):
    """Saves the components of RequirementsPipelineOutput into 5 distinct Markdown files.
    
    1. user_needs.md
    2. functional_requirements.md
    3. non_functional_requirements.md
    4. user_stories.md
    5. analysis_summary.md (Traceability, Gaps & Recommendations, Summary Stats)
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------------
    # 1. User Needs
    # ---------------------------------------------------------
    un_lines = ["# 1. High-Level User Needs\n"]
    for un in response.user_needs:
        un_lines.append(f"### {un.id}: {un.user_need}")
        un_lines.append(f"- **User Group Type:** {un.user_group_type}")
        un_lines.append(f"- **User Group:** {un.user_group}")
        un_lines.append(f"- **Demand Level:** {un.demand}")
        un_lines.append(f"- **User Journey Context:** {un.user_journey}\n")
    
    (out_path / "01_user_needs.md").write_text("\n".join(un_lines), encoding="utf-8")

    # ---------------------------------------------------------
    # 2. Functional Requirements
    # ---------------------------------------------------------
    fr_lines = ["# 2. Functional Requirements\n"]
    for fr in response.functional_requirements:
        fr_lines.append(f"### {fr.id}")
        fr_lines.append(f"- **Requirement:** {fr.requirement}")
        fr_lines.append(f"- **Source Need:** {fr.source}")
        fr_lines.append(f"- **Priority:** {fr.priority}\n")

    (out_path / "02_functional_requirements.md").write_text("\n".join(fr_lines), encoding="utf-8")

    # ---------------------------------------------------------
    # 3. Non-Functional Requirements
    # ---------------------------------------------------------
    nfr_lines = ["# 3. Non-Functional Requirements\n"]
    for nfr in response.non_functional_requirements:
        nfr_lines.append(f"### {nfr.id}")
        nfr_lines.append(f"- **Requirement:** {nfr.requirement}")
        nfr_lines.append(f"- **Source:** {nfr.source}")
        nfr_lines.append(f"- **Priority:** {nfr.priority}\n")

    (out_path / "03_non_functional_requirements.md").write_text("\n".join(nfr_lines), encoding="utf-8")

    # ---------------------------------------------------------
    # 4. User Stories & Acceptance Criteria
    # ---------------------------------------------------------
    us_lines = ["# 4. User Stories & Acceptance Criteria\n"]
    for us in response.user_stories:
        us_lines.append(f"### {us.id}")
        us_lines.append(f"**User Story:** {us.user_story}\n")
        us_lines.append(f"- **Source:** {us.source}")
        us_lines.append(f"- **Priority:** {us.priority}\n")
        
        us_lines.append("**Acceptance Criteria:**")
        for sc in us.acceptance_criteria:
            us_lines.append(f"- **Scenario: {sc.scenario}**")
            us_lines.append(f"  - **Given:** {sc.given}")
            us_lines.append(f"  - **When:** {sc.when}")
            us_lines.append(f"  - **Then:** {sc.then}")
        us_lines.append("")  # Empty newline

    (out_path / "04_user_stories.md").write_text("\n".join(us_lines), encoding="utf-8")

    # ---------------------------------------------------------
    # 5. Combined Analysis Summary (Matrix + Gaps + Stats)
    # ---------------------------------------------------------
    summary_lines = ["# 5. Requirements Analysis & Summary\n"]

    # 5a. Traceability Matrix Table
    summary_lines.append("## Traceability Matrix\n")
    summary_lines.append("| User Need ID | Derived Requirements | Mapped User Stories | Primary Domain Area |")
    summary_lines.append("|---|---|---|---|")
    for row in response.traceability_matrix:
        reqs = ", ".join(row.derived_requirement_ids)
        stories = ", ".join(row.mapped_user_story_ids)
        summary_lines.append(
            f"| {row.user_need_id} | {reqs} | {stories} | {row.primary_domain_area} |"
        )
    summary_lines.append("\n---")

    # 5b. Gaps & Recommendations
    summary_lines.append("## Gaps & BA Recommendations\n")
    if response.gaps_and_recommendations:
        for gap in response.gaps_and_recommendations:
            summary_lines.append(f"### {gap.title}")
            summary_lines.append(f"- **Observation:** {gap.observation}")
            summary_lines.append(f"- **Recommendation:** {gap.recommendation}\n")
    else:
        summary_lines.append("No critical gaps or ambiguities identified.\n")
    summary_lines.append("---")

    # 5c. Summary Statistics
    stats = response.summary_statistics
    summary_lines.append("## Summary Statistics\n")
    summary_lines.append(f"- **Total Discovered User Needs:** {stats.total_user_needs}")
    summary_lines.append(f"- **Total Functional Requirements (FR):** {stats.total_functional_requirements}")
    summary_lines.append(f"- **Total Non-Functional Requirements (NFR):** {stats.total_non_functional_requirements}")
    summary_lines.append(f"- **Total User Stories (US):** {stats.total_user_stories}")
    summary_lines.append(f"- **User Needs Coverage:** {stats.user_needs_coverage}\n")
    
    summary_lines.append("### Priority Breakdown")
    summary_lines.append(f"- **High:** {stats.priority_breakdown.high}")
    summary_lines.append(f"- **Medium:** {stats.priority_breakdown.medium}")
    summary_lines.append(f"- **Low:** {stats.priority_breakdown.low}\n")

    (out_path / "05_analysis_summary.md").write_text("\n".join(summary_lines), encoding="utf-8")

    print(f" Successfully saved all 5 markdown files to '{out_path.resolve()}'")



## function to save files
def _save_ixd_files(
    ixd_output: IxdPipelineOutput, output_dir: str = "output"
) -> list[str]:
    """Saves generated HTML mockups into an 'html' subfolder and writes ixd_design_notes.md."""
    base_path = Path(output_dir)
    html_dir = base_path / "html"
    html_dir.mkdir(parents=True, exist_ok=True)

    saved_files = []

    # 1. Save HTML Mockup Files
    for item in ixd_output.mockup_files.files:
        filename = item.html_filename
        if not filename.endswith(".html"):
            filename += ".html"

        file_path = html_dir / filename
        file_path.write_text(item.html_content, encoding="utf-8")
        saved_files.append(str(file_path))

    # 2. Save Mapping Table & Design Trade-offs
    md_lines = ["# Interaction Design (IxD) & Mockup Specifications\n"]

    md_lines.append("## HTML Mockups to User Stories Mapping\n")
    md_lines.append(
        "| HTML File | Mapped User Stories | Visualizations / Components |"
    )
    md_lines.append("|---|---|---|")

    for row in ixd_output.mapping_table.mapping_table:
        stories = ", ".join(row.user_stories)
        visuals = ", ".join(row.visualizations)
        md_lines.append(f"| `{row.html_file}` | {stories} | {visuals} |")

    md_lines.append("\n---\n")

    md_lines.append("## UI/UX Design Decisions & Trade-offs\n")
    for row in ixd_output.tradeoffs.table:
        md_lines.append(f"### {row.tradeoff_name}")
        md_lines.append(f"{row.tradeoff_data}\n")

    notes_path = base_path / "ixd_design_notes.md"
    notes_path.write_text("\n".join(md_lines), encoding="utf-8")
    saved_files.append(str(notes_path))

    return saved_files


def _compile_deliverables(state, architecture_name: str = "Multi-Agent System") -> dict:
    """Compiles INDEX.md and exports HTML mockups into final_deliverables/ inside state['output_dir']."""
    output_dir = Path(state["output_dir"])
    final_dir = output_dir / "final_deliverables"
    final_dir.mkdir(parents=True, exist_ok=True)

    ba_output = state.get("ba_output") or {}
    ixd_output = state.get("ixd_output") or {}

    index_lines = [
        "# Master Requirements & Design Package\n",
        "## Executive Summary\n",
        f"This deliverable package contains the Requirements Specification and Interaction Design mockups generated by the **{architecture_name}** pipeline.\n",
        "---\n",
        "## Package Index\n",
    ]

    # 1. BA Summary
    user_needs = ba_output.get("user_needs", [])
    user_stories = ba_output.get("user_stories", [])
    fr_count = len(ba_output.get("functional_requirements", []))
    nfr_count = len(ba_output.get("non_functional_requirements", []))

    index_lines.append("### 1. Requirements Specification")
    index_lines.append(f"- **Discovered User Needs:** {len(user_needs)}")
    index_lines.append(f"- **Functional Requirements:** {fr_count}")
    index_lines.append(f"- **Non-Functional Requirements:** {nfr_count}")
    index_lines.append(f"- **Agile User Stories:** {len(user_stories)}\n")

    # 2. IxD Summary
    mockup_files = ixd_output.get("mockup_files", {}).get("files", []) or ixd_output.get("mockup_files", {}).get("table", [])
    tradeoffs = ixd_output.get("tradeoffs", {}).get("table", [])

    index_lines.append("### 2. Interaction Design Mockups")
    index_lines.append(f"- **HTML Mockup Screens:** {len(mockup_files)}")
    index_lines.append(f"- **UI/UX Trade-off Decisions:** {len(tradeoffs)}\n")

    # Copy / save HTML mockups to final_deliverables folder if available
    if mockup_files:
        mockups_dir = final_dir / "mockups"
        mockups_dir.mkdir(exist_ok=True)
        for mockup in mockup_files:
            if isinstance(mockup, dict):
                file_name = mockup.get("file_name") or mockup.get("html_filename") or "mockup.html"
                code = mockup.get("html_code") or mockup.get("html_content") or ""
            else:
                file_name = getattr(mockup, "html_filename", "mockup.html")
                code = getattr(mockup, "html_content", "")
            (mockups_dir / file_name).write_text(code, encoding="utf-8")
        index_lines.append("HTML mockups have been exported to `./mockups/`\n")

    index_lines.append(f"---\n*Status: Deliverables Compiled via {architecture_name}*")

    (final_dir / "INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")
    print(f"[Compiler] Final deliverables compiled to '{final_dir.resolve()}'")

    return {
        "messages": [
            f"Workflow completed successfully. Deliverables packaged at '{final_dir.resolve()}'"
        ],
    }

def token_counter(response:dict,agent_name:str):
    raw_msg = response["raw"]
    usage = getattr(raw_msg, "usage_metadata", {}) or {}
    in_tokens = usage.get("input_tokens", 0)
    out_tokens = usage.get("output_tokens", 0)
    tot_tokens = usage.get("total_tokens", in_tokens + out_tokens)
    print(f"f{agent_name} Input Tokens: {in_tokens}, Output Tokens: {out_tokens}, Total: {tot_tokens}")
    return in_tokens,out_tokens,tot_tokens
