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

    def __init__(self) -> None:
        self.client = None

    def resolveAPIClient(self) -> None:
        self.client = OpenAI(
            base_url=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
        )

    def call(self, format, messages: list[dict], model: str = "gpt-4.1"):
        """Call the LLM with a list of messages.

        Parameters:
            format: expected output format (project-specific)
            messages: list of message dicts for the chat API
            model: model/deployment name
        """
        if self.client is None:
            self.resolveAPIClient()

        assert self.client is not None
        response = self.client.responses.parse(
            model=model,
            input=messages,  # type: ignore
            text_format=format,
        )

        return response.output_parsed



