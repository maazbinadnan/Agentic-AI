In this folder, we aim to measure the performance of a Single specialized Agent LLM system using langGraph. The flow is as follows. The Agent reads the user research and generates a candidate backlog of user stories and acceptance criteria expressed as Behaviour-Driven Development (BDD) Given-When-Then statements. Each LLM prompt will be optimized to provide the best maximum output. This is the first baseline that we will create to establish our findings. 

# Single Agent

This component implements a single-agent workflow for evaluating and refining requirements using large language models (LLMs). It provides a simple pipeline to run an LLM with a configurable system prompt, collect its outputs, and store intermediate reasoning and final evaluations. The folder includes:

- `main.py`: entry point to run the single-agent process.
- `functions.py`: helper functions used by the agent (prompting, I/O, formatting).
- `prompts/system_prompt.md`: the system prompt used to configure agent behavior.
- `states/`: runtime state management and saved conversation traces.
- `1/` and `7-18-2026/`: example run outputs and reasoning traces for different model configurations.

This module is intended for experiments that compare LLM outputs, analyze functional and non-functional evaluations, and prototype single-agent refinement loops. It's lightweight and designed for easy integration into the larger project evaluation framework.