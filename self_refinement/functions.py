from self_refinement.states.state import GraphState,output_format
from global_client_layer.AzureClient import ChatClient
from global_functions.functions import _read_file,_write_json_file
from typing import cast
from langgraph.types import interrupt
import os
import json
client = ChatClient().client

prompt_file = r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\prompts\initial_system_prompt.md'
refinement_prompt = r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\prompts\refinement_prompt.md'
evaluator_prompt = r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\self_refinement\prompts\evaluation_prompt.md'

def generate_requirements(state:GraphState):
    '''read the md file and output user stories'''
    if state["feedback"]:
        print("changing output files")
        system_prompt = _read_file(refinement_prompt)
        print(f"calling LLM with system prompt {refinement_prompt}")
        functional_reqs = _read_file(state['output_functional_path'])
        non_functional_reqs = _read_file(state['output_non_functional_path'])
        original_source = _read_file(state['requirements_filepath'])

        user_content = f"""
            ### 1. ORIGINAL SOURCE DOCUMENT
            {original_source}

            ### 2. GENERATED FUNCTIONAL REQUIREMENTS
            {functional_reqs}

            ### 3. GENERATED NON-FUNCTIONAL REQUIREMENTS
            {non_functional_reqs}

            Please evaluate the generated requirements against the original source document.
            """

        last_message = state["messages"][-1] if state["messages"] else None
        if isinstance(last_message, dict):
            previous_generation = str(last_message.get("content", "No previous generation found."))
        elif last_message is not None:
            previous_generation = str(getattr(last_message, "content", "No previous generation found."))
        else:
            previous_generation = "No previous generation found."
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
            {"role" :"assistant","content": previous_generation}
        ]
    else:
        system_prompt = _read_file(prompt_file)
        requirements = _read_file(state['requirements_filepath'])
        print(f"calling LLM with system prompt {prompt_file}")
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": requirements},
        ]
    
    response = client.responses.parse(model=state["generation_model"], input= cast(str,messages),text_format=output_format)
    reqs = json.loads(response.output_text)
    new_message = [{"role":"assistant","content":response.output_text}]
    print(_write_json_file(state['think_file'],reqs['thinking']))
    print(_write_json_file(state['output_functional_path'],reqs['functional_reqs']))
    print(_write_json_file(state['output_non_functional_path'],reqs['non_functional_reqs']))

    if state['feedback']:
        approved = interrupt(f"Stop after {state['evaluation_count']} evaluation? (true/false)")
        if isinstance(approved, bool):
            stop_requested = approved
        elif isinstance(approved, str):
            stop_requested = approved.strip().lower() in {"true", "t", "yes", "y", "1"}
        else:
            stop_requested = bool(approved)
    else:
        stop_requested = False
    return {"messages":messages + new_message,"stop_requested":stop_requested}


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

    # Correct message array structure (separate dicts!)
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
    
    response = client.responses.create(model=state['evaluator_model'], input= cast(str,messages))
    new_message = [{"role":"assistant","content":response.output_text}]
    print(_write_json_file(state['feedback_path'],response.output_text))
    evaluation_count = state["evaluation_count"] + 1

    return {
        "messages" : new_message,
        "feedback":True,
        "evaluation_count": evaluation_count,
    }
