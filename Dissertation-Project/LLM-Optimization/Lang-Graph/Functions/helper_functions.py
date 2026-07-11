"""Module: helper_functions

Utilities for evaluating user stories and interacting with the
Pinecone vector store. Only module-level documentation was added;
no functional changes were made.
"""

from ...Client_Layer.PineconeClient import PineconeClient
from ...Client_Layer.AzureClient import ChatClient
from pathlib import Path
from typing import Literal
import pandas as pd
import os

def evaluate_user_stories(pc:PineconeClient,az:ChatClient, filepath: Path, type: Literal["Functional Requirements", "Non-Functional Requirements"], score_threshold:float):
    """Evaluate user stories by finding nearest requirements in Pinecone.

    The function reads a CSV at `filepath`, creates embeddings for each
    row, queries the index and writes an evaluation CSV to `Evaluation/`.
    """
    df = pd.read_csv(filepath)
    results = []

    # loop through each, embed it and find closest match
    for text in df["Functional Requirements"]:
        embedding_data = az.client.embeddings.create(input=text,model="text-embedding-3-small")
        vector = embedding_data.data[0].embedding

        data = pc.client.query(
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
                "Matched Requirement": matched_text if score > score_threshold else None,
                "Similarity Score": score if score > score_threshold else None
            }
        )

    results_df = pd.DataFrame(results)
    results_df.to_csv(rf"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\LLM-Optimization\Data\Evaluation_Data\{type} evaluation_{score_threshold}.csv")

