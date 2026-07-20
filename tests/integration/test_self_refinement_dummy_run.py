from pathlib import Path

from self_refinement.main import _build_state, _build_workflow
from self_refinement.testing.fake_client import FakeLLMClient


def test_dummy_graph_run_end_to_end(tmp_path: Path):
    data_dir = tmp_path / "Data"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "requirements.md").write_text(
        "System should allow submissions and respond quickly.",
        encoding="utf-8",
    )

    project_root = tmp_path
    state = _build_state(project_root=project_root, run_number="test-run")
    state["llm_client"] = FakeLLMClient()

    app = _build_workflow(with_human_gate=False)
    result = app.invoke(state)

    assert result["feedback"] is True
    assert Path(state["think_file"]).exists()
    assert Path(state["output_functional_path"]).exists()
    assert Path(state["output_non_functional_path"]).exists()
    assert Path(state["feedback_path"]).exists()
