import pytest
from Functions.agent_functions import Agent_functions

class FakeResponse:
    def __init__(self, output_parsed):
        self.output_parsed = output_parsed

class FakeResponses:
    def __init__(self, out=None):
        self.out = out if out is not None else {"ok": True}
        self.calls = []

    def parse(self, model, input, text_format):
        # record call and return a FakeResponse
        self.calls.append({"model": model, "input": input, "text_format": text_format})
        return FakeResponse(self.out)

class FakeAzureClientWrapper:
    def __init__(self, response_out=None):
        self.client = type("C", (), {})()
        self.client.responses = FakeResponses(response_out)

class FakePineconeClientWrapper:
    def __init__(self):
        self.client = type("C", (), {})()


@pytest.fixture
def fake_azure_client():
    return FakeAzureClientWrapper(response_out={"parsed": "ok"})


@pytest.fixture
def fake_pinecone_client():
    return FakePineconeClientWrapper()


@pytest.fixture
def agent(fake_pinecone_client, fake_azure_client, monkeypatch):
    ag = Agent_functions(pinecone_client=fake_pinecone_client, azure_client=fake_azure_client)
    # patch read_md_file to return stable content and avoid file I/O
    monkeypatch.setattr(Agent_functions, "_read_md_file", lambda self, filepath: f"CONTENT FOR {filepath}")
    return ag


@pytest.fixture
def sample_state():
    return {
        "model": "test-model",
        "requirements": {
            "functional_reqs": [
                {"requirement_no": "FR1", "requirement_text": "Do X", "requirement_reference": "sourceA"}
            ],
            "non_functional_reqs": [
                {"requirement_no": "NFR1", "requirement_text": "Be fast", "requirement_reference": "sourceB"}
            ],
        },
        "filepath": ".",
        "read_state": False,
    }
