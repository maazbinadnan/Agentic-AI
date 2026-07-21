import os
import json
from pathlib import Path


def _read_file(filepath:str):
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
            
        with open(filepath, "w", encoding="utf-8") as file:
            content =  json.dumps(content, indent=4, ensure_ascii=False)
            file.write(content)
        return f"wrote file {filepath} successfully"
    except FileNotFoundError:
        return f"Error: The directory for '{filepath}' was not found."
    except PermissionError:
        return f"Error: Permission denied when trying to write to '{filepath}'."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
def _draw_graph(graph,output_path = Path(__file__).resolve().parent/"graph.png"):
    image_bytes = graph.get_graph(xray=True).draw_mermaid_png() 
    # Save the binary data to a file
    with open(output_path, "wb") as f:
        f.write(image_bytes)       
    print(f"Graph successfully saved to {output_path}")