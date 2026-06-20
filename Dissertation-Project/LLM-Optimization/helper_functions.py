"""Module: helper_functions

Utilities for evaluating user stories and interacting with the
Pinecone vector store. Only module-level documentation was added;
no functional changes were made.
"""

from Database_Layer.pinecone_connect import PineconeClient
from pathlib import Path
from typing import Literal
import pandas as pd
import os

def evaluate_user_stories(filepath: Path, type: Literal["Functional Requirements", "Non-Functional Requirements"], score_threshold:float):
    """Evaluate user stories by finding nearest requirements in Pinecone.

    The function reads a CSV at `filepath`, creates embeddings for each
    row, queries the index and writes an evaluation CSV to `Evaluation/`.
    """
    df = pd.read_csv(filepath)
    pc = PineconeClient()
    results = []

    # loop through each, embed it and find closest match
    for text in df["Functional Requirements"]:
        embedding_data = pc.create_embedding(text=text)
        vector = embedding_data.data[0].embedding

        data = pc.index.query(
            namespace="requirements",
            vector=vector,
            filter={"requirement_type": {"$eq": type}},
            top_k=1,
            include_metadata=True,
        )

        matches = data.get("matches", [])
        matched_text = ""
        score = 0

        if matches:
            top_match = matches[0]
            metadata = top_match.get("metadata", {})
            matched_text = metadata.get("requirement_text")
            score = top_match.get("score")

        results.append(
            {
                "Ground Truth": text,
                "Matched Requirement": matched_text,
                "Similarity Score": score > score_threshold,
            }
        )

    results_df = pd.DataFrame(results)
    results_df.to_csv(rf"Dissertation-Project\LLM-Optimization\Evaluation\\{type} evaluation.csv")

path = Path(r"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\LLM-Optimization\Data\functional_requirements.csv")

evaluate_user_stories(filepath=path, type="Functional Requirements",score_threshold=0.85)
