from langchain_openai import ChatOpenAI
from langchain_core.language_models import GenericFakeChatModel
from langchain.messages import AIMessage
import sys
from langchain_core.messages import BaseMessage
import os
from dotenv import load_dotenv
load_dotenv()
import warnings
# Suppress Pydantic serialization warnings caused by LangChain's internal include_raw wrapper
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

import httpx
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_llm(
    model: str | None = None,
    temperature: float = 0, 
    test: bool = False,
) -> ChatOpenAI | GenericFakeChatModel:
    """Create a ChatOpenAI instance using the project's OpenAI-compatible endpoint.

    Reads ``AZURE_OPENAI_ENDPOINT`` and ``AZURE_OPENAI_API_KEY`` from the
    environment (same variables used by the existing ``Global_Client_Layer``).
    The model defaults to ``gpt-4.1`` but can be overridden via the
    
    Supports ``model-router`` — Azure AI's automatic model routing that
    selects the optimal model per request based on prompt complexity.

    Also takes a test input that returns a Fake Generic Chat Model for testing
    """
    model = model or os.getenv("MODEL", "gpt-4.1")
    print(f"[GLOBAL] LLM initialized with model {model}")
    if test:
        return GenericFakeChatModel(
            messages=iter([AIMessage(content="hello this is a fake chat streaming model")]),
        )
    else: 
        return ChatOpenAI(
        base_url=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_key=os.environ["AZURE_OPENAI_API_KEY"], #type: ignore
        model=model, 
        temperature=temperature,
        stream_usage= True,
        streaming= True
    )



def stream_llm(messages: list[BaseMessage], llm, agent_label: str = "AGENT") -> str:
    """Streams an LLM call to the console token-by-token and returns the full text."""

    print(f"\n--- {agent_label} ---\n", flush=True)

    full_response = []

    for chunk in llm.stream(messages):
        if content := getattr(chunk, "content", None):
            text = content if isinstance(content, str) else str(content)
            sys.stdout.write(text)
            sys.stdout.flush()
            full_response.append(text)

    print("\n\n---------------------\n", flush=True)

    return "".join(full_response)





