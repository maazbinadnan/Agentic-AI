# LLM-Optimization

Overview
- Purpose: This subproject evaluates and optimizes prompts and evaluation workflows for large language model (LLM) outputs in the context of requirements extraction and evaluation. It provides tools to load datasets, run agents/pipelines, evaluate generated requirements against ground truth, and iterate on revisions.

Project structure
- `data_loader.py`: utilities to load datasets and evaluation CSVs used by the pipeline.
- `main.py`: main entry point for running experiments and orchestration of the LLM optimization flow.
- `Client_Layer/`
  - `AzureClient.py`: wrapper for interacting with Azure LLM services (prompt sending, responses).
  - `PineconeClient.py`: wrapper for interacting with Pinecone (vector storage/retrieval) used in retrieval-augmented workflows.
- `Data/`
  - `Requirements.md`: notes on dataset and requirements formatting.
  - `Evaluation_Data/`: CSVs containing model outputs under different evaluation thresholds.
  - `Ground_truths/`: CSVs with labeled functional and non-functional requirements used as ground truth.
  - `LLM_Outputs/`: example or saved outputs from LLM runs (e.g., GPT-4.1 outputs).
- `Functions/`
  - `agent_functions.py`: core functions used by agents to create, evaluate, and revise user stories or requirements.
  - `helper_functions.py`: small utilities and helpers used across the project.
- `Prompts/`
  - `evaluator_prompt.md`, `revise_prompt.md`, `system_prompt.md`: prompt templates used to drive evaluation and revision steps.
- `States/`
  - `final_state.json`, `state_before_evaluation.json`: example saved states for evaluation checkpoints.
  - `State.py`: data model and helpers for saving/loading pipeline state.
- `unit_tests/`
  - `conftest.py`, `test_agent_functions.py`: unit tests for core agent logic.

Goals and workflow
- Create user stories / requirement items using LLMs.
- Evaluate generated items against ground truth using scripted evaluation prompts.
- Iteratively revise items using revision prompts and re-evaluate.
- Persist pipeline state and outputs to allow analysis of changes across iterations.

Key libraries and tools
- `openai` / Azure OpenAI SDK (via `AzureClient.py`) — for LLM access.
- `pandas` — for CSV loading, processing, and evaluation metrics.
- `numpy` — numerical utilities used by evaluation code.
- `pinecone-client` or `pinecone` — vector DB client (via `PineconeClient.py`) for retrieval augmentation.
- `pytest` — for running unit tests under `unit_tests/`.
- (Optional) other ML/metrics libs like `scikit-learn` for precision/recall computations if present in the code.

How to run
1. Create and activate a Python virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Configure credentials/environment variables for Azure OpenAI and Pinecone as required (see `Client_Layer` files for exact env var names).
3. Run experiments or the main pipeline:

```powershell
python Dissertation-Project\LLM-Optimization\main.py
```

Notes and next steps
- Update `README.md` if new modules are added or clients change.
- Consider adding an example `env.example` listing required environment variables for quick setup.
- If you'd like, I can also add a short `requirements.txt` specific to this folder or a runnable example script.
