import os
import json
import pandas as pd
import re
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from global_layer.AzureClient import ChatClient

# Resolve project root and config relative to this file
_EVAL_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_EVAL_DIR)

with open(os.path.join(_EVAL_DIR, "config.json"), "r") as _cfg_f:
    _config = json.load(_cfg_f)

embedding_client = ChatClient()


def _azure_embed_texts(texts: list[str]) -> np.ndarray:
    """Create embeddings through Azure OpenAI and return a 2D numpy array."""
    if not texts:
        return np.array([])

    response = embedding_client.create_embedding(texts)
    # Preserve response order so similarity rows align with the input texts.
    return np.array([item.embedding for item in response.data], dtype=float)


def thresholded_topk_coverage_score(scores: np.ndarray, top_indices: np.ndarray, threshold: float) -> float:
    """Average scores in top-k that meet threshold; return 0.0 if none qualify."""
    selected_scores = [float(scores[i]) for i in top_indices if float(scores[i]) >= threshold]
    if not selected_scores:
        return 0.0
    return round(sum(selected_scores) / len(selected_scores), 4)


def get_ground_truths():
    ground_fnr_path = os.path.join(_PROJECT_ROOT, _config["ground_fnr"])
    ground_nfnr_path = os.path.join(_PROJECT_ROOT, _config["ground_nfnr"])

    with open(ground_fnr_path, "r", encoding="utf-8") as f: 
        ground_fnr = json.load(f)  

    with open(ground_nfnr_path, "r", encoding="utf-8") as f: 
        ground_nfnr = json.load(f)

    requirements_list = []

    # Support dict wrapper with "requirements" key
    if isinstance(ground_fnr, dict) and "requirements" in ground_fnr:
        ground_fnr = ground_fnr["requirements"]

    if isinstance(ground_nfnr, dict) and "requirements" in ground_nfnr:
        ground_nfnr = ground_nfnr["requirements"]

    for req in ground_fnr:
        if isinstance(req, dict):
            text = req.get('Requirement') or req.get('text')
            if text:
                requirements_list.append({"type": "fnr", "requirement": text})

    for req in ground_nfnr:
        if isinstance(req, dict):
            text = req.get('Requirement') or req.get('text')
            if text:
                requirements_list.append({"type": "nfnr", "requirement": text})

    return requirements_list

def get_generated(functional_reqs: str, nfunctional_reqs: str):
    all_generated = []

    # 1. Extract Functional Requirements
    with open(functional_reqs, "r", encoding="utf-8") as funcs:
        generated_funcs = funcs.read()

    req_pattern = re.compile(
        r"-\s*\*\*Requirement:\*\*\s*(.*?)(?=\r?\n-|\r?\n###|\Z)", 
        re.DOTALL
    )    
    
    for text in req_pattern.findall(generated_funcs):
        all_generated.append({
            "gen_type": "gen_fnr",
            "gen_requirement": text.strip()
        })

    # 2. Extract Non-Functional Requirements (appended to the SAME list)
    with open(nfunctional_reqs, "r", encoding="utf-8") as nfuncs:
        generated_nfuncs = nfuncs.read()

    for text in req_pattern.findall(generated_nfuncs):
        all_generated.append({
            "gen_type": "gen_nfnr",
            "gen_requirement": text.strip()
        })

    return all_generated

def requirements_coverage(
    ground_truths: list,
    generated_reqs: list,
    top_k: int = 2,
    threshold: float = 0.0,
    output_json_path: str = "coverage.json",
):
    """Embeds requirements, retrieves top-k matches, and computes coverage from cosine similarity.

    Args:
        ground_truths: List of dicts, e.g., [{'type': 'fnr', 'requirement': '...'}, ...]
        generated_reqs: List of dicts, e.g., [{'gen_type': 'gen_fnr', 'gen_requirement': '...'}, ...]
        top_k: Number of top matches to retrieve per ground truth item (default: 3).
        threshold: Similarity cutoff. Only top-k scores >= threshold are averaged.
        output_json_path: Path to save the output JSON file.

    Returns:
        List of dictionaries containing each ground truth requirement, top-k matches, and coverage score.
    """
    # 1. Extract texts for embedding
    gt_texts = [item["requirement"] for item in ground_truths]
    gen_texts = [item["gen_requirement"] for item in generated_reqs]

    if not gt_texts or not gen_texts:
        return []

    # 2. Vectorize texts using Azure embedding endpoint
    gt_embeddings = _azure_embed_texts(gt_texts)
    gen_embeddings = _azure_embed_texts(gen_texts)

    # 3. Compute cosine similarity matrix (shape: [num_gt, num_gen])
    similarity_matrix = cosine_similarity(gt_embeddings, gen_embeddings)

    results = []

    print("\nEvaluating requirement coverage using Azure embeddings + cosine similarity...")

    # 4. For each ground truth, extract top_k matches and evaluate coverage using Azure OpenAI LLM
    for idx, gt_item in enumerate(ground_truths):
        gt_req = gt_item.get("requirement")
        scores = similarity_matrix[idx]

        # Get indices of top_k highest similarity scores (sorted descending)
        top_indices = np.argsort(scores)[::-1][:top_k]

        matches = []
        candidate_texts = []
        for match_idx in top_indices:
            candidate_req = generated_reqs[match_idx].get("gen_requirement")
            candidate_texts.append(candidate_req)
            matches.append(
                {
                    "gen_type": generated_reqs[match_idx].get("gen_type"),
                    "gen_requirement": candidate_req,
                    "similarity_score": round(float(scores[match_idx]), 4),
                }
            )

        coverage_score = thresholded_topk_coverage_score(scores, top_indices, threshold)

        results.append(
            {
                "ground_truth_type": gt_item.get("type"),
                "ground_truth_requirement": gt_req,
                "top_matches": matches,
                "coverage_score": coverage_score
            }
        )

    # 5. Save final results JSON outside the loop
    if output_json_path:
        output_dir = os.path.dirname(output_json_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        with open(output_json_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"Successfully saved coverage analysis to: {output_json_path}")

    return results