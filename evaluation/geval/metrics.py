"""DeepEval GEval metrics for evaluating Functional and Non-Functional Requirements."""

from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams
from evaluation.geval.azure_model import AzureOpenAIDeepEval


def create_functional_req_geval(model: AzureOpenAIDeepEval | None = None) -> GEval:
    """Create GEval metric for functional requirements evaluation."""
    return GEval(
        name="Functional Requirements Coverage & Quality",
        criteria=(
            "Evaluate the quality and coverage of generated functional requirements against expected ground truth requirements."
        ),
        evaluation_steps=[
            "Compare actual generated functional requirements against expected ground truth functional requirements.",
            "Check for completeness: are all key functional capabilities (login, live ticker, team statistics, live stream links, push notifications, social sharing) included?",
            "Check for clarity and atomicity: is each requirement clear, unambiguous, and focused on a single function?",
            "Check for correctness: are requirements accurately stated without introducing hallucinations or contradictions?",
        ],
        evaluation_params=[
            LLMTestCaseParams.INPUT,
            LLMTestCaseParams.ACTUAL_OUTPUT,
            LLMTestCaseParams.EXPECTED_OUTPUT,
        ],
        threshold=0.7,
        model=model or AzureOpenAIDeepEval(),
    )


def create_non_functional_req_geval(model: AzureOpenAIDeepEval | None = None) -> GEval:
    """Create GEval metric for non-functional requirements evaluation."""
    return GEval(
        name="Non-Functional Requirements Quality & Constraints",
        criteria=(
            "Evaluate the quality of generated non-functional requirements against expected quality constraints."
        ),
        evaluation_steps=[
            "Compare actual generated non-functional requirements against expected ground truth non-functional requirements.",
            "Check quality attributes coverage: does it address performance, security, usability, availability, and reliability?",
            "Check measurability: are constraints quantitative or verifiable?",
            "Check domain alignment: does it accurately reflect system operational constraints?",
        ],
        evaluation_params=[
            LLMTestCaseParams.INPUT,
            LLMTestCaseParams.ACTUAL_OUTPUT,
            LLMTestCaseParams.EXPECTED_OUTPUT,
        ],
        threshold=0.7,
        model=model or AzureOpenAIDeepEval(),
    )
