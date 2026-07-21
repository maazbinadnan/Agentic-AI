from self_refinement.states.state import GraphState,output_format,EvaluationReport, regenerated_format
from global_client_layer.AzureClient import ChatClient
from global_functions.functions import _read_file,_write_json_file
from langgraph.graph import END
from typing import cast, Any
from langgraph.types import interrupt,Command
import os
import json
from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"
prompt_file = str(PROMPTS_DIR / "initial_system_prompt.md")
refinement_prompt = str(PROMPTS_DIR / "refinement_prompt.md")
evaluator_prompt = str(PROMPTS_DIR / "evaluation_prompt.md")


def _resolve_client(state: GraphState) -> Any:
    """Resolve client without storing non-serializable objects in checkpointed state."""
    if state.get("llm_mode") == "dummy":
        from self_refinement.testing.fake_client import FakeLLMClient

        return FakeLLMClient()

    # Backward compatibility for non-checkpointed local tests.
    injected_client = state.get("llm_client")
    if injected_client is not None:
        return injected_client

    return ChatClient().client

#initial step to generate requirements
def generate_requirements(state:GraphState):
    '''read the md file and output user stories'''

    requirements = _read_file(state['requirements_filepath'])
    system_prompt = _read_file(prompt_file)

    print("generating user requirements")
    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": requirements},
        ]
    
    client = _resolve_client(state)
    response = client.responses.parse(model=state["generation_model"], input= cast(str,messages),text_format=output_format)
    reqs = json.loads(response.output_text)
    new_message = [{"role":"assistant","content":response.output_text}]

    #write all the files
    print(_write_json_file(state['think_file'],reqs['thinking']))
    print(_write_json_file(state['output_functional_path'],reqs['functional_reqs']))
    print(_write_json_file(state['output_non_functional_path'],reqs['non_functional_reqs']))
    return {"messages":messages + new_message} 


#initial step to re-generate requirements
def regenerate_requirements(state:GraphState):
    '''regenerate requirements based on the evaluation'''
    
    prompt = _read_file(refinement_prompt)
    # Read the files as strings
    functional_reqs = _read_file(state['output_functional_path'])
    non_functional_reqs = _read_file(state['output_non_functional_path'])
    feedback = _read_file(state['feedback_path'])

    # Format the user content string nicely so the LLM can distinguish them
    user_content = f"""
            ### 1. GENERATED FUNCTIONAL REQUIREMENTS
            {functional_reqs}

            ### 2. GENERATED NON-FUNCTIONAL REQUIREMENTS
            {non_functional_reqs}

            Please rewrite the requirements based on the feedback provided.
            """

    messages = [
        {
            "role": "system", 
            "content": prompt
        },
        {
            "role": "assistant", 
            "content": feedback
        },
        {
            "role": "user", 
            "content": user_content
        }
    ]

    client = _resolve_client(state)
    response = client.responses.parse(model=state["generation_model"], input= cast(str,messages),text_format=regenerated_format)
    reqs = json.loads(response.output_text)
    new_message = [{"role":"assistant","content":response.output_text}]

    #rewrite to new files

    func_dir, func_file = os.path.split(state['output_functional_path'])
    non_func_dir, non_func_file = os.path.split(state['output_non_functional_path'])

    # we peel back the last directory so they stack neatly as original/1, original/2,
    # rather than creating nested sub-hell original/1/2/3.
    if func_dir.split(os.sep)[-1].isdigit():
        func_dir = os.path.dirname(func_dir)
    if non_func_dir.split(os.sep)[-1].isdigit():
        non_func_dir = os.path.dirname(non_func_dir)

    #If count is 0, this loop generates folder '1', then '2', etc.
    next_version = str(state['evaluation_count'])
    new_func_path = os.path.join(func_dir, next_version, func_file)
    new_non_path = os.path.join(non_func_dir, next_version, non_func_file)

    #physically create the version directories on disk
    os.makedirs(os.path.dirname(new_func_path), exist_ok=True)
    os.makedirs(os.path.dirname(new_non_path), exist_ok=True)

    #Write payloads to the new paths, not the old ones
    _write_json_file(new_func_path, reqs['functional_reqs'])
    _write_json_file(new_non_path, reqs['non_functional_reqs'])

    
    return {
        "messages": new_message,
        "output_functional_path": new_func_path,
        "output_non_functional_path": new_non_path,
    }

#evaluate the requirements
def evaluate_requirements(state: GraphState):
    '''
    evaluate the initial user stories and give feedback to LLM to update the user stories
    '''
    prompt = _read_file(evaluator_prompt)
    # Read the files as strings
    functional_reqs = _read_file(state['output_functional_path'])
    non_functional_reqs = _read_file(state['output_non_functional_path'])
    original_source = _read_file(state['requirements_filepath'])

    # Format the user content string nicely so the LLM can distinguish them
    user_content = f"""
            ### 1. ORIGINAL SOURCE DOCUMENT
            {original_source}

            ### 2. GENERATED FUNCTIONAL REQUIREMENTS
            {functional_reqs}

            ### 3. GENERATED NON-FUNCTIONAL REQUIREMENTS
            {non_functional_reqs}

            Please evaluate the generated requirements against the original source document.
            """

    messages = [
        {
            "role": "system", 
            "content": prompt
        },
        {
            "role": "user", 
            "content": user_content
        }
    ]
    
    client = _resolve_client(state)
    response = client.responses.parse(model=state['evaluator_model'], input= cast(str,messages),text_format=EvaluationReport)
    new_message = [{"role":"assistant","content":response.output_text}]
    print(_write_json_file(state['feedback_path'],json.loads(response.output_text)))
    evaluation_count = state["evaluation_count"] + 1

    return {
        "messages" : new_message,
        "feedback":True,
        "evaluation_count": evaluation_count,
    }

def human_approval(state: GraphState):
    # Pause and ask for approval
    decision = interrupt({
        "question": f"Do you approve the following feedback in file {state['feedback_path']}?"
    })
    
    return {"run_evaluation":decision}

def route_after_human(state: GraphState) -> str:
    # Approve => finish, Reject => regenerate and re-evaluate.
    if state.get("run_evaluation") is False:
        print("\n Ending workflow.")
        return "evaluation_chart"

    print("\n Routing to evaluating requirements...")
    return "evaluate_requirements"

def process_interrupt(response: str) -> bool:
    clean_response = response.strip().lower()
    if clean_response in ("true", "yes", "y", "approve", "1"):
        return True
    # Check for common "false" variations
    if clean_response in ("false", "no", "n", "reject", "0"):
        return False
    # Optional: Fallback default if they type something unexpected
    print(f"⚠️ Unrecognized input '{response}'. Defaulting to False.")
    return False

def evaluation_chart(state:GraphState):
    with open(state['feedback_path'],'r') as file:
        data = json.load(file)
    
    # Force data into a list if it's just a single object item
    evaluations = data if isinstance(data, list) else [data]
        
    total = len(evaluations)
    passed_count = sum(1 for item in evaluations if item.get('passed') is True)
    failed_count = total - passed_count
    
    print("\n=== EVALUATION RUN TOTALS ===")
    print(f"Total Requirements Processed: {total}")
    print(f"Passed                      : {passed_count}")
    print(f"Failed                      : {failed_count}")
    print("=============================")

