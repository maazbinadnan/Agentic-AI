import json


class _FakeResponse:
    def __init__(self, payload: dict):
        self.output_text = json.dumps(payload)


class _FakeResponsesAPI:
    def parse(self, model: str, input: str, text_format):
        model_name = getattr(text_format, "__name__", "")

        if model_name == "output_format":
            return _FakeResponse(
                {
                    "thinking": "Dummy thinking for dry-run testing.",
                    "functional_reqs": [
                        {
                            "requirement_no": "FR-001",
                            "requirement_text": "System shall let user submit a request.",
                            "requirement_reference": "Dummy source line 1",
                            "user_story": {
                                "story": "As a user I submit a request.",
                                "Acceptance": "Given valid data When submit Then request is accepted",
                            },
                        }
                    ],
                    "non_functional_reqs": [
                        {
                            "requirement_no": "NFR-001",
                            "requirement_text": "System shall respond within 2 seconds.",
                            "requirement_reference": "Dummy source line 2",
                            "user_story": {
                                "story": "As a user I get fast responses.",
                                "Acceptance": "Given normal load When request Then response under 2 seconds",
                            },
                        }
                    ],
                }
            )

        if model_name == "regenerated_format":
            return _FakeResponse(
                {
                    "functional_reqs": [
                        {
                            "requirement_no": "FR-001",
                            "requirement_text": "System shall let user submit an improved request.",
                            "requirement_reference": "Dummy source line 1",
                            "user_story": {
                                "story": "As a user I submit an improved request.",
                                "Acceptance": "Given valid data When submit Then improved request is accepted",
                            },
                        }
                    ],
                    "non_functional_reqs": [
                        {
                            "requirement_no": "NFR-001",
                            "requirement_text": "System shall respond within 1.5 seconds.",
                            "requirement_reference": "Dummy source line 2",
                            "user_story": {
                                "story": "As a user I get very fast responses.",
                                "Acceptance": "Given normal load When request Then response under 1.5 seconds",
                            },
                        }
                    ],
                }
            )

        if model_name == "EvaluationReport":
            return _FakeResponse(
                {
                    "evaluations": [
                        {
                            "generated_requirements": "FR-001",
                            "passed": True,
                            "feedback": "Looks good for dummy evaluation.",
                            "action_to_take": "No changes needed",
                        }
                    ]
                }
            )

        raise ValueError(f"Unsupported text format in fake client: {model_name}")


class FakeLLMClient:
    def __init__(self):
        self.responses = _FakeResponsesAPI()
