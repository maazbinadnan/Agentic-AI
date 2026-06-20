"""Module: ChatClient

Small wrapper around the OpenAI client used by the project. Only
module-level documentation was added in this formatting pass; no
behavioral changes were made.
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class ChatClient:
    """Client wrapper for OpenAI responses API.

    This class lazily resolves the underlying `OpenAI` client from
    environment variables and exposes a `call` method used by the
    rest of the project.
    """
    def __init__(self):
        self._client = OpenAI(
            base_url=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
        )
    @property    
    def client(self):
        return self._client

    def create_embedding(self, text, model: str = "text-embedding-3-small"):
        model_name = os.getenv("EMBEDDING_MODEL_DEPLOYMENT", model)
        return self.client.embeddings.create(input=text, model=model_name)



