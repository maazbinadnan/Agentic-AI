import os
from typing import Any, cast,List


from global_layer.AzureClient import ChatClient
from global_layer.functions import _write_json_file
from evaluation.confusion_matrix import get_ground_truths, get_generated
from evaluation.state.llm_judge_state import GroundTruthCoverageList, ISO29148EvaluationReport, INVESTEvaluationReport

# Resolve prompt path relative to this file (never hardcoded)
_EVAL_DIR = os.path.dirname(os.path.abspath(__file__))
SYSTEM_PROMPT = os.path.join(_EVAL_DIR, "prompts", "requirements_evaluator.md")
ISO_29148_PROMPT = os.path.join(_EVAL_DIR, "prompts", "iso_29148_auditor.md")
INVEST_PROMPT = os.path.join(_EVAL_DIR, "prompts", "invest_evaluator.md")

client = ChatClient().client


def evaluate_requirements(
    func_reqs: str,
    non_func_reqs: str,
    output_file: str,
    model: str | None = None,
):
    """Lean LLM Judge that evaluates generated requirements against ground truth."""
    model = model or os.getenv("EVAL_MODEL", "gpt-4.1")

    # Load system prompt
    with open(SYSTEM_PROMPT, "r", encoding="utf-8") as prompt:
        sys_prompt = prompt.read()

    ground_truth = get_ground_truths()
    generated_reqs = get_generated(func_reqs, non_func_reqs)

    user_message = f"""
        Please evaluate the generated functional and non-functional requirements against the ground truth requirements.

        ### GROUND TRUTH FUNCTIONAL REQUIREMENTS
        {ground_truth}
        
        ### GENERATED REQUIREMENTS WITH gen_fnr REPRESENTING FUNCTIONAL AND gen_nfnr REPRESENTING NON-FUNCTIONAL
        {generated_reqs}

"""
    messages = [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_message},
            ]
    
    response = client.responses.parse(
        model=model,
        input=cast(Any, messages),
        text_format=GroundTruthCoverageList
    )
    output_parsed = response.output_parsed
    if output_file:
        print(_write_json_file(output_file, output_parsed))
    return output_parsed


def evaluate_iso_29148_quality(
    func_reqs: str,
    non_func_reqs: str,
    output_file: str,
    model: str | None = None,
):
    """Evaluates generated requirements against ISO/IEC/IEEE 29148 quality standards (identifying requirement issues)."""
    model = model or os.getenv("EVAL_MODEL", "gpt-4.1")

    with open(ISO_29148_PROMPT, "r", encoding="utf-8") as prompt_file:
        sys_prompt = prompt_file.read()

    generated_reqs = get_generated(func_reqs, non_func_reqs)

    user_message = f"""
Please perform a structural quality audit on the generated functional and non-functional requirements statements according to ISO/IEC/IEEE 29148 standards:

### GENERATED REQUIREMENTS:
{generated_reqs}
"""

    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_message},
    ]

    response = client.responses.parse(
        model=model,
        input=cast(Any, messages),
        text_format=ISO29148EvaluationReport,
    )
    output_parsed = response.output_parsed
    if output_file:
        print(_write_json_file(output_file, output_parsed))
    return output_parsed


def evaluate_invest_user_stories(
    user_stories_file_or_text: str,
    output_file: str,
    model: str | None = None,
):
    """Evaluates Agile User Stories against the INVEST rubric (Independent, Negotiable, Valuable, Estimable, Small, Testable)."""
    model = model or os.getenv("EVAL_MODEL", "gpt-4.1")

    with open(INVEST_PROMPT, "r", encoding="utf-8") as prompt_file:
        sys_prompt = prompt_file.read()

    if os.path.isfile(user_stories_file_or_text):
        with open(user_stories_file_or_text, "r", encoding="utf-8") as f:
            stories_content = f.read()
    else:
        stories_content = user_stories_file_or_text

    user_message = f"""
Please evaluate the following Agile User Stories against the INVEST rubric (Independent, Negotiable, Valuable, Estimable, Small, Testable):

### USER STORIES TO EVALUATE:
{stories_content}
"""

    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_message},
    ]

    response = client.responses.parse(
        model=model,
        input=cast(Any, messages),
        text_format=INVESTEvaluationReport,
    )
    output_parsed = response.output_parsed
    if output_file:
        print(_write_json_file(output_file, output_parsed))
    return output_parsed