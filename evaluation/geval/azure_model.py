import os
from typing import Any, Optional, Type
from pydantic import BaseModel
from deepeval.models.base_model import DeepEvalBaseLLM
from global_layer.AzureClient import ChatClient


class AzureOpenAIDeepEval(DeepEvalBaseLLM):
    """Custom DeepEval LLM wrapper connecting GEval metrics to Azure OpenAI ChatClient."""

    def __init__(self, model_name: Optional[str] = None):
        self.model_name = model_name or os.getenv("EVAL_MODEL", "gpt-4.1")
        self._client = None

    def load_model(self):
        if self._client is None:
            self._client = ChatClient().client
        return self._client

    def generate(self, prompt: str, schema: Optional[Type[BaseModel]] = None) -> Any:
        client = self.load_model()
        if schema is not None:
            response = client.responses.parse(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                text_format=schema,
            )
            return response.output_parsed
        else:
            response = client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
            )
            res_text = response.choices[0].message.content
            return res_text

    async def a_generate(self, prompt: str, schema: Optional[Type[BaseModel]] = None) -> Any:
        return self.generate(prompt, schema=schema)

    def get_model_name(self) -> str:
        return self.model_name
