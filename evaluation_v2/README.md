# Multi-Agent Requirements Engineering & Interaction Design Evaluation Suite (`evaluation_v2`)

This directory contains the hybrid, multi-tiered evaluation framework for assessing generated software requirements and HTML wireframe mockups across multi-agent architectural design patterns (**Single Agent**, **Supervisor-Worker**, **Three Amigos**, **Orchestrator-Worker**, **Planning Agent**).

---

## 🏛️ Framework Overview

Evaluating AI-generated software requirements and UI mockups requires going beyond basic text matching. This framework implements a **4-Pillar Hybrid Evaluation Suite** combining deterministic NLP parsing, semantic information retrieval, calibrated G-Eval LLM judging, and multi-agent system efficiency tracking.

```
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │                       EVALUATION V2 FRAMEWORK PILLARS                        │
 ├───────────────────┬────────────────────┬──────────────────┬─────────────────┤
 │ Pillar 1: Determin│ Pillar 2: Semantic │ Pillar 3: G-Eval │ Pillar 4: IxD   │
 │ Metric Parsing    │ Alignment (F1)     │ Rubric Judging   │ Mockups & System│
 ├───────────────────┼────────────────────┼──────────────────┼─────────────────┤
 │ • BDD Regex Check │ • Semantic Recall  │ • INVEST Score   │ • DOM Components│
 │ • Ambiguity Density│ • Precision Score │ • BDD Quality    │ • Story Coverage│
 │ • Redundancy Index│ • Macro F1 Score   │ • Feasibility    │ • Total Iters   │
 └───────────────────┴────────────────────┴──────────────────┴─────────────────┘
```

---

## 📊 The 4 Evaluation Pillars

### 1. Deterministic Syntax & Structural Metrics (`deterministic_eval.py`)
*Zero-LLM bias, reproducible code analysis.*

- **BDD Syntax Compliance (%)**: Regex/AST parser checking sequential `GIVEN` $\rightarrow$ `WHEN` $\rightarrow$ `THEN` clause ordering in acceptance criteria.
- **Ambiguity Density (per 100 words)**: Standard IEEE 830 / ISO 29148 requirement ambiguity scanner counting non-verifiable terms (*fast*, *user-friendly*, *seamless*, *robust*, *etc.*).
- **Pairwise Redundancy Index (0.0 - 1.0)**: Computes mean Jaccard token similarity across generated user stories to detect duplicate or overlapping requirements.

### 2. Semantic Alignment & Retrieval Metrics (`llm_judge_eval.py`)
*1-to-1 semantic matching against Ground Truth benchmarks ([`Data/functional_requirements.json`](file:///c:/Users/OMNI%20BOOK/OneDrive%20-%20Lancaster%20University/MSc%20Dissertation/MSc%20Project/Data/functional_requirements.json)).*

- **Semantic Recall (Coverage)**:
  $$\text{Recall} = \frac{|\text{Ground Truth Requirements Covered}|}{|\text{Total Ground Truth Requirements}|}$$
- **Semantic Precision**:
  $$\text{Precision} = \frac{|\text{Valid Generated Requirements Matching Ground Truth}|}{|\text{Total Generated Requirements}|}$$
- **Macro F1-Score**: Harmonic mean of Precision and Recall.

### 3. Calibrated G-Eval Rubric Judging (`eval_g_eval_prompt.md`)
*Chain-of-Thought structured LLM evaluation.*

- **INVEST Criteria Score (1-5)**: Independent, Negotiable, Valuable, Estimable, Small, Testable.
- **BDD Quality Score (1-5)**: Precondition clarity, trigger specificity, expected state transitions.
- **Functional Scope & Completeness (1-5)**: Edge case coverage and fidelity to source document.
- **Technical Feasibility (1-5)**: Coherence and freedom from internal contradictions.

### 4. Phase 2 IxD Mockup & Multi-Agent System Metrics
*Wireframe parsing and multi-agent revision tracking.*

- **DOM Interactive Component Density**: Python standard library `html.parser` counts interactive tags (`<button>`, `<a href>`, `<input>`, `<select>`, `<form>`, `<table>`).
- **Story-to-Mockup Coverage (%)**: Percentage of generated User Stories mapped to at least one HTML mockup screen in the mapping matrix.
- **System Iteration & Efficiency**: Total revision iterations (`ba` + `ixd`), feedback rounds, and supervisor verdicts extracted from `state.json`.

---

## 📁 File & Module Structure

```
evaluation_v2/
├── README.md                          # This documentation file
├── __init__.py
├── prompts/
│   ├── eval_g_eval_prompt.md         # G-Eval rubric system prompt
│   └── metrics_alignment_prompt.md   # Semantic 1-to-1 match prompt template
├── states/
│   ├── __init__.py
│   └── state.py                       # Pydantic models for evaluation outputs
├── deterministic_eval.py             # BDD parser, ambiguity scanner, DOM parser, redundancy
├── llm_judge_eval.py                 # Semantic alignment (Recall/Precision/F1) & G-Eval judge
├── pipeline.py                       # Unified pipeline evaluator for single run output folders
├── runner.py                         # CLI batch matrix runner across all architectures
└── results/                          # Output directory for summary JSONs and comparative CSV
```

---

## 🚀 How to Run Evaluations

### 1. Run Pipeline on a Single Execution Output Folder

```powershell
python -m evaluation_v2.pipeline
```

### 2. Run Batch Comparative Matrix Across All Architectures

```powershell
python -m evaluation_v2.runner
```

This generates `evaluation_v2/results/architecture_comparison_matrix.csv` aggregating metrics side-by-side:

| Architecture | Total Reqs | BDD Compliance % | Ambiguity Density | Semantic Recall | Semantic Precision | Macro F1 | Mockup Files | Story Coverage % | Total Iterations | G-Eval Overall |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Single Agent Final** | 15 | 73.3% | 1.82 | 0.800 | 0.850 | 0.824 | 3 | 66.7% | 1 | 3.8 |
| **Supervisor Worker** | 16 | 93.8% | 0.35 | 0.933 | 0.933 | 0.933 | 7 | 100.0% | 3 | 4.6 |

### 3. Run Automated Unit Tests

```powershell
.venv\Scripts\python.exe -m pytest tests/test_evaluation_v2.py -v
```

---

## 📄 Output Schema (`eval_summary.json`)

Each pipeline run saves a structured JSON summary matching `EvaluationV2Summary`:

```json
{
  "architecture_name": "Supervisor Worker",
  "target_type": "Functional",
  "deterministic_metrics": {
    "total_requirements": 16,
    "bdd_compliant_count": 15,
    "bdd_compliance_percentage": 93.75,
    "ambiguity_density_per_100_words": 0.35,
    "redundancy_score": 0.12
  },
  "alignment_metrics": {
    "recall": 0.9333,
    "precision": 0.9333,
    "macro_f1": 0.9333
  },
  "g_eval_metrics": {
    "mean_invest_score": 4.5,
    "mean_bdd_score": 4.8,
    "mean_overall_score": 4.6
  },
  "ixd_metrics": {
    "total_mockup_files": 7,
    "total_interactive_components": 34,
    "story_mapping_coverage_percentage": 100.0,
    "mapped_stories_count": 16
  },
  "system_metrics": {
    "total_iterations": 3,
    "feedback_rounds_count": 2,
    "verdict": "APPROVE"
  }
}
```
