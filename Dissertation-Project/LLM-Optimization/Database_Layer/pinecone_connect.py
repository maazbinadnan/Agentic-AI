from pinecone import Pinecone
from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()


class PineconeClient:
    """Simple wrapper around the Pinecone client for index/namespace management

    Usage:
        pc = PineconeClient()
        pc.ensure_namespace()
        pc.upsert_record(id, vector, metadata={...})
    """

    DEFAULT_SCHEMA = {
        "fields": {
            "requirement_no": {"filterable": True},
            "requirement_type": {"filterable": True},
            "requirement_text": {"filterable": True},
            "created_at": {"filterable": True}
        }
    }

    def __init__(self, api_key: str | None = None, index_name: str = "obsidian-rag", namespace: str = "requirements"):
        if api_key is None:
            api_key = os.getenv("PINECONE_API_KEY")
        if not api_key:
            raise ValueError("PINECONE_API_KEY is not set in environment and no api_key was provided")

        self._pc = Pinecone(api_key=api_key)
        self.index_name = index_name
        self.index = self._pc.index(self.index_name)
        self.namespace = namespace

    def ensure_namespace(self, schema: dict | None = None):
        """Create the namespace if it doesn't exist. Returns the API response or None.

        If the namespace already exists the underlying SDK may raise; this method
        will return the exception message in that case.
        """
        schema = schema or self.DEFAULT_SCHEMA
        try:
            return self.index.create_namespace(name=self.namespace, schema=schema)
        except Exception as exc:  # keep broad to surface SDK-specific errors
            return exc

    def upsert_record(self, id: str | int, vector: list[float], metadata: dict | None = None, namespace: str | None = None):
        """Upsert a single vector record into the index.

        Parameters:
            id: unique id for the vector (string or int)
            vector: list of floats representing the vector embedding
            metadata: optional dictionary of metadata/fields
            namespace: optional namespace override

        Returns the SDK response for the upsert call.
        """
        ns = namespace or self.namespace
        if not isinstance(vector, (list, tuple)):
            raise ValueError("`vector` must be a list or tuple of floats")

        item = {"id": str(id), "values": list(vector)}
        if metadata:
            item["metadata"] = metadata

        try:
            return self.index.upsert(vectors=[item], namespace=ns)
        except Exception as exc:
            raise
    
    def create_embedding(self, text, model: str = "text-embedding-3-small"):
        client = OpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            base_url=os.environ["AZURE_OPENAI_ENDPOINT"],
        )
        model_name = os.getenv("EMBEDDING_MODEL_DEPLOYMENT", model)
        return client.embeddings.create(input=text, model=model_name)


__all__ = ["PineconeClient"]


