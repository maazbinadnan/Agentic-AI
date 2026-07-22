"""Final Compiler — assembles all artefacts into a consolidated report.

Combines the original research, BA user stories, and IxD HTML mockups
into a single polished Markdown document.  Also saves each HTML mockup
as a separate file named by its user story number (e.g. ``1_mockup.html``).
"""
from pathlib import Path
from orchestrator_worker.state.states import GlobalState, CompilerExtraction
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
from langchain.tools import tool
from orchestrator_worker.agents._common import llm, _stream_llm, _save_output, load_prompt

@tool
def write_file(filename: str, content: str, output_folder: str) -> str:
    """Writes text or code content to a specified output file/directory.

    Args:
        filename: The name of the file to save (e.g., 'user_needs.md or e.g 1_login.html').
        content: The text, markdown, or HTML content to write inside the file.
        output_folder: The directory path where the file should be saved.

    Returns:
        A success or failure status message.
    """
    try:
        base_dir = Path(output_folder)
        base_dir.mkdir(parents=True, exist_ok=True)

        target_path = (base_dir / filename).resolve()

        # Security check: Prevent path traversal outside the target directory
        if not target_path.is_relative_to(base_dir.resolve()):
            return f"Error: Target path '{filename}' attempts to write outside directory '{output_folder}'."

        target_path.write_text(content, encoding="utf-8")
        return f"Successfully wrote {len(content)} characters to '{target_path}'"

    except Exception as e:
        return f"Failed to write file '{filename}': {str(e)}"


def compile(state:GlobalState):

    llm_with_tools = llm.bind_tools([write_file])

    user_stories = state['user_stories']
    html_mockups = state['html_mockups']


    system_prompt = load_prompt("compiler.md")

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(
            content=(
                f'''## User Stories \n
                {user_stories}  
                
                ##HTML Mockups \n
                {html_mockups} '''
            )
        ),
    ]

    response = llm_with_tools.invoke(messages)

    saved_files_log = []
    tool_messages = []

    if response.tool_calls:
        print("🛠️ Executing tool calls to write output files...\n")
        for tool_call in response.tool_calls:
            if tool_call["name"] == "write_file":
                # Execute the tool explicitly with args supplied by LLM
                result = write_file.invoke(tool_call["args"])
                tool_args = tool_call["args"]
                tool_args["output_folder"] = state['output_dir']
                print(f"  ✓ {result}")
                saved_files_log.append(result)
                # Append ToolMessage back for proper message chain tracking
                tool_messages.append(
                    ToolMessage(
                        content=result,
                        tool_call_id=tool_call["id"]
                    )
                )

    return {
        "messages": [response] + tool_messages,
        "final_output": "\n".join(saved_files_log),
        "current_phase": "completed",
    }


