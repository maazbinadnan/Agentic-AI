from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

## Definining and Resolving Client
class ChatClient:
    def __init__(self) -> None:
        self.client = None 
        pass
    
    def resolveAPIClient(self):
        self.client = OpenAI(
            base_url= os.environ['AZURE_OPENAI_ENDPOINT'],
            api_key= os.environ['AZURE_OPENAI_API_KEY']
        )
    
    def call(self,format, messages: list[dict], model="gpt-4o-mini"):
        """Call the LLM with a list of messages."""
        if self.client is None:
            self.resolveAPIClient()

        # Assert to Pylance that self.client is definitely not None at this point
        assert self.client is not None
        response = self.client.responses.parse(
            model=model,
            input=messages # type: ignore
            ,text_format= format
        )
        return response.output_parsed



