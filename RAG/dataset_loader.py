from pathlib import Path
import tiktoken
from configurations import Config

config = Config()
_encoding_cache = {}

def _readrepo_and_save(folder_path, batch_size=10):
    path = Path(folder_path)
    items = list(path.rglob("*.md"))
    all_vectors = []
    
    for i in items:
        print(f"Processing {i.name}")
        vectors = chunk_and_save(file=i, model='gpt-4o-mini')
        all_vectors.extend(vectors)
        
        if len(all_vectors) >= batch_size:
            config.index.upsert(vectors=all_vectors[:batch_size])
            all_vectors = all_vectors[batch_size:]
    
    if all_vectors:
        config.index.upsert(vectors=all_vectors)
        print(f"Final batch: {len(all_vectors)} vectors")
    

def _build_vectors(chunks, file_name=None):
    if not isinstance(chunks, (list, tuple)):
        chunks = [chunks]
    
    resp = config.create_embedding(text=chunks)
    
    return [
        {
            "id": f"{file_name or 'doc'}-{idx}",
            "values": data_object.embedding,
            "metadata": {
                "source_file": file_name,
                "chunk_index": idx,
                "text": chunks[idx]
            }
        }
        for idx, data_object in enumerate(resp.data)
    ]

def chunk_and_save(file: Path, model, max_tokens=1024, overlap_percentage=0.20):
    if model not in _encoding_cache:
        _encoding_cache[model] = tiktoken.encoding_for_model(model)
    encoding = _encoding_cache[model]
    
    text = file.read_text(encoding="utf-8")
    all_tokens = encoding.encode(text)
    total_tokens = len(all_tokens)
    print(f"{file.name}: {total_tokens} tokens")
    
    overlap_tokens = int(overlap_percentage * max_tokens)
    step = max_tokens - overlap_tokens
    
    chunks = [
        encoding.decode(all_tokens[i:i + max_tokens])
        for i in range(0, total_tokens, step)
    ]
    
    return _build_vectors(chunks, file_name=file.name)
        


folder_path = "C:\\Users\\OMNI BOOK\\OneDrive\\Documents\\Second-Brain"
_readrepo_and_save(folder_path)

