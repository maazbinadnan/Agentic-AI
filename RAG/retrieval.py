from configurations import Config
from pinecone import QueryResponse
from pathlib import Path

class Retrieval:
    def __init__(self,config:Config) -> None:
        self.config = config

    def retrieve(self, query,top_k=3):
        embedding = self.config.create_embedding(text=query)
        raw_vector = embedding.data[0].embedding
        results = self.config.index.query(
        # namespace="_default_",
        vector=raw_vector,          # Pass the raw vector list here
        top_k=top_k,
        include_metadata=True,        # Ensures your "source_file" and "text" fields come back
        )
        return results 

    def build_context_string(self, response:QueryResponse):
        matches = response.matches if hasattr(response, 'matches') else response.get('matches', [])
        context_chunks = []

        for match in matches:
            metadata = match.metadata if hasattr(match, 'metadata') else match.get('metadata', {})
            filename = metadata.get('source_file', 'Unknown File')
            text = metadata.get('text', '')

            # Format beautifully for the LLM to read
            chunk_str = f"--- START OF FILE: {filename} ---\n{text.strip()}\n--- END OF FILE ---"
            context_chunks.append(chunk_str)

        return "\n\n".join(context_chunks)

    def generate_response(self, query, context):
        client = self.config.get_base_model()
        
        # Retrieve prompt from system_prompt.md
        prompt_path = Path(__file__).parent / "system_prompt.md"
        system_instruction = prompt_path.read_text(encoding="utf-8").replace("{{context}}", context)
        
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": query}
            ],
            stream= True
        )
        return response




