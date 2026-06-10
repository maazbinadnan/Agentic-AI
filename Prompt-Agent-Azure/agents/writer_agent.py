"""
WriterAgent — Agent 2
=====================
Uses the official Azure AI Projects SDK pattern per the documentation:
  - project.agents.create_agent()  →  creates a runnable agent
  - project.agents.create_thread() →  creates a conversation thread
  - project.agents.create_message() → adds a user message
  - project.agents.create_and_process_run() → runs the agent and polls to completion
  - project.agents.list_messages()  → retrieves the response
  - project.agents.delete_agent()   → cleans up the ephemeral agent

create_version() is called separately at the end of each iteration by the
orchestrator to register the prompt version in Foundry for audit purposes.
"""

from __future__ import annotations

from azure.ai.projects import AIProjectClient


class WriterAgent:
    """Generates Given/When/Then user stories from a raw research document.

    A new ephemeral agent is created for each call so that the evolving
    system prompt is always applied cleanly. The agent is deleted after
    each call to avoid resource leaks.
    """

    def __init__(self, project: AIProjectClient, model: str = "gpt-4o-mini") -> None:
        self.project = project
        self.model = model

    def run(self, system_prompt: str, research_document: str) -> str:
        """Run the writer agent and return its full text response.

        Args:
            system_prompt: The current iteration's system instructions.
            research_document: The raw user research content to analyse.

        Returns:
            The agent's text output (draft user stories as a string).

        Raises:
            RuntimeError: If the agent run fails on the Azure side.
        """
        # Create an ephemeral runnable agent with the current prompt
        agent = self.project.agents.create_agent(
            model=self.model,
            name="writer-agent-ephemeral",
            instructions=system_prompt,
        )

        try:
            thread = self.project.agents.create_thread()

            self.project.agents.create_message(
                thread_id=thread.id,
                role="user",
                content=(
                    "Please generate user stories from the following user research document:\n\n"
                    f"{research_document}"
                ),
            )

            run = self.project.agents.create_and_process_run(
                thread_id=thread.id,
                agent_id=agent.id,
            )

            if run.status == "failed":
                raise RuntimeError(
                    f"Writer agent run failed. Status: {run.status}. "
                    f"Error: {getattr(run, 'last_error', 'unknown')}"
                )

            # Messages are returned newest-first; return the first assistant message
            messages = self.project.agents.list_messages(thread_id=thread.id)
            for msg in messages.data:
                if msg.role == "assistant":
                    content = msg.content[0]
                    if hasattr(content, "text"):
                        return content.text.value
                    return str(content)

            return ""

        finally:
            # Always clean up the ephemeral agent, even if the run throws
            try:
                self.project.agents.delete_agent(agent.id)
            except Exception:
                pass
