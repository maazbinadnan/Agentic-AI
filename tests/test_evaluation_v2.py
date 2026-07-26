import pytest
from evaluation_v2.deterministic_eval import (
    evaluate_bdd_syntax,
    scan_ambiguous_words,
    compute_redundancy_score,
    evaluate_deterministic_metrics,
    evaluate_ixd_mockups,
    evaluate_traceability,
    evaluate_system_efficiency,
)


def test_evaluate_bdd_syntax_valid():
    text = "Given the user is logged in, when they click submit, then the order is placed."
    assert evaluate_bdd_syntax(text) is True


def test_evaluate_bdd_syntax_invalid():
    text = "The system should work fast and be user-friendly."
    assert evaluate_bdd_syntax(text) is False


def test_scan_ambiguous_words():
    text = "The application must be fast, seamless, and user-friendly with robust scaling."
    count, freq = scan_ambiguous_words(text)
    assert count >= 4
    assert "fast" in freq
    assert "seamless" in freq


def test_compute_redundancy_score():
    s1 = "The user can view live match results in real time."
    s2 = "The user can view live match results in real time."
    score = compute_redundancy_score([s1, s2])
    assert score == 1.0


def test_evaluate_deterministic_metrics():
    sample_data = [
        {
            "user_story": "Story 1",
            "acceptance_criteria": "Given a user on home page, when they click news, then news is displayed."
        },
        {
            "user_story": "Story 2",
            "acceptance_criteria": "The system should be fast and easy to use."
        }
    ]
    metrics = evaluate_deterministic_metrics(sample_data)
    assert metrics.total_requirements == 2
    assert metrics.bdd_compliant_count == 1
    assert metrics.bdd_compliance_percentage == 50.0
    assert metrics.ambiguous_words_found >= 2


def test_evaluate_ixd_mockups():
    sample_ixd = {
        "mockup_files": {
            "files": [
                {
                    "html_filename": "login.html",
                    "html_content": "<html><body><form><input type='text'/><button>Submit</button></form></body></html>"
                }
            ]
        },
        "mapping_table": {
            "mapping_table": [
                {"html_file": "login.html", "user_stories": ["US-001", "US-002"]}
            ]
        },
        "tradeoffs": {
            "table": [
                {"tradeoff_name": "Modal vs Page", "tradeoff_data": "Decided page"}
            ]
        }
    }
    metrics = evaluate_ixd_mockups(sample_ixd, total_user_stories_count=2)
    assert metrics.total_mockup_files == 1
    assert metrics.buttons_count == 1
    assert metrics.inputs_count == 1
    assert metrics.containers_count == 1
    assert metrics.mapped_stories_count == 2
    assert metrics.story_mapping_coverage_percentage == 100.0


def test_evaluate_system_efficiency():
    sample_state = {
        "iterations": {"ba": 1, "ixd": 2},
        "feedback_history": [{"phase": "ba", "feedback": "Fix FR-1"}, {"phase": "ixd", "feedback": "Add button"}],
        "verdict": "APPROVED"
    }
    metrics = evaluate_system_efficiency(sample_state)
    assert metrics.total_iterations == 3
    assert metrics.ba_iterations == 1
    assert metrics.ixd_iterations == 2
    assert metrics.feedback_rounds_count == 2
    assert metrics.verdict == "APPROVED"
