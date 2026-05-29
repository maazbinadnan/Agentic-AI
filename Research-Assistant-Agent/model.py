from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
load_dotenv()

#defining the model
base_model = ChatOpenAI(
    model="gpt-4o-mini", 
    base_url=os.environ['AZURE_OPENAI_ENDPOINT'],
    api_key= SecretStr(os.environ['AZURE_OPENAI_API_KEY']),  
    temperature=0
)

