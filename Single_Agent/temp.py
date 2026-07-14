from Global_Client_Layer.PineconeClient import PineconeClient
from Global_Client_Layer.AzureClient import ChatClient 
import csv
import os
from typing import Optional


def upsert_functional_requirements_csv(csv_path: str,
									   index_name: Optional[str] = None,
									   namespace: Optional[str] = None,
									   embedding_model: str = "text-embedding-3-small") -> None:
	"""Read the functional requirements CSV and upsert each row to Pinecone.

	Each row will be embedded using OpenAI and upserted as a vector with
	metadata containing the original fields.

	Args:
		csv_path: Path to the functional requirements CSV file.
		index_name: Optional Pinecone index name (falls back to client default).
		namespace: Optional Pinecone namespace to upsert into.
		embedding_model: OpenAI embedding model to use.
	"""
	# create clients
	pc = PineconeClient(index_name) if index_name else PineconeClient()
	oa = ChatClient()

	vectors = []
	with open(csv_path, newline='', encoding='utf-8') as f:
		reader = csv.DictReader(f)
		for row in reader:
			req_id = row.get('No.') or row.get('No') or row.get('No.,Functional Requirements') or row.get('No.,Functional Requirements')
			# Some CSVs may have the requirement text under different headers; try common names
			text = row.get('Functional Requirements') or row.get('Requirement') or list(row.values())[-1]
			if not text:
				continue

			# get embedding from OpenAI
			emb_resp = oa.create_embedding(text=text)
			embedding = emb_resp.data[0].embedding

			meta = {k: v for k, v in row.items()}
			vector_obj = {"id": str(req_id) or os.urandom(6).hex(), "values": embedding, "metadata": meta}
			vectors.append(vector_obj)

			# batch upsert in chunks of 50
			if len(vectors) >= 50:
				pc.client.upsert(vectors=vectors, namespace=namespace) if namespace else pc.client.upsert(vectors=vectors)
				vectors = []

	if vectors:
		pc.client.upsert(vectors=vectors, namespace=namespace) if namespace else pc.client.upsert(vectors=vectors)


if __name__ == '__main__':
	# example usage; adjust path as needed
	csv_path = os.path.join(os.path.dirname(__file__), '..', 'Data', 'non_functional_requirements.csv')
	csv_path = os.path.normpath(csv_path)
	upsert_functional_requirements_csv(csv_path,namespace="requirements")

