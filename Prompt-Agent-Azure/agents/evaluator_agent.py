"""
EvaluatorAgent — Agent 1 (Orchestrator)
========================================
Uses the official Azure AI Projects SDK pattern per the documentation:
  - project.agents.create_agent()         →  creates a runnable agent (once, cached)
  - project.agents.create_thread()        →  fresh thread per evaluation
  - project.agents.create_message()       →  adds the user message
  - project.agents.create_and_process_run() → runs and polls to completion
  - project.agents.list_messages()        →  retrieves the structured JSON response
  - project.agents.delete_agent()         →  cleanup on teardown

create_version() is NOT used here — it is a prompt-management API only.
"""

from __future__ import annotations

import json
import re

from azure.ai.projects import AIProjectClient

# Keys that must be present in a valid evaluation response
_REQUIRED_KEYS = {"score", "dimension_scores", "feedback", "improved_prompt"}


class EvaluatorAgent:
    """Scores draft user stories and generates an improved writer prompt.

    The evaluator agent is created once and reused across all iterations.
    A fresh thread is used per call to prevent conversation context bleeding.
    Call :meth:`cleanup` when the run loop finishes to delete the agent.
    """

    def __init__(
        self,
        project: AIProjectClient,
        system_prompt: str,
        model: str = "gpt-4o-mini",
    ) -> None:
        self.project = project
        self.model = model
        self.system_prompt = system_prompt
        self._agent = None  # lazily created on first run()

    # ── Internal helpers ──────────────────────────────────────────────────────

    def _get_or_create_agent(self):
        """Create and cache the evaluator agent on first use."""
        if self._agent is None:
            self._agent = self.project.agents.create_agent(
                model=self.model,
                name="evaluator-agent",
                instructions=self.system_prompt,
            )
        return self._agent

    @staticmethod
    def _extract_json(raw: str) -> str:
        """Strip markdown code fences and return the bare JSON string."""
        cleaned = re.sub(r"```(?:json)?", "", raw).replace("```", "").strip()
        return cleaned

    # ── Public API ────────────────────────────────────────────────────────────

    def run(self, draft_stories: str, gold_stories: str) -> dict:
        """Evaluate draft user stories against the gold standard.

        Args:
            draft_stories: Agent 2's output from the current iteration.
            gold_stories:  The reference gold-standard user stories.

        Returns:
            A dict with keys:
                - ``score`` (int 0–10)
                - ``dimension_scores`` (dict)
                - ``feedback`` (str)
                - ``improved_prompt`` (str)

        Raises:
            RuntimeError: If the agent run fails.
            ValueError: If the response cannot be parsed as valid JSON.
        """
        agent = self._get_or_create_agent()

        # Fresh thread per evaluation — prevents context bleed between iterations
        thread = self.project.agents.create_thread()

        user_message = (
            "Please evaluate the following draft user stories against the gold standard "
            "and return your response as JSON only.\n\n"
            "=== DRAFT USER STORIES ===\n"
            f"{draft_stories}\n\n"
            "=== GOLD STANDARD USER STORIES ===\n"
            f"{gold_stories}"
        )

        self.project.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_message,
        )

        run = self.project.agents.create_and_process_run(
            thread_id=thread.id,
            agent_id=agent.id,
        )

        if run.status == "failed":
            raise RuntimeError(
                f"Evaluator agent run failed. Status: {run.status}. "
                f"Error: {getattr(run, 'last_error', 'unknown')}"
            )

        # Extract the assistant's reply (messages are returned newest-first)
        messages = self.project.agents.list_messages(thread_id=thread.id)
        raw_response = ""
        for msg in messages.data:
            if msg.role == "assistant":
                content = msg.content[0]
                raw_response = content.text.value if hasattr(content, "text") else str(content)
                break

        # Parse and validate JSON
        json_text = self._extract_json(raw_response)
        try:
            result = json.loads(json_text)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Evaluator returned invalid JSON.\n"
                f"Raw response:\n{raw_response}\n"
                f"Parse error: {exc}"
            ) from exc

        missing = _REQUIRED_KEYS - result.keys()
        if missing:
            raise ValueError(
                f"Evaluator JSON is missing required keys: {missing}\n"
                f"Got: {list(result.keys())}"
            )

        # Coerce score to int defensively
        result["score"] = int(result["score"])
        return result

    def cleanup(self) -> None:
        """Delete the persistent evaluator agent from Azure AI Foundry."""
        if self._agent is not None:
            try:
                self.project.agents.delete_agent(self._agent.id)
            except Exception:
                pass
            finally:
                self._agent = None
