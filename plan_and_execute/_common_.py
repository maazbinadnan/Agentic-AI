from global_layer.llm_client import get_llm
from dotenv import load_dotenv
import os, json
from pathlib import Path
from pydantic import BaseModel
from functools import lru_cache
from langgraph.types import Command

load_dotenv()
# reused across all node calls
llm = get_llm()

# read from config if exists
config_path = Path(__file__).parent / "config.json"
if config_path.exists():
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    p_dir = Path(config["prompts_dir"])
    PROMPTS_DIR = p_dir if p_dir.is_absolute() else (Path(__file__).parent / p_dir).resolve()
else:
    PROMPTS_DIR = Path(__file__).parent / "prompts"


def _outputs_dir() -> str:
    """Return (and create) the Outputs directory for this module."""
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(d, exist_ok=True)
    return d


def _session_dir(run_number: str) -> str:
    """Create and return a timestamped session subdirectory inside outputs/."""
    d = os.path.join(_outputs_dir(), f"{run_number}")
    os.makedirs(d, exist_ok=True)
    return d


@lru_cache(maxsize=32)
def load_prompt(prompt_name: str) -> str:
    """Load a prompt template from the prompts/ directory."""
    prompt_path = os.path.join(PROMPTS_DIR, prompt_name)
    with open(prompt_path, "r", encoding="utf-8") as fh:
        return fh.read()


def save_state(state: dict):
    """Saves the graph execution state to a JSON file."""
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

    print(f"State saved successfully to '{path.resolve()}'")


def answer_elicitation_qs(payload: dict) -> dict:
    """Prompts the user for elicitation clarifying questions from the interrupt payload and returns answers dict."""
    questions = payload.get("questions", []) if isinstance(payload, dict) else [payload]
    if not isinstance(questions, list):
        questions = [questions]

    print("\n=======================================================")
    print(f"[?] ELICITATION AGENT: {len(questions)} Ambiguity Question(s) Triggered")
    print("Please answer below (or press Enter to skip):")
    print("=======================================================\n")

    user_answers = {}
    for q in questions:
        q_id = q.get("id") if isinstance(q, dict) else getattr(q, "id", "Q-01")
        topic = q.get("topic") if isinstance(q, dict) else getattr(q, "topic", "General")
        text = q.get("question") if isinstance(q, dict) else getattr(q, "question", str(q))
        reason = q.get("context_reason") if isinstance(q, dict) else getattr(q, "context_reason", "")

        print(f"[{q_id}] Topic: {topic}")
        if reason:
            print(f"Context: {reason}")
        print(f"Question: {text}")
        answer = input("Your Answer > ").strip()
        if answer:
            user_answers[q_id] = answer
        else:
            user_answers[q_id] = "No response provided (Default assumptions applied)."
        print("-" * 55)

    return user_answers
