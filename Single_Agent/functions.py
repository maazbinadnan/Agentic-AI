from single_agent.states.state import GraphState,output_format
from global_client_layer.AzureClient import ChatClient
from global_functions.functions import _read_file,_write_json_file
from typing import cast
import os
import json
client = ChatClient().client

prompt_file = r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Single_Agent\Prompts\system_prompt.md'


def generate_requirements(state:GraphState):
    '''read the md file and output user stories'''

    requirements = _read_file(state['requirements_filepath'])
    system_prompt = _read_file(prompt_file)

    print("generating user requirements")
    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": requirements},
        ]
    
    response = client.responses.parse(model=state["model"], input= cast(str,messages),text_format=output_format)
    reqs = json.loads(response.output_text)
    new_message = [{"role":"assistant","content":response.output_text}]
    print(_write_json_file(state['think_file'],reqs['thinking']))
    print(_write_json_file(state['output_functional_path'],reqs['functional_reqs']))
    print(_write_json_file(state['output_non_functional_path'],reqs['non_functional_reqs']))
    return {"messages":messages + new_message}    
