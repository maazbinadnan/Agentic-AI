from ChatClient import ChatClient
from state import BusinessAnalystAgentState


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
            "content": "please generate the user story"
        }]
    
    response = llm_client.call(messages=messages)
    print(response)

