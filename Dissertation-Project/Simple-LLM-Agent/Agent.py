from ChatClient import ChatClient
from pathlib import Path
from state import BusinessAnalystAgentState
from state import LLM_response


# resolve the client that returns the properties
llm_client = ChatClient()
llm_client.resolveAPIClient()


def parse_input(state:BusinessAnalystAgentState):
    "Extract and parse input"
    print(f"parsing file {state['filename']}")


def create_user_stories(state:BusinessAnalystAgentState):
    "takes the file details and parses it to create user stories"
    
    SystemPrompt =f"""Given the user research I want you to create user stories using the if-then-when acceptance criteria
    
    User-Research = {state['user_research']}
    
    """

    messages=[{
            "role": "system",
            "content": SystemPrompt
        },
        {
            "role": "user",
            "content": "please generate the user story along with a title"
        }
        ]
    
    response = llm_client.call(messages=messages,format = LLM_response)
    
    if not response:
        return {}

    return {
        "user_story": [{"title": response.story_title, "content": response.story_content, "written": False}]
    }


def write_user_stories(state: BusinessAnalystAgentState):
    for story in state['user_story']:
        if not story['written']:
            # Create a safe filename from the title
            filename = f"{story['title'].replace(' ', '_')}.md"
            with open(filename, "w") as f:
                f.write(f"# {story['title']}\n\n")
                f.write(story['content'])
            print(f"File {filename} created.")
            
            # Note: In a real LangGraph setup, you would return updated written status 
            # but updating specific items in a list reducer requires a strategy 
            # (like an ID) or a full state overwrite here.
    
    return {"written": True}
            
