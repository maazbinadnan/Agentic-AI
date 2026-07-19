from self_refinement.states.state import GraphState,output_format,EvaluationReport, regenerated_format
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

    requirements = _read_file(state['requirements_filepath'])
    system_prompt = _read_file(prompt_file)

    print("generating user requirements")
    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": requirements},
        ]
    
    response = client.responses.parse(model=state["generation_model"], input= cast(str,messages),text_format=output_format)
    reqs = json.loads(response.output_text)
    new_message = [{"role":"assistant","content":response.output_text}]

    #write all the files
    print(_write_json_file(state['think_file'],reqs['thinking']))
    print(_write_json_file(state['output_functional_path'],reqs['functional_reqs']))
    print(_write_json_file(state['output_non_functional_path'],reqs['non_functional_reqs']))
    return {"messages":messages + new_message} 

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

    response = client.responses.parse(model=state["generation_model"], input= cast(str,messages),text_format=regenerated_format)
    reqs = json.loads(response.output_text)
    new_message = [{"role":"assistant","content":response.output_text}]

    #rewrite to new files

    func_dir, func_file = os.path.split(state['output_functional_path'])
    non_func_dir, non_func_file = os.path.split(state['output_non_functional_path'])

    # 2. Reconstruct the paths by nesting the evaluation count as a subfolder branch
    new_func_path = os.path.join(func_dir, str(state['evaluation_count']), func_file)
    new_non_path = os.path.join(non_func_dir, str(state['evaluation_count']), non_func_file)

    # 3. Ensure the new nested folders (e.g., '\1\') physically exist on disk
    os.makedirs(os.path.dirname(new_func_path), exist_ok=True)
    os.makedirs(os.path.dirname(new_non_path), exist_ok=True)

    # 4. Save your requirements data payloads to the new paths
    print(_write_json_file(new_func_path, reqs['functional_reqs']))
    print(_write_json_file(new_non_path, reqs['non_functional_reqs']))

    return {"messages": new_message}



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
    
    response = client.responses.parse(model=state['evaluator_model'], input= cast(str,messages),text_format=EvaluationReport)
    new_message = [{"role":"assistant","content":response.output_text}]
    print(_write_json_file(state['feedback_path'],json.loads(response.output_text)))
    evaluation_count = state["evaluation_count"] + 1

    return {
        "messages" : new_message,
        "feedback":True,
        "evaluation_count": evaluation_count,
    }
