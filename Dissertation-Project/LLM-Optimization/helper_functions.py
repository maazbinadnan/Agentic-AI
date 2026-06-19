from Database_Layer.pinecone_connect import PineconeClient
from pathlib import Path
from typing import Literal
import pandas as pd
import os

def evaluate_user_stories(filepath:Path,type:Literal['Functional Requirements','non-functional']):
    df = pd.read_csv(filepath)
    pc = PineconeClient()
    results = []
    matched_text = ""
    score = 0
    #loop through each, embed it and find closest match
    for text in df['Functional Requirements']:
        embedding_data = pc.create_embedding(text=text)
        vector = embedding_data.data[0].embedding
        data = pc.index.query(
            namespace= "requirements",
            vector= vector,
            filter = {
                "requirement_type" : {"$eq":type}
            },
            top_k= 1,
            include_metadata= True
        )
        print("ground_truth = ", text)
        matches = data.get("matches", [])
        if matches:
            # Grab the top match directly without a loop
            top_match = matches[0]
            metadata = top_match.get("metadata", {})
            matched_text= metadata.get('requirement_text')
            score =  top_match.get("score")
        results.append({
            "Ground Truth": text,
            "Matched Requirement": matched_text,
            "Similarity Score": score
        })
    results_df = pd.DataFrame(results)
    results_df.to_csv(f"Evaluation\\{type} evaluation.csv")
path = Path("Data\\functional_requirements.csv")

evaluate_user_stories(filepath=path,type='Functional Requirements')
