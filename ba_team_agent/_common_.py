from global_layer.llm_client import get_llm
from dotenv import load_dotenv
import os, json
from pathlib import Path
from pydantic import BaseModel
from langchain.tools import tool

load_dotenv()

# Reused LLM client
llm = get_llm()


def _outputs_dir() -> str:
    """Return (and create) the outputs directory for ba_team_agent."""
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(d, exist_ok=True)
    return d


def _session_dir(run_number: str) -> str:
    """Create and return a session subdirectory inside outputs/."""
    d = os.path.join(_outputs_dir(), f"{run_number}")
    os.makedirs(d, exist_ok=True)
    return d


def load_prompt(filename: str) -> str:
    """Load a markdown system prompt from prompts/ directory."""
    prompt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts", filename)
    with open(prompt_path, "r", encoding="utf-8") as fh:
        return fh.read()


def save_state(state: dict):
    """Saves state dictionary to state.json."""
    path = Path(state["output_dir"]) / "state.json"
    path.parent.mkdir(parents=True, exist_ok=True)

    def default_serializer(obj):
        if isinstance(obj, BaseModel):
            return obj.model_dump()
        if hasattr(obj, "dict"):
            return obj.dict()
        return str(obj)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, default=default_serializer)

    print(f"[ba_team_agent] State saved successfully to '{path.resolve()}'")


@tool
def read_file(filename: str, output_dir: str = "outputs") -> str:
    """Reads a previously generated report file (e.g., '01_elicitation_report.md') from the session output directory.
    
    Parameters
    ----------
    filename : str
        Name of the file to read (e.g. '01_elicitation_report.md').
    output_dir : str
        Target output directory path containing the file.
    """
    file_path = Path(output_dir) / filename
    if not file_path.exists():
        if Path(filename).exists():
            return Path(filename).read_text(encoding="utf-8")
        return f"File '{filename}' not found in directory '{output_dir}'."
    return file_path.read_text(encoding="utf-8")
