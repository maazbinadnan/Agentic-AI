"""
RL-Style Two-Tier Agent System — Orchestrator
=============================================

Iteratively improves the writer agent's system prompt until Agent 2 produces
user stories that score >= PASS_THRESHOLD against the gold-standard stories
held by Agent 1 (the evaluator).

Loop flow
---------
1. Load gold stories, research doc, and seed prompt.
2. For each iteration (up to MAX_ITERATIONS=10):
   a. Save the current prompt as prompts/history/writer_prompt_v{n}.md
   b. Agent 2 (WriterAgent) uses create_agent() to run the current prompt
      against the research document and produce draft user stories.
   c. Agent 1 (EvaluatorAgent) scores the draft against the gold stories and
      returns {score, feedback, improved_prompt}.
   d. Append a structured entry to logs/run_log.jsonl.
   e. If score >= PASS_THRESHOLD  →  exit the loop (success).
   f. Else  →  replace current_prompt with improved_prompt and repeat.
3. Write the best-scoring prompt to writer_prompt.md.
4. Persist the winning prompt to Azure AI Foundry via create_version() for
   audit and reuse (separate from the run-time create_agent() calls).

Key API distinction (per official docs)
----------------------------------------
- create_agent()   → creates a RUNNABLE agent (used during the loop).
- create_version() → registers a VERSIONED PROMPT DEFINITION in Foundry
                     (used only at the end to persist the winner).

Environment variables (.env)
-----------------------------
AZURE_PROJECT_ENDPOINT  — required
AGENT_MODEL             — optional, default: gpt-4o-mini
PASS_THRESHOLD          — optional, default: 8  (integer 0–10)
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from dotenv import load_dotenv

from agents.writer_agent import WriterAgent
from agents.evaluator_agent import EvaluatorAgent

# ── Load .env ─────────────────────────────────────────────────────────────────
load_dotenv()

# ── Configuration ─────────────────────────────────────────────────────────────
PROJECT_ENDPOINT: str = os.environ["AZURE_PROJECT_ENDPOINT"]
MODEL: str = os.getenv("AGENT_MODEL", "gpt-4o-mini")
PASS_THRESHOLD: int = int(os.getenv("PASS_THRESHOLD", "8"))
MAX_ITERATIONS: int = 10
WRITER_AGENT_NAME: str = "USER-STORY-WRITER"

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
PROMPTS_DIR = BASE_DIR / "prompts"
HISTORY_DIR = PROMPTS_DIR / "history"
LOGS_DIR = BASE_DIR / "logs"

GOLD_STORIES_PATH = DATA_DIR / "gold_stories.md"
RESEARCH_INPUT_PATH = DATA_DIR / "research_input.md"
SEED_PROMPT_PATH = PROMPTS_DIR / "writer_seed_prompt.md"
EVALUATOR_PROMPT_PATH = PROMPTS_DIR / "evaluator_prompt.md"
FINAL_PROMPT_PATH = BASE_DIR / "writer_prompt.md"
LOG_PATH = LOGS_DIR / "run_log.jsonl"

# ── ANSI colour helpers (graceful fallback on Windows without VT) ─────────────
try:
    import colorama
    colorama.init()
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
except ImportError:
    GREEN = YELLOW = RED = CYAN = RESET = BOLD = ""


# ── Helpers ───────────────────────────────────────────────────────────────────

def _load_file(path: Path, label: str) -> str:
    """Read a required text file; exit with a clear message if missing/empty."""
    if not path.exists():
        print(f"{RED}[ERROR]{RESET} {label} not found: {path}")
        sys.exit(1)
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        print(f"{RED}[ERROR]{RESET} {label} is empty: {path}")
        sys.exit(1)
    return content


def _save_prompt_version(prompt: str, iteration: int) -> Path:
    """Write the current prompt to prompts/history/writer_prompt_v{n}.md."""
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    dest = HISTORY_DIR / f"writer_prompt_v{iteration}.md"
    dest.write_text(prompt, encoding="utf-8")
    return dest


def _log_iteration(
    iteration: int,
    score: int,
    dimension_scores: dict,
    feedback: str,
    prompt_snapshot: str,
) -> None:
    """Append a structured JSON entry to logs/run_log.jsonl."""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    entry = {
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
        "iteration": iteration,
        "score": score,
        "threshold": PASS_THRESHOLD,
        "passed": score >= PASS_THRESHOLD,
        "dimension_scores": dimension_scores,
        "feedback": feedback,
        "prompt_chars": len(prompt_snapshot),
    }
    with LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry) + "\n")



def _persist_to_foundry(project: AIProjectClient, prompt: str) -> None:
    """Push the winning prompt to Azure AI Foundry as a new versioned agent.

    This uses create_version() which is a prompt-management API — separate
    from the create_agent() calls used to run agents during the loop.
    """
    try:
        agent = project.agents.create_version(
            agent_name=WRITER_AGENT_NAME,
            definition=PromptAgentDefinition(
                model=MODEL,
                instructions=prompt,
            ),
        )
        print(
            f"  {GREEN}[FOUNDRY]{RESET} Winning prompt saved → "
            f"'{agent.name}' version {agent.version}"
        )
    except Exception as exc:
        print(f"  {YELLOW}[WARN]{RESET} Could not persist to Foundry: {exc}")


def _print_header() -> None:
    width = 62
    print(f"\n{BOLD}{'─' * width}{RESET}")
    print(f"{BOLD}  RL-Style Prompt Optimiser{RESET}")
    print(
        f"  Model: {CYAN}{MODEL}{RESET} | "
        f"Threshold: {CYAN}{PASS_THRESHOLD}/10{RESET} | "
        f"Max loops: {CYAN}{MAX_ITERATIONS}{RESET}"
    )
    print(f"{BOLD}{'─' * width}{RESET}\n")


def _print_iteration_result(
    iteration: int, score: int, dim: dict, feedback: str
) -> None:
    colour = GREEN if score >= PASS_THRESHOLD else YELLOW
    passed_str = f"{GREEN}PASS{RESET}" if score >= PASS_THRESHOLD else f"{YELLOW}FAIL{RESET}"
    print(f"\n  Score: {colour}{score}/10{RESET} [{passed_str}]")
    print(f"  Dimensions: {dim}")
    # Truncate feedback for console readability
    short_feedback = feedback[:160] + ("…" if len(feedback) > 160 else "")
    print(f"  Feedback:   {short_feedback}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    _print_header()

    # ── Load inputs ───────────────────────────────────────────────────────────
    gold_stories = _load_file(GOLD_STORIES_PATH, "Gold Stories")
    research_doc = _load_file(RESEARCH_INPUT_PATH, "Research Document")
    current_prompt = _load_file(SEED_PROMPT_PATH, "Seed Prompt")
    evaluator_prompt = _load_file(EVALUATOR_PROMPT_PATH, "Evaluator Prompt")

    print(f"  {GREEN}[LOADED]{RESET} Gold stories   → {GOLD_STORIES_PATH.name}")
    print(f"  {GREEN}[LOADED]{RESET} Research doc   → {RESEARCH_INPUT_PATH.name}")
    print(f"  {GREEN}[LOADED]{RESET} Seed prompt    → {SEED_PROMPT_PATH.name}")
    print(f"  {GREEN}[LOADED]{RESET} Evaluator spec → {EVALUATOR_PROMPT_PATH.name}")

    # ── Azure client ──────────────────────────────────────────────────────────
    project = AIProjectClient(
        endpoint=PROJECT_ENDPOINT,
        credential=DefaultAzureCredential(),
    )

    writer = WriterAgent(project=project, model=MODEL)
    evaluator = EvaluatorAgent(project=project, system_prompt=evaluator_prompt, model=MODEL)

    # ── Tracking state ────────────────────────────────────────────────────────
    best_score: int = 0
    best_prompt: str = current_prompt
    winning_iteration: int = 0

    try:
        for iteration in range(1, MAX_ITERATIONS + 1):
            print(f"\n{BOLD}── Iteration {iteration}/{MAX_ITERATIONS} ───────────────────────────{RESET}")

            # (a) Save prompt version before running so v1 = seed, v2 = first improvement, …
            version_path = _save_prompt_version(current_prompt, iteration)
            print(f"  [PROMPT ] Saved → {version_path.name}")

            # (b) Agent 2: Generate draft user stories
            print(f"  [WRITER ] Calling writer agent…")
            draft_stories = writer.run(
                system_prompt=current_prompt,
                research_document=research_doc,
            )
            draft_lines = len(draft_stories.splitlines())
            print(f"  [WRITER ] Done — {draft_lines} lines generated")

            # (c) Agent 1: Evaluate draft against gold standard
            print(f"  [EVAL   ] Calling evaluator agent…")
            evaluation = evaluator.run(
                draft_stories=draft_stories,
                gold_stories=gold_stories,
            )

            score: int = evaluation["score"]
            feedback: str = evaluation["feedback"]
            dim_scores: dict = evaluation.get("dimension_scores", {})
            improved_prompt: str = evaluation.get("improved_prompt", current_prompt)

            _print_iteration_result(iteration, score, dim_scores, feedback)

            # (d) Log the iteration
            _log_iteration(iteration, score, dim_scores, feedback, current_prompt)

            # Track best
            if score > best_score:
                best_score = score
                best_prompt = current_prompt
                winning_iteration = iteration

            # (e) Check exit condition
            if score >= PASS_THRESHOLD:
                print(
                    f"\n  {GREEN}{BOLD}✅ Threshold reached on iteration {iteration} "
                    f"(score {score}/{PASS_THRESHOLD}){RESET}"
                )
                break

            # (f) Improve prompt for next iteration
            print(
                f"  {YELLOW}[OPTIM  ]{RESET} Score {score} < {PASS_THRESHOLD} — "
                "applying improved prompt for next iteration…"
            )
            current_prompt = improved_prompt

        else:
            # Loop exhausted without passing
            print(
                f"\n  {YELLOW}⚠️  Max iterations ({MAX_ITERATIONS}) reached. "
                f"Best score: {best_score}/10 at iteration {winning_iteration}.{RESET}"
            )

    except KeyboardInterrupt:
        print(f"\n  {YELLOW}[ABORT]{RESET} Run interrupted by user.")
    finally:
        evaluator.cleanup()

    # ── Write winning prompt to writer_prompt.md ──────────────────────────────
    FINAL_PROMPT_PATH.write_text(best_prompt, encoding="utf-8")
    print(f"\n  {GREEN}[OUTPUT]{RESET} Winning prompt → writer_prompt.md")

    # ── Persist winning prompt to Azure AI Foundry (create_version) ──────────────────
    _persist_to_foundry(project, best_prompt)

    # ── Final summary ─────────────────────────────────────────────────────────
    print(f"\n{BOLD}{'─' * 62}{RESET}")
    print(f"  Run complete.")
    print(f"  Best score        : {GREEN}{best_score}/10{RESET} (iteration {winning_iteration})")
    print(f"  Prompt history    : {HISTORY_DIR.relative_to(BASE_DIR)}/")
    print(f"  Full run log      : {LOG_PATH.relative_to(BASE_DIR)}")
    print(f"  Final prompt      : writer_prompt.md")
    print(f"{BOLD}{'─' * 62}{RESET}\n")


if __name__ == "__main__":
    main()
