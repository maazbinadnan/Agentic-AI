import json
import pickle
import pytest
from Functions.agent_functions import Agent_functions


def test_generate_user_stories_calls_parse(agent, fake_azure_client, sample_state):
    # configure fake response
    fake_azure_client.client.responses.out = {"generated": "requirements"}
    result = agent.generate_user_stories(sample_state)
    assert result == {"requirements": {"generated": "requirements"}}

    # parse should have been called once with a messages list
    assert len(fake_azure_client.client.responses.calls) == 1
    call = fake_azure_client.client.responses.calls[0]
    assert isinstance(call["input"], list)
    roles = [m["role"] for m in call["input"]]
    assert "system" in roles and "user" in roles


def test__generate_user_message_builds_tables(agent, sample_state):
    msg = agent._generate_user_message(sample_state)
    assert "Functional Requirements" in msg
    assert "Non-Functional Requirements" in msg
    assert "FR1" in msg
    assert "NFR1" in msg


def test_evaluate_user_stories_calls_parse_and_returns_evaluation(agent, fake_azure_client, sample_state, monkeypatch):
    # patch _generate_user_message to a deterministic value
    monkeypatch.setattr(Agent_functions, "_generate_user_message", lambda self, s: "USER_MESSAGE")
    fake_azure_client.client.responses.out = {"score": 0.8, "issues": []}

    result = agent.evaluate_user_stories(sample_state)
    assert result == {"evaluation": {"score": 0.8, "issues": []}}
    assert len(fake_azure_client.client.responses.calls) == 1
    call = fake_azure_client.client.responses.calls[0]
    assert isinstance(call["input"], list)


def test_revise_user_stories_serializes_state_before_call(agent, fake_azure_client, sample_state):
    fake_azure_client.client.responses.out = {"revised": "new requirements"}
    res = agent.revise_user_stories(sample_state)
    assert res == {"requirements": {"revised": "new requirements"}}

    # validate the message content sent was serialized to a string
    call = fake_azure_client.client.responses.calls[-1]
    assert isinstance(call["input"][1]["content"], str)
    assert '"requirements"' in call["input"][1]["content"]


def test_write_state_uses_pickle_dump(agent, monkeypatch, sample_state):
    # intercept pickle.dump to avoid disk write
    recorded = {}
    def fake_dump(obj, f):
        recorded['obj'] = obj

    monkeypatch.setattr(pickle, 'dump', fake_dump)
    agent.write_state(sample_state)
    assert recorded['obj'] == sample_state


def test_router(agent, sample_state):
    s = sample_state.copy()
    s["read_state"] = False
    assert agent.router(s) == "write_state"
    s["read_state"] = True
    assert agent.router(s) == "read_state"


def test_write_to_csv_prints_filenames(agent, capsys, sample_state):
    s = sample_state.copy()
    s["requirements"] = ["Functional", "NonFunctional"]
    s["model"] = "mymodel"
    agent.write_to_csv(s)
    captured = capsys.readouterr()
    assert "mymodel_Functional.csv" in captured.out
    assert "mymodel_NonFunctional.csv" in captured.out
