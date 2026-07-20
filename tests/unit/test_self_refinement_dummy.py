import json
from pathlib import Path

from self_refinement.functions import generate_requirements, evaluate_requirements


def _state(tmp_path: Path) -> dict:
    req_file = tmp_path / "requirements.md"
    req_file.write_text(
        "User can create a request.\nSystem should be fast.",
        encoding="utf-8",
    )

    return {
        "messages": [],
        "requirements_filepath": str(req_file),
        "think_file": str(tmp_path / "thinking.json"),
        "output_functional_path": str(tmp_path / "functional.json"),
        "output_non_functional_path": str(tmp_path / "non_functional.json"),
        "feedback_path": str(tmp_path / "feedback.json"),
        "generation_model": "gpt-4.1",
        "evaluator_model": "gpt-5.4",
        "feedback": False,
        "evaluation_count": 0,
        "stop_requested": False,
        "llm_mode": "dummy",
    }


def test_generate_requirements_dummy_writes_outputs(tmp_path: Path):
    state = _state(tmp_path)

    result = generate_requirements(state)

    assert len(result["messages"]) >= 1
    assert Path(state["think_file"]).exists()
    assert Path(state["output_functional_path"]).exists()
    assert Path(state["output_non_functional_path"]).exists()


def test_evaluate_requirements_dummy_writes_feedback(tmp_path: Path):
    state = _state(tmp_path)
    generate_requirements(state)

    result = evaluate_requirements(state)

    assert result["feedback"] is True
    assert result["evaluation_count"] == 1

    feedback = json.loads(Path(state["feedback_path"]).read_text(encoding="utf-8"))
    assert "evaluations" in feedback
    assert isinstance(feedback["evaluations"], list)
