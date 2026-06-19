import os
import csv
from ChatClient import ChatClient
from State import output_format_final,GraphState


def read_md_file(filepath):
    """Takes a filepath to an MD file and reads all its contents."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file at '{filepath}' was not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    

def write_to_file(state:GraphState):
    """Writes each category to a simple Markdown file, creating directories as needed."""
    model = state.get("requirements")
    assert model is not None
    basepath = state.get('filepath', '.')
    model_name = state.get('model', 'model')

    for category in model.final:
        req_type = str(category.requirement_type)
        filename = f"{model_name}_{req_type}.md"
        filepath = os.path.normpath(os.path.join(basepath, filename))
        try:
            directory = os.path.dirname(filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)

            with open(filepath, "w", encoding="utf-8") as file:
                    for output_requirements in category.requirements:
                        file.write(f"{output_requirements.requirement_no} {output_requirements.requirement_text}, reasoning = {output_requirements.requirement_reasoning}, reference = {output_requirements.requirement_reference}  \n")
            print(f"Successfully wrote to {filepath}")
        except Exception as e:
            print(f"Error writing to {filepath}: {e}")
    
def write_to_csv(state:GraphState):
    """Writes each category to a CSV file, creating directories as needed."""
    model = state.get("requirements")
    assert model is not None
    basepath = state.get('filepath', '.')
    model_name = state.get('model', 'model')

    for category in model.final:
        req_type = str(category.requirement_type)
        filename = f"{model_name}_{req_type}.csv"
        filepath = os.path.normpath(os.path.join(basepath, filename))
        try:
            directory = os.path.dirname(filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)

            with open(filepath, "w", newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["requirement_no", "requirement_text", "requirement_reasoning", "requirement_reference"])
                for output_requirements in category.requirements:
                    writer.writerow([
                        output_requirements.requirement_no,
                        output_requirements.requirement_text,
                        output_requirements.requirement_reasoning,
                        output_requirements.requirement_reference,
                    ])
            print(f"Successfully wrote CSV to {filepath}")
        except Exception as e:
            print(f"Error writing CSV to {filepath}: {e}")
    
def generate_user_stories(state:GraphState):
    '''generate user stories given a prompt'''
    print("generating user stories")
    #reolve chat client
    client = ChatClient()
    client.resolveAPIClient()

    datafile = os.path.normpath(os.path.join("Data", "Requirements.md"))
    promptfile = os.path.normpath(os.path.join("prompt", "system_prompt.md"))

    system_prompt = read_md_file(promptfile)
    data = read_md_file(datafile)
    messages=[{
               "role": "system",
               "content": system_prompt
           },
           {
               "role": "user",
               "content": data
           }
           ]
    
    response = client.call(model=state["model"], messages=messages,format = output_format_final)
    if response is None:
        return 
    assert response is not None
    return { "requirements": response }

