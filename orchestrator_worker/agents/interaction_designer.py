"""Interaction Designers Agent — designs HTML mockups from user stories.

Takes the formalised user stories and produces wireframe-level HTML
mockups covering the key screens and interactions.
"""

from orchestrator_worker.state.states import GlobalState,ixd_output
from typing import cast
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from orchestrator_worker.agents._common import llm, _save_output, load_prompt


def interaction_designers_node(state: GlobalState) -> dict:
    """IxD Team — design HTML mockups from the formalised user stories."""
    system_prompt = load_prompt("ixd_team.md")
    user_stories = state.get("user_stories", "")
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(
            content=(
                "Design HTML mockups based on the following user stories "
                "and acceptance criteria:\n\n"
                f"{user_stories}"
            )
        ),
    ]

    print("\n🎨 [INTERACTION DESIGNERS] Generating structured mockups & mapping...\n")

    # 1. Bind structured output schema to the LLM
    structured_llm = llm.with_structured_output(ixd_output)

    # 2. Invoke structured LLM (returns an instance of ixd_output)
    response = cast(ixd_output,structured_llm.invoke(messages))
    # _save_output(
    #         state=state,
    #         filename=f"ixd_full_response.md",
    #         content=cast(str,response)
    #     )
    
    saved_files = []

    # 3. Write each generated HTML mockup directly to disk
    for file_item in response.html_files:
        _save_output(
            state=state,
            filename=f"{file_item.file_name}",
            content=file_item.html
        )
        saved_files.append(file_item.file_name)

    # 4. Format structured architecture notes as clean Markdown text
    formatted_summary = (
        "## Interaction Design Overview\n\n"
        "### 1. Screen Architecture & Mapping\n"
        f"{response.html_mapping.architecture_mapping}\n\n"
        "### 2. UI/UX Design Notes & Trade-offs\n"
        f"{response.html_mapping.design_tradeoff}\n\n"
        "### 💾 Saved HTML Mockups\n"
        + "\n".join([f"- `{f}`" for f in saved_files])
    )

    # 5. Persist output artifact
    _save_output(state, "html_mockup_summary.md", formatted_summary, title="HTML Mockups")
    print("✅ Interaction Designers complete.\n")

    return {
        "messages": [
            AIMessage(content=f"[INTERACTION DESIGNERS]\n{formatted_summary}")
        ],
        "html_mockups": formatted_summary,
        "current_phase": "ixd_complete",
    }