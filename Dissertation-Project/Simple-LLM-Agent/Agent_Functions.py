import os
import re

def read_md_file(filepath):
    """Takes a filepath to an MD file and reads all its contents."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file at '{filepath}' was not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def write_to_file(filepath, content):
    """Writes content to a file, creating directories if they don't exist."""
    try:
        # Create directories if they don't exist
        directory = os.path.dirname(filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)
            
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
        return f"Successfully wrote to {filepath}"
    except Exception as e:
        return f"Error writing to {filepath}: {e}"

def create_files_from_llm_output(llm_output):
    """
    Parses LLM output for file blocks and creates files.
    Expected format in LLM output:
    [FILE: filename.txt]
    content here
    [END_FILE]
    """
    # Pattern to match [FILE: path] ... [END_FILE]
    pattern = r"\[FILE:\s*(.*?)\]\n?(.*?)\n?\[END_FILE\]"
    matches = re.findall(pattern, llm_output, re.DOTALL)
    
    if not matches:
        return "No file markers ([FILE: ...] and [END_FILE]) found in the output."
    
    results = []
    for filepath, content in matches:
        filepath = filepath.strip()
        # Clean up code blocks if the LLM wrapped content in ``` 
        clean_content = re.sub(r"^```[a-zA-Z]*\n", "", content)
        clean_content = re.sub(r"\n```$", "", clean_content)
        
        result = write_to_file(filepath, clean_content)
        results.append(result)
    
    return "\n".join(results)

