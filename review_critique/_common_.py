from global_layer.llm_client import get_llm
from dotenv import load_dotenv
import os, json
from pathlib import Path
from pydantic import BaseModel
from functools import lru_cache
from langchain.tools import tool

load_dotenv()

# Reused LLM client across all tool calls
llm = get_llm()

# Resolve prompts directory — uses supervisor_worker's prompts (same files, no duplication)
PROMPTS_DIR = (Path(__file__).resolve().parent / "prompts")


def _outputs_dir() -> str:
    """Return (and create) the outputs directory for supervisor_worker_agent."""
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(d, exist_ok=True)
    return d


def _session_dir(run_number: str) -> str:
    """Create and return a session subdirectory inside outputs/."""
    d = os.path.join(_outputs_dir(), f"{run_number}")
    os.makedirs(d, exist_ok=True)
    return d


@lru_cache(maxsize=32)
def load_prompt(prompt_name: str) -> str:
    """Load a prompt template from the supervisor_worker prompts/ directory."""
    prompt_path = PROMPTS_DIR / prompt_name
    with open(prompt_path, "r", encoding="utf-8") as fh:
        return fh.read()

def save_state(state: dict):
    """Saves state dictionary to state.json."""
    path = Path(state["output_dir"]) / "state.json"
    path.parent.mkdir(parents=True, exist_ok=True)

    def default_serializer(obj):
        if isinstance(obj, BaseModel):
            return obj.model_dump(by_alias=True)
        if hasattr(obj, "dict"):
            return obj.dict()
        return str(obj)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, default=default_serializer)

    print(f"[supervisor_worker_agent] State saved successfully to '{path.resolve()}'")
