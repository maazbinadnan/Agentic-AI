import os
import json


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
        return f"wrote file {filepath} successfully"
    except FileNotFoundError:
        return f"Error: The directory for '{filepath}' was not found."
    except PermissionError:
        return f"Error: Permission denied when trying to write to '{filepath}'."
    except Exception as e:
        return f"An unexpected error occurred: {e}"