from global_layer.llm_client import get_llm
from dotenv import load_dotenv
import os, json
from pathlib import Path
from pydantic import BaseModel


load_dotenv()
# reused across all node calls
llm = get_llm()

#read from json
config_path = Path(__file__).parent / "config.json"
if config_path.exists():
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    PROMPTS_DIR = Path(config["prompts_dir"])
else:
    PROMPTS_DIR = Path(__file__).parent / "prompts"


def _outputs_dir() -> str:
    """Return (and create) the Outputs directory for this module."""
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(d, exist_ok=True)
    return d

def _session_dir(run_number:str) -> str:
    """Create and return a timestamped session subdirectory inside outputs/."""
    d = os.path.join(_outputs_dir(), f"{run_number}")
    os.makedirs(d, exist_ok=True)
    return d

def load_prompt(prompt_name: str) -> str:
    """Load a prompt template from the ``prompts/`` directory."""
    prompt_path = os.path.join(PROMPTS_DIR, prompt_name)
    with open(prompt_path, "r", encoding="utf-8") as fh:
        return fh.read()

def save_state(state: dict):
    """Saves the graph execution state to a JSON file."""
    path = Path(state["output_dir"]) / "state.json"
    path.parent.mkdir(parents=True, exist_ok=True)

    # Helper serializer for Pydantic models or non-serializable objects
    def default_serializer(obj):
        if isinstance(obj, BaseModel):
            return obj.model_dump(by_alias=True)
        if hasattr(obj, "dict"):
            return obj.dict()
        return str(obj)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, default=default_serializer)

    print(f"State saved successfully to '{path.resolve()}'")