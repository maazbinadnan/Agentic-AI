# GEval Requirements Evaluation (`evaluation/geval`)

This folder implements custom requirement evaluations using DeepEval's **GEval** metric (`GEval`).

## Overview

**GEval** allows defining custom evaluation criteria using an LLM as a judge. In this project:
1. **Functional Requirements GEval (`create_functional_req_geval`)**: Evaluates generated functional requirements for completeness, clarity, atomicity, and correctness against ground truth user needs.
2. **Non-Functional Requirements GEval (`create_non_functional_req_geval`)**: Evaluates generated non-functional requirements for ISO quality attribute coverage (performance, security, usability, availability) and measurability against ground truth goals.

---

## Directory Structure

```
evaluation/geval/
├── __init__.py
├── azure_model.py                # DeepEvalBaseLLM wrapper for Azure OpenAI ChatClient
├── metrics.py                    # GEval metric definitions (functional & non-functional)
├── run_geval.py                  # Standalone runner script (CLI entrypoint)
├── test_requirements_geval.py    # Pytest evaluation suite for deepeval CLI
└── README.md                     # Documentation (this file)
```

---

## How to Run

### Method 1: Standalone Python Runner (Recommended for quick testing)

Run GEval on your agent's generated functional and non-functional requirement files:

```bash
python -m evaluation.geval.run_geval \
    --func-reqs hitl_agent/outputs/final_run/03_functional_requirements.md \
    --nfunc-reqs hitl_agent/outputs/final_run/04_non_functional_requirements.md \
    --agent hitl_run
```

**Output:**
- Interactive terminal console output showing scores, pass/fail status, and LLM reasoning.
- Output report saved to `evaluation/evals/<agent>/geval_report.json`.

---

### Method 2: DeepEval CLI / Pytest

Run using DeepEval's test runner:

```bash
deepeval test run evaluation/geval/test_requirements_geval.py
```

---

## Metric Configuration

Metrics are defined in [`evaluation/geval/metrics.py`](file:///c:/Users/OMNI%20BOOK/OneDrive%20-%20Lancaster%20University/MSc%20Dissertation/MSc%20Project/evaluation/geval/metrics.py):

```python
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams

functional_geval = GEval(
    name="Functional Requirements Coverage & Quality",
    criteria="Evaluate completeness, clarity, atomicity, and correctness...",
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ],
    threshold=0.7,
)
```
