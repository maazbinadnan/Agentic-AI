In the global layer of the project, we use the openAI SDK to natively call models. 

## Dummy Runs Before Real Calls

Run a deterministic dry-run (no real API calls):

```powershell
python -m self_refinement.main --mode dummy
```

Run with real model calls:

```powershell
python -m self_refinement.main --mode real
```

Run automated tests for the dummy flow:

```powershell
pytest tests/unit/test_self_refinement_dummy.py tests/integration/test_self_refinement_dummy_run.py -q
```