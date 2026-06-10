from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from openai import OpenAI
from pydantic import SecretStr
from pinecone import Pinecone

load_dotenv()

def get_pinecone_index(name: str = "obsidian-rag"):
        pc = Pinecone(api_key=os.environ['PINECONE_API_KEY'])
        return pc.Index(name)

class Config:
    def  __init__(self):
        self.index = get_pinecone_index()

    def get_base_model(self):
        return OpenAI(
            base_url=os.environ['AZURE_OPENAI_ENDPOINT'],
            api_key=os.environ['AZURE_OPENAI_API_KEY']
        )

    def create_embedding(self, text, model: str = "text-embedding-3-small"):
        client = OpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            base_url=os.environ["AZURE_OPENAI_ENDPOINT"],
        )
        model_name = os.getenv("EMBEDDING_MODEL_DEPLOYMENT", model)
        return client.embeddings.create(input=text, model=model_name)
