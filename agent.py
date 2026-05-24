import os
from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()


config = ""
with open('config.json', 'r') as file:
    config = json.load(file)
endpoint = config["AzureAI"]["ResponseEndpoint"]
deployment = config["AzureAI"]["deployment"]

print(endpoint)

api_key = os.getenv("api_key") 
# 3. Use the specialized AzureOpenAI client wrapper
client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

# 4. Make your call (Note: the model argument targets your deployment name)
response = client.responses.create(
    model=deployment,
    input="What is the capital of France?",
)

print(response.output[0])
