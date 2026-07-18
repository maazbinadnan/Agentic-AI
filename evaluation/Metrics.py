
from global_client_layer.AzureClient import ChatClient
from typing import cast
from evaluation.states.state import MetricsReport
from global_functions.functions import _read_file,_write_json_file
import json
import pandas as pd
client = ChatClient().client
system_prompt = r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\evaluation\prompts\metrics_prompt.md"

    
def metrics_user_stories(original_requirements_file:str,generated_requirements:str,evaluation_file:str, model:str):
    print("evaluating user stories")
    
    ground_truth = _read_file(original_requirements_file)
    generated_requirements =  _read_file(generated_requirements)

    user_content = f"""
            ### 1. ORIGINAL SOURCE DOCUMENT
            {ground_truth}

            ### 2. GENERATED REQUIREMENTS
            {generated_requirements}

            Please evaluate the generated requirements against the original source document.
            """
    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]
    
    response = client.responses.parse(model=model, input= cast(str,messages),text_format=MetricsReport)
    _write_json_file(evaluation_file,json.loads(response.output_text))


##calling
ground_truth_file =r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Data\functional_requirements.json"
generated_file = r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\single_agent\7-18-2026\output_gpt_4.1_functional.json"
metrics_file = r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\evaluation\single_agent\7-18-2026\gpt-4.1\metrics_functional.json"
metrics_user_stories(ground_truth_file,generated_file,metrics_file,"gpt-5.4")

ground_truth_file =r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Data\non_functional_requirements.json"
generated_file = r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\single_agent\7-18-2026\output_gpt_4.1_non_functional.json"
metrics_file = r"C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\evaluation\single_agent\7-18-2026\gpt-4.1\metrics_non_functional.json"
metrics_user_stories(ground_truth_file,generated_file,metrics_file,"gpt-5.4")