"""Shared utilities for the Three Amigos agent nodes.

Contains the LLM client, streaming helper, file-I/O helper, and prompt
loader that every agent imports.
"""

from three_amigos.States.state import ThreeAmigosState
from global_layer.llm_client import get_llm
from dotenv import load_dotenv
import os

load_dotenv()

# Module-level singleton — reused across all node calls
llm = get_llm()


# ─── Streaming Helper ───────────────────────────────────────────────────────

# ANSI colour codes for distinguishing agents in the terminal
_AGENT_COLOURS = {
    "SUPERVISOR":            "\033[96m",   # cyan
    "ELICITATION":           "\033[93m",   # yellow
    "REQUIREMENTS ENGINEER": "\033[92m",   # green
    "STORY WRITER":          "\033[95m",   # magenta
    "PRODUCT OWNER":         "\033[94m",   # blue
    "DEVELOPER":             "\033[91m",   # red
    "QA ENGINEER":           "\033[33m",   # dark yellow
    "CONSENSUS CHECK":       "\033[97m",   # white
    "FINAL COMPILER":        "\033[36m",   # dark cyan
}
_RESET = "\033[0m"


def _stream_llm(
    messages: list,
    *,
    agent_label: str,
) -> str:
    """Stream an LLM call, printing each token to the terminal in real time.

    Parameters
    ----------
    messages : list
        The message list to send to the LLM.
    agent_label : str
        A human-readable label printed above the streamed output
        (e.g. ``"SUPERVISOR"``).

    Returns
    -------
    str
        The full concatenated response text.
    """
    # Prefix match so labels like "PRODUCT OWNER (Round 2)" still get colour
    label_upper = agent_label.upper()
    colour = _AGENT_COLOURS.get(label_upper, "")
    if not colour:
        for key, val in _AGENT_COLOURS.items():
            if label_upper.startswith(key):
                colour = val
                break
    header = f"\n{colour}{'─' * 60}{_RESET}"
    header += f"\n{colour}  🤖  {agent_label}  (streaming…){_RESET}"
    header += f"\n{colour}{'─' * 60}{_RESET}\n"
    print(header, flush=True)

    chunks: list[str] = []
    for chunk in llm.stream(messages):
        token = chunk.content
        if token:
            print(f"{colour}{token}{_RESET}", end="", flush=True)
            chunks.append(token) #type:ignore

    # End the streamed block with a newline
    print(f"\n{colour}{'─' * 60}{_RESET}\n", flush=True)

    return "".join(chunks)


# ─── File I/O Helper ────────────────────────────────────────────────────────

# Auto-incrementing counter so output files sort chronologically
_file_counter: int = 0


def _save_output(
    state: ThreeAmigosState,
    filename: str,
    content: str,
    *,
    title: str | None = None,
) -> None:
    """Write *content* to a Markdown file inside the session output directory.

    Parameters
    ----------
    state : ThreeAmigosState
        Current graph state (used to read ``output_dir``).
    filename : str
        The file basename **without** a numeric prefix (e.g. ``"supervisor_analysis"``).
        A zero-padded counter is prepended automatically so that files sort in
        the order they were created.
    content : str
        The Markdown text to write.
    title : str, optional
        If provided, a ``# title`` heading is prepended to the file.
    """
    global _file_counter
    output_dir = state.get("output_dir", "")
    if not output_dir:
        return  # gracefully skip when no output dir is configured

    os.makedirs(output_dir, exist_ok=True)
    _file_counter += 1
    safe_name = filename.replace(" ", "_").lower()
    path = os.path.join(output_dir, f"{_file_counter:02d}_{safe_name}.md")

    body = ""
    if title:
        body += f"# {title}\n\n"
    body += content

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(body)

    print(f"💾  Saved → {path}")


# ─── Prompt Loader ───────────────────────────────────────────────────────────
PROMPTS_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "Prompts"
)


def load_prompt(prompt_name: str) -> str:
    """Load a prompt template from the ``Prompts/`` directory."""
    prompt_path = os.path.join(PROMPTS_DIR, prompt_name)
    with open(prompt_path, "r", encoding="utf-8") as fh:
        return fh.read()
