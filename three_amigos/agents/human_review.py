"""Human Review — interrupt point for final approval.

Pauses the pipeline so the human can approve the output or request
further revisions.
"""

from three_amigos.States.state import ThreeAmigosState
from langchain_core.messages import HumanMessage
from langgraph.types import interrupt

from three_amigos.agents._common import _save_output


def human_review_node(state: ThreeAmigosState) -> dict:
    """Interrupt: pause for the human to approve or request revisions."""
    user_stories = state.get("user_stories", "")
    fr = state.get("functional_requirements", "")
    nfr = state.get("non_functional_requirements", "")
    discussion_round = state.get("discussion_round", 0)

    review_summary = (
        f"## Three Amigos Discussion Complete  (Round {discussion_round})\n\n"
        f"### Functional Requirements\n\n{fr}\n\n"
        f"### Non-Functional Requirements\n\n{nfr}\n\n"
        f"### User Stories with Acceptance Criteria\n\n{user_stories}\n\n"
        "---\n\n"
        "**Please review and respond with:**\n"
        "- Type **APPROVED** to accept these requirements.\n"
        "- Or provide specific feedback for further refinement.\n"
    )

    # Save the review summary to a file so the human can read it at leisure
    _save_output(state, "human_review_summary", review_summary,
                 title="Human Review — Summary of All Artifacts")

    human_response = interrupt(
        {
            "type": "review",
            "summary": review_summary,
            "message": (
                "The Three Amigos discussion is complete. "
                "Please review the output above.\n"
                "💡  All artifacts have also been saved to individual "
                "files in the session output directory."
            ),
        }
    )

    approved = "APPROVED" in str(human_response).upper()

    result: dict = {
        "messages": [
            HumanMessage(content=f"[HUMAN REVIEW]\n{human_response}")
        ],
        "human_approved": approved,
    }

    if not approved:
        # Feed human feedback into the next discussion round
        result["po_feedback"] = f"Human reviewer feedback: {human_response}"

    return result
