from global_client_layer.AzureClient import ChatClient
from typing import cast
from evaluation.states.state import EvaluationReport
from global_functions.functions import _read_file,_write_json_file
import json

client = ChatClient().client
system_prompt = r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\evaluation\prompts\evaluation_prompt.md'

def evaluate_user_stories(original_requirements_file:str,functional_requirements:str,non_functional_reqs:str,evaluation_file:str, model:str):
    print("evaluating user stories")
    
    requirements = _read_file(original_requirements_file)
    functional_requirements =  _read_file(functional_requirements)
    non_functional_reqs = _read_file(non_functional_reqs)

    user_content = f"""
            ### 1. ORIGINAL SOURCE DOCUMENT
            {requirements}

            ### 2. GENERATED FUNCTIONAL REQUIREMENTS
            {functional_requirements}

            ### 3. GENERATED NON-FUNCTIONAL REQUIREMENTS
            {non_functional_reqs}

            Please evaluate the generated requirements against the original source document.
            """
    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]
    
    response = client.responses.parse(model=model, input= cast(str,messages),text_format=EvaluationReport)
    _write_json_file(evaluation_file,json.loads(response.output_text))



