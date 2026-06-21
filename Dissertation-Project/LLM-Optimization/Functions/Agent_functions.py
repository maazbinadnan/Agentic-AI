"""Module: Agent_functions

Contains helper functions used by the LLM-Optimization project. Only
documentation was added in this pass; no code logic was modified.
"""
import os
from Client_Layer.PineconeClient import PineconeClient
from Client_Layer.AzureClient import ChatClient
from States.State import output_format, GraphState,evaluator_output
from typing import cast
import pickle
import json


class Agent_functions():
    def __init__(self, pinecone_client: PineconeClient, azure_client : ChatClient) -> None:
        self._pcindex = pinecone_client.client
        self._azureclient = azure_client.client
    

    def _read_md_file(self,filepath: str) -> str:
        """Read and return the contents of a Markdown file.

        Returns a string with an error message on failure.
        """
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: The file at '{filepath}' was not found."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def generate_user_stories(self,state: GraphState):
        """Generate user stories given the project prompts and data files."""
        print("generating user stories")

        datafile = os.path.normpath(os.path.join("Data", "Requirements.md"))
        promptfile = os.path.normpath(os.path.join("prompt", "system_prompt.md"))

        system_prompt = self._read_md_file(promptfile)
        requirements = self._read_md_file(datafile)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": requirements},
        ]

        response = self._azureclient.responses.parse(model=state["model"], input= cast(str,messages),text_format=output_format)
        if response is None:
            return None
        
        return {"requirements": response.output_parsed}

    def _generate_user_message(self, state: GraphState):
        requirements = state.get("requirements")
        assert requirements is not None

        # 1. Build the Functional Requirements Table
        functional_rows = []
        # If your state is a raw dict from the JSON payload, use .get()
        # If it's a Pydantic object, change to: requirements.functional_reqs
        functional_reqs = requirements.get("functional_reqs", []) if isinstance(requirements, dict) else requirements.functional_reqs
        
        for req in functional_reqs:
            # Safely handle both object attribute or dict key lookups
            r_no = req.get("requirement_no") if isinstance(req, dict) else req.requirement_no
            r_text = req.get("requirement_text") if isinstance(req, dict) else req.requirement_text
            r_ref = req.get("requirement_reference") if isinstance(req, dict) else req.requirement_reference
            
            functional_rows.append(f"| {r_no} | {r_text} | *\"{r_ref}\"* |")

        functional_table = (
            "| Requirement ID | Requirement Text | Source Reference |\n"
            "| :--- | :--- | :--- |\n" + "\n".join(functional_rows)
        )

        # 2. Build the Non-Functional Requirements Table
        nfr_rows = []
        non_functional_reqs = requirements.get("non_functional_reqs", []) if isinstance(requirements, dict) else requirements.non_functional_reqs
        
        for req in non_functional_reqs:
            r_no = req.get("requirement_no") if isinstance(req, dict) else req.requirement_no
            r_text = req.get("requirement_text") if isinstance(req, dict) else req.requirement_text
            r_ref = req.get("requirement_reference") if isinstance(req, dict) else req.requirement_reference
            
            nfr_rows.append(f"| {r_no} | {r_text} | *\"{r_ref}\"* |")

        nfr_table = (
            "| Requirement ID | Requirement Text | Source Reference |\n"
            "| :--- | :--- | :--- |\n" + "\n".join(nfr_rows)
        )

        datafile = os.path.normpath(os.path.join("Data", "Requirements.md"))
        requirements = self._read_md_file(datafile)
        # 3. Construct the clean prompt block for the Evaluator Agent
        user_message_content = (
            "#### 1. Original Requirements Data"
            f"{requirements}\n\n"
            "### 2. Functional Requirements\n"
            f"{functional_table}\n\n"
            "### 3. Non-Functional Requirements\n"
            f"{nfr_table}"
        )

        # Return the update for your LangGraph state array
        return user_message_content


    def evaluate_user_stories(self,state: GraphState):
        print("evaluating user stories")

        datafile = os.path.normpath(os.path.join("Data", "Requirements.md"))
        promptfile = os.path.normpath(os.path.join("prompt", "evaluator_prompt.md"))

        system_prompt = self._read_md_file(promptfile)
        requirements = self._read_md_file(datafile)

        user_message = self._generate_user_message(state)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ]

        response = self._azureclient.responses.parse(model=state["model"], input= cast(str,messages),text_format = evaluator_output)
        if response is None:
            return None

        return {"evaluation" : response.output_parsed}
    
    def revise_user_stories(self,state:GraphState):
        print("revising user stories")
        promptfile = os.path.normpath(os.path.join("prompt", "revise_prompt.md"))   
        system_prompt = self._read_md_file(promptfile)
        if state['evaluation'] is None:
            return "no evaluation found"
        assert state['evaluation'] is not None
        message = ''
        for table in state['evaluation'].evaluation:
            req_id = table.original_requirement_id
            issue = table.issue_identified
            rewritten = table.rewritten_requirement_text
            
            # Example string compilation:
            message += f"ID: {req_id}\nIssue: {issue}\nFix: {rewritten}\n---\n"
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ]

        response = self._azureclient.responses.parse(model="gpt-4o-mini", input= cast(str,messages),text_format=output_format)
        if response is None:
            return None
        
        return {"requirements": response.output_parsed ,"read_state":True}


    def write_state(self, state: GraphState):
        if state['read_state'] == True:
            state_path = r"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\LLM-Optimization\States\final_state.pkl"
        # Change the file extension to .pkl or .bin to reflect it is a binary file
        else:
            state_path = r"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\LLM-Optimization\States\state_before_evaluation.pkl"
        
        try:
            # Open the file in write-binary mode ("wb")
            with open(state_path, "wb") as f:
                pickle.dump(state, f)
            print(f"State object successfully saved directly to {state_path}")
        except Exception as e:
            print(f"Failed to save state object: {e}")


    def router(self,state:GraphState):
        if state["read_state"] == False:
            return "write_state"
        else:
            return "read_state"


    def write_to_csv(self,state: GraphState) -> None:
        """Write each requirement category to a CSV file under `filepath`."""
        requirements = state.get("requirements")
        assert requirements is not None
        basepath = state.get("filepath", ".")
        model_name = state.get("model", "model")

        for category in requirements:
            filename = f"{model_name}_{category}.csv"
            print(filename)
            # filepath = os.path.normpath(os.path.join(basepath, filename))
            # try:
            #     directory = os.path.dirname(filepath)
            #     if directory and not os.path.exists(directory):
            #         os.makedirs(directory, exist_ok=True)

            #     with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
            #         writer = csv.writer(csvfile)
            #         writer.writerow(["requirement_no", "requirement_text", "requirement_reasoning", "requirement_reference"])
            #         for output_requirements in category.requirements:
            #             writer.writerow([
            #                 output_requirements.requirement_no,
            #                 output_requirements.requirement_text,
            #                 output_requirements.requirement_reasoning,
            #                 output_requirements.requirement_reference,
            #             ])
            #     print(f"Successfully wrote CSV to {filepath}")
            # except Exception as e:
            #     print(f"Error writing CSV to {filepath}: {e}")


    # def upsert_vectors(self,state: GraphState) -> None:
    #     """Create embeddings and upsert requirement vectors into Pinecone."""
    #     namespace = "requirements"
    #     model = state.get("requirements")
    #     assert model is not None
        
    #     # Ensure the namespace/schema exists before upserting
    #     for category in model.final:
    #         req_type = str(category.requirement_type)
    #         for output_requirements in category.requirements:
                
    #             embedding = self._azureclient.embeddings.create(input = output_requirements.requirement_text,model="text-embedding-3-small")
    #             vector_embedding = embedding.data[0].embedding
    #             # Build metadata from the requirement object
    #             md = {
    #                 "requirement_no": output_requirements.requirement_no,
    #                 "requirement_type": req_type,
    #                 "requirement_text": output_requirements.requirement_text,
    #             }

    #             self._pcindex.upsert(
    #                 vectors=[{ "id": output_requirements.requirement_no, "values":vector_embedding,"metadata":md}],
    #                 namespace = namespace 
    #             )


