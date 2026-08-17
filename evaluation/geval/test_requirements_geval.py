"""Pytest test suite for GEval requirements evaluation.

Run with:
    deepeval test run evaluation/geval/test_requirements_geval.py
"""

import json
import os
import sys
import pytest

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from evaluation.geval.azure_model import AzureOpenAIDeepEval
from evaluation.geval.metrics import (
    create_functional_req_geval,
    create_non_functional_req_geval,
)


def load_file_content(path: str) -> str:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def get_ground_truths(project_root: str) -> tuple[str, str]:
    config_path = os.path.join(project_root, "evaluation", "config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    fnr_path = os.path.join(project_root, config["ground_fnr"])
    nfnr_path = os.path.join(project_root, config["ground_nfnr"])

    with open(fnr_path, "r", encoding="utf-8") as f:
        fnr_data = json.load(f)
    with open(nfnr_path, "r", encoding="utf-8") as f:
        nfnr_data = json.load(f)

    fnr_text = "\n".join([f"- {item['Requirement']}" for item in fnr_data if 'Requirement' in item])
    nfnr_text = "\n".join([f"- {item['Requirement']}" for item in nfnr_data if 'Requirement' in item])

    return fnr_text, nfnr_text


# Load test cases dynamically
EVAL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(EVAL_DIR)

FUNC_ACTUAL = load_file_content(os.path.join(PROJECT_ROOT, "hitl_agent", "outputs", "final_run", "03_functional_requirements.md"))
NFUNC_ACTUAL = load_file_content(os.path.join(PROJECT_ROOT, "hitl_agent", "outputs", "final_run", "04_non_functional_requirements.md"))
FUNC_EXPECTED, NFUNC_EXPECTED = get_ground_truths(PROJECT_ROOT)

model = AzureOpenAIDeepEval()


@pytest.mark.parametrize(
    "input_prompt, actual_output, expected_output, metric_creator",
    [
        (
            "Extract functional requirements",
            FUNC_ACTUAL,
            FUNC_EXPECTED,
            create_functional_req_geval,
        ),
        (
            "Extract non-functional requirements",
            NFUNC_ACTUAL,
            NFUNC_EXPECTED,
            create_non_functional_req_geval,
        ),
    ],
)
def test_geval_requirements(input_prompt, actual_output, expected_output, metric_creator):
    """Test functional and non-functional requirements using G-Eval."""
    test_case = LLMTestCase(
        input=input_prompt,
        actual_output=actual_output,
        expected_output=expected_output,
    )
    metric = metric_creator(model=model)
    assert_test(test_case=test_case, metrics=[metric])
