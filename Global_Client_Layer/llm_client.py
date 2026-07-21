from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()


def get_llm(
    model: str | None = None,
    temperature: float = 0,
) -> ChatOpenAI:
    """Create a ChatOpenAI instance using the project's OpenAI-compatible endpoint.

    Reads ``AZURE_OPENAI_ENDPOINT`` and ``AZURE_OPENAI_API_KEY`` from the
    environment (same variables used by the existing ``Global_Client_Layer``).
    The model defaults to ``gpt-4o-mini`` but can be overridden via the
    ``THREE_AMIGOS_MODEL`` env-var or the *model* parameter.
    """
    model = model or os.getenv("THREE_AMIGOS_MODEL", "gpt-4.1")
    return ChatOpenAI(
        base_url=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_key=os.environ["AZURE_OPENAI_API_KEY"], #type: ignore
        model=model, 
        temperature=temperature,
    )