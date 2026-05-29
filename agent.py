import os
from dotenv import load_dotenv
from openai import OpenAI
import json
from openai import OpenAI
load_dotenv()

'''config setup'''
config = ""
with open('config.json', 'r') as file:
    config = json.load(file)
endpoint = config["AzureAI"]["ResponseEndpoint"]
deployment = config["AzureAI"]["deployment"]

'''setup api key'''
api_key = os.getenv("AZURE_OPENAI_API_KEY") 


'''Agent setup'''
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

client = OpenAI(
    base_url=endpoint,
    api_key= api_key
)


completion = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": "can you explain how langgraph works in simple short terms",
        }
    ],
)

print(completion.choices[0].message)