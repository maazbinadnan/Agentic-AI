import os
from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()

'''config setup'''
config = ""
with open('config.json', 'r') as file:
    config = json.load(file)
endpoint = config["AzureAI"]["ResponseEndpoint"]
deployment = config["AzureAI"]["deployment"]

'''setup api key'''
api_key = os.getenv("api_key") 

#setting up the client
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
