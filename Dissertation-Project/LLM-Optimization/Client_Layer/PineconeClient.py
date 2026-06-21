"""Module: pinecone_connect

Light wrapper for Pinecone operations and OpenAI embedding creation.
This pass only adds documentation and clarifying docstrings; no logic
or behavioral changes were made.
"""
from pinecone import Pinecone
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
import json 
with open(r"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\config.json","r") as jsonfile:
    data = json.load(jsonfile)

class PineconeClient:
    """Simple wrapper around the Pinecone client for index/namespace management

    Usage:
        pc = PineconeClient()
        pc.ensure_namespace()
        pc.upsert_record(id, vector, metadata={...})
    """
    def __init__(self, index_name: str = "obsidian-rag", namespace: str = data["$namespace"]):
        api_key = os.getenv("PINECONE_API_KEY")
        self._pc = Pinecone(api_key=api_key)
        self._index = self._pc.index(index_name)
    @property
    def client(self):
        """Return the raw Pinecone client instance for direct use (upsert/query/etc.)."""
        return self._index



__all__ = ["PineconeClient"]


