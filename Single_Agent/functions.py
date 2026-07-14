from Single_Agent.States.state import GraphState,output_format
from Global_Client_Layer.AzureClient import ChatClient
from typing import cast
import os
import json
client = ChatClient().client

prompt_file = r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Single-Agent\description.md'
output_file = r'C:\Users\OMNI BOOK\OneDrive - Lancaster University\MSc Dissertation\MSc Project\Single-Agent\output.md'
def _read_md_file(filepath:str):
    """Read and return the contents of a Markdown file.
    Returns a string with an error message on failure.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file at '{filepath}' was not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
def _write_json_file(filepath: str, content: str):
    """Writes the provided content string to a Markdown file.
    
    Returns a success message on completion, or an error message on failure.
    """
    try:
        target_dir = os.path.dirname(filepath)
        
        # Create the directory structure if it doesn't exist (does nothing if it exists)
        if target_dir:
            os.makedirs(target_dir, exist_ok=True)
            
        with open(filepath, "x", encoding="utf-8") as file:
            content =  json.dumps(content, indent=4, ensure_ascii=False)
            file.write(content)
    except FileNotFoundError:
        return f"Error: The directory for '{filepath}' was not found."
    except PermissionError:
        return f"Error: Permission denied when trying to write to '{filepath}'."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def generate_requirements(state:GraphState):
    '''read the md file and output user stories'''
    requirements = _read_md_file(state['filepath'])
    system_prompt = _read_md_file(prompt_file)

    print("calling LLM")
    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": requirements},
        ]

    response = client.responses.parse(model=state["model"], input= cast(str,messages),text_format=output_format)
    reqs = json.loads(response.output_text)
    print(_write_json_file(state['output_functional_path'],reqs['functional_reqs']))
    print(_write_json_file(state['output_non_functional_path'],reqs['non_functional_reqs']))
    


# def generate_user_stories(state:GraphState):
#     '''read the md file and output user stories'''
#     requirements = _read_md_file(state['filepath'])
#     system_prompt = _read_md_file(prompt_file)

#     messages = [
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": requirements},
#         ]

#     response = client.responses.create(model=state["model"], input= cast(str,messages))
#     print(_write_md_file(state['output_path'],response.output_text))
#     return {"response": response.output_text}
