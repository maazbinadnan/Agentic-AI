from global_client_layer.PineconeClient import PineconeClient
from global_client_layer.AzureClient import ChatClient 
import csv
import os
from typing import Optional


def _upsert_requirements_csv(
	csv_path: str,
	text_column: str,
	metadata_text_key: str,
	id_prefix: str,
	default_type: Optional[str] = None,
	index_name: Optional[str] = None,
	namespace: Optional[str] = None,
	embedding_model: str = "text-embedding-3-small",
) -> None:
	"""Internal helper to embed and upsert requirement rows into Pinecone."""
	pc = PineconeClient(index_name) if index_name else PineconeClient()
	oa = ChatClient()

	vectors = []
	with open(csv_path, newline='', encoding='utf-8') as f:
		sample = f.read(2048)
		f.seek(0)
		delimiter = '\t' if '\t' in sample else ','
		reader = csv.DictReader(f, delimiter=delimiter)
		for row in reader:
			req_id = (row.get('No.') or row.get('No') or '').strip()
			text = (row.get(text_column) or row.get('Requirement') or '').strip()
			req_type = (row.get('Type') or default_type or '').strip()
			if not text:
				continue

			emb_resp = oa.create_embedding(text=text, model=embedding_model)
			embedding = emb_resp.data[0].embedding

			base_id = req_id if req_id else os.urandom(6).hex()
			vector_id = f"{id_prefix}{base_id}"
			meta = {
				"id": vector_id,
				metadata_text_key: text,
				"type": req_type,
			}
			vectors.append({"id": vector_id, "values": embedding, "metadata": meta})

			if len(vectors) >= 50:
				pc.client.upsert(vectors=vectors, namespace=namespace) if namespace else pc.client.upsert(vectors=vectors)
				vectors = []

	if vectors:
		pc.client.upsert(vectors=vectors, namespace=namespace) if namespace else pc.client.upsert(vectors=vectors)


def upsert_functional_requirements_csv(
	csv_path: str,
	index_name: Optional[str] = None,
	namespace: Optional[str] = None,
	embedding_model: str = "text-embedding-3-small",
) -> None:
	"""Upsert functional requirements CSV rows into Pinecone."""
	_upsert_requirements_csv(
		csv_path=csv_path,
		text_column="Functional Requirements",
		metadata_text_key="functional_requirement",
		id_prefix="FR-",
		default_type="Functional",
		index_name=index_name,
		namespace=namespace,
		embedding_model=embedding_model,
	)


def upsert_non_functional_requirements_csv(
	csv_path: str,
	index_name: Optional[str] = None,
	namespace: Optional[str] = None,
	embedding_model: str = "text-embedding-3-small",
) -> None:
	"""Upsert non-functional requirements CSV rows into Pinecone."""
	_upsert_requirements_csv(
		csv_path=csv_path,
		text_column="Requirement according to Property-, Environment-, & ProcessMASTER",
		metadata_text_key="non_functional_requirement",
		id_prefix="NFR-",
		default_type=None,
		index_name=index_name,
		namespace=namespace,
		embedding_model=embedding_model,
	)


if __name__ == '__main__':
	# example usage; adjust paths as needed
	base_data_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'Data'))
	functional_csv = os.path.join(base_data_dir, 'functional_requirements.csv')
	non_functional_csv = os.path.join(base_data_dir, 'non_functional_requirements.csv')

	upsert_functional_requirements_csv(functional_csv, namespace="requirements")
	# upsert_non_functional_requirements_csv(non_functional_csv, namespace="requirements")

