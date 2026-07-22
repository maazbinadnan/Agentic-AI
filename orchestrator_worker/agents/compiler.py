"""Final Compiler — assembles all artefacts into a consolidated report.

Combines the original research, BA user stories, and IxD HTML mockups
into a single polished Markdown document.  Also saves each HTML mockup
as a separate file named by its user story number (e.g. ``1_mockup.html``).
"""

import os

from orchestrator_worker.state.states import GlobalState, CompilerExtraction
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from orchestrator_worker.agents._common import llm, _stream_llm, _save_output, load_prompt


def _save_html_mockups(state: GlobalState, extraction: CompilerExtraction) -> None:
    """Save each extracted story-mockup pair as a numbered HTML file."""
    output_dir = state.get("output_dir", "")
    if not output_dir:
        return

    mockups_dir = os.path.join(output_dir, "mockups")
    os.makedirs(mockups_dir, exist_ok=True)

    for item in extraction.story_mockups:
        filename = f"{item.story_number}_mockup.html"
        filepath = os.path.join(mockups_dir, filename)
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(item.html_content)
        print(f"💾  Saved mockup → {filepath}  (Story {item.story_number}: {item.story_title})")


def compile_final_output(state: GlobalState) -> dict:
    """Compiler — extract story-mockup pairs, save HTML files, assemble final report."""

    # ── Step 1: Extract individual story → mockup mappings ────────────────
    extraction_prompt = load_prompt("compiler_extraction.md")

    extraction_messages = [
        SystemMessage(content=extraction_prompt),
        HumanMessage(
            content=(
                f"## User Stories & Acceptance Criteria\n\n{state.get('user_stories', '')}\n\n"
                f"## HTML Mockups\n\n{state.get('html_mockups', '')}\n\n"
            )
        ),
    ]

    structured_llm = llm.with_structured_output(CompilerExtraction)
    extraction: CompilerExtraction = structured_llm.invoke(extraction_messages)

    _save_html_mockups(state, extraction)
    print(f"✅  Saved {len(extraction.story_mockups)} HTML mockup(s).")

    # ── Step 2: Compile the full report (streamed) ────────────────────────
    report_prompt = load_prompt("compiler.md")

    context = (
        f"## Original User Research\n\n{state['user_research']}\n\n"
        f"## User Stories & Acceptance Criteria\n\n{state.get('user_stories', '')}\n\n"
        f"## HTML Mockups\n\n{state.get('html_mockups', '')}\n\n"
    )

    report_messages = [
        SystemMessage(content=report_prompt),
        HumanMessage(content=context),
    ]

    response_text = _stream_llm(report_messages, agent_label="COMPILER")
    _save_output(state, "final_report", response_text, title="Final Coordinator Report")
    print("📄  Final report compiled.")

    return {
        "messages": [
            AIMessage(content=f"[FINAL OUTPUT]\n{response_text}")
        ],
        "final_output": response_text,
        "current_phase": "complete",
    }
