from global_layer.llm_client import get_llm
from dotenv import load_dotenv
import os, json
from pathlib import Path
from pydantic import BaseModel
from functools import lru_cache

load_dotenv()
# reused across all node calls
llm = get_llm()

# read from json
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


def _save_supervisor_review(review, output_dir: str = "output", filename: str = "supervisor_review.md") -> str:
    """Saves the Supervisor's review/feedback into a formatted Markdown file matching SupervisorReview schema.
    
    Parameters
    ----------
    review : Pydantic BaseModel, dict, or str
        The output from the Supervisor node.
    output_dir : str
        Target output directory.
    filename : str
        Name of the file to save (default: "supervisor_review.md").
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / filename

    lines = ["# Supervisor Review & Feedback\n"]

    if hasattr(review, "model_dump") or hasattr(review, "dict"):
        data = review.model_dump() if hasattr(review, "model_dump") else review.dict()

        verdict = data.get("verdict", "N/A")
        lines.append(f"## Overall Verdict: **{verdict}**\n")

        score = data.get("score") if "score" in data else (data.get("quality_score") or data.get("completeness_score"))
        if score is not None:
            lines.append(f"- **Quality Score:** {score}/5")

        phase = data.get("phase")
        if phase:
            lines.append(f"- **Next Execution Phase:** `{phase}`")

        lines.append("\n---\n")

        issues = data.get("issues", [])
        if issues:
            lines.append("## Identified Issues & Flaws:\n")
            for issue in issues:
                lines.append(f"- {issue}")
            lines.append("\n---\n")

        feedback = data.get("feedback") or data.get("actionable_feedback") or data.get("feedback_summary")
        if feedback:
            lines.append("## Detailed Feedback:\n")
            if isinstance(feedback, list):
                for item in feedback:
                    lines.append(f"- {item}")
            else:
                lines.append(str(feedback))
    else:
        lines.append(str(review))

    file_path.write_text("\n".join(lines), encoding="utf-8")
    print(f" Successfully saved supervisor review to '{file_path.resolve()}'")
    return str(file_path)