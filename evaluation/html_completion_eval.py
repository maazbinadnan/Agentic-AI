import re
from global_layer.functions import _read_file, _write_json_file
from pathlib import Path
folder = Path(r"single_agent\outputs\smart_home_gpt_5.4")
EVAL_FILE =r"evaluation\evals\pure_single_gpt_5.4\pure_single_gpt_5.4_mockup_coverage.json"

def load_html_mapping(markdown_file):
    mapping = {}

    content = _read_file(markdown_file)

    # Match each table row
    rows = re.findall(
        r"\|\s*`([^`]+)`\s*\|\s*([^|]+)\s*\|",
        content
    )

    for html_file, stories in rows:
        # Extract US-001, US-002, etc.
        user_stories = re.findall(r"US-\d+", stories)

        mapping[html_file] = user_stories

    print(mapping)
    return mapping

def extract_user_story(file = str(next(folder.glob("04*"), None))):
    markdown_text = _read_file(file)
    pattern = r"###\s*(US-\d+)\s*\n\*\*User Story:\*\*\s*(.+)"
    matches = re.findall(pattern, markdown_text)
    print(matches)
    #get the html mapping from html mapping file 
    file = next(folder.glob("07*"), None)
    html_mapping = load_html_mapping(file)
    output = []
    count =0
    for story_id,story_text in matches: 
        for html_file, mapped_stories in html_mapping.items():
            if story_id in mapped_stories:
                output.append(
                        {
                            "story_id": story_id,
                            "story_text": story_text.strip(),
                            "html_file": html_file,
                            "coverage": "",
                        }
                    )
    # Remove duplicates while preserving order
    _write_json_file(EVAL_FILE,output)
    return output

print(extract_user_story())
