"""Supervisor-Worker Agent — CLI Runner for LangGraph Pipeline.

Usage
─────
    python -m supervisor_worker_redone.run --output-dir outputs/test_run_1 -tid "swa_1"
"""

import argparse
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig

from global_layer.functions import _data_file
from review_critique._common_ import _session_dir, save_state
from review_critique.main import create_agent_pipeline, PipelineState


def main() -> None:
    parser = argparse.ArgumentParser(description="Supervisor-Worker Agent CLI Runner")
    parser.add_argument(
        "--output-dir", "-o",
        type=str,
        default="supervisor_worker_agent_outputs",
        help="Output directory path for requirement files.",
    )
    parser.add_argument(
        "--thread-id", "-tid",
        type=str,
        default="swa_1",
        help="Thread ID for graph checkpointing.",
    )
    args = parser.parse_args()

    config: RunnableConfig = {
        "configurable": {"thread_id": args.thread_id},
        "recursion_limit": 50,
    }

    out_dir = _session_dir(args.output_dir)
    raw_input = _data_file()

    print("=======================================================")
    print("Launching Supervisor-Worker Agent Pipeline...")
    print(f"Output Directory: {out_dir}")
    print("=======================================================\n")

    pipeline = create_agent_pipeline()

    instruction = (
        f"Could you extract the requirements from this raw document if needed:\n{raw_input}\n"
        f"and output them into dir: {out_dir} and also give me html mockups and everything"
    )

    initial_state: PipelineState = {
        "messages": [HumanMessage(content=instruction)],
        "output_dir": out_dir,
    }

    print("\n--- Live Execution & Streaming Output ---")

    final_state = pipeline.invoke(
        initial_state,
        config=config,
    )

    state_snapshot = pipeline.get_state(config)
    final_values = state_snapshot.values if state_snapshot else {}

    gen_model = final_values.get("generator_model", "")
    gen_in = final_values.get("generator_input_tokens", 0)
    gen_out = final_values.get("generator_output_tokens", 0)
    gen_tot = final_values.get("generator_total_tokens", 0)

    eval_model = final_values.get("eval_model", "")
    eval_in = final_values.get("eval_input_tokens", 0)
    eval_out = final_values.get("eval_output_tokens", 0)
    eval_tot = final_values.get("eval_total_tokens", 0)

    tot_in = final_values.get("input_tokens", gen_in + eval_in)
    tot_out = final_values.get("output_tokens", gen_out + eval_out)
    tot_all = tot_in + tot_out

    print("\n=======================================================")
    print("Supervisor-Worker Execution Finished!")
    print(f"- Output Directory: {out_dir}")
    print("\nGenerator Model & Token Usage:")
    print(f"- Model:                {gen_model}")
    print(f"- Generator In Tokens:  {gen_in}")
    print(f"- Generator Out Tokens: {gen_out}")
    print(f"- Generator Total:      {gen_tot}")
    print("\nEval Model & Token Usage:")
    print(f"- Model:                {eval_model}")
    print(f"- Eval In Tokens:       {eval_in}")
    print(f"- Eval Out Tokens:      {eval_out}")
    print(f"- Eval Total:           {eval_tot}")
    print("\nCombined Pipeline Total Usage:")
    print(f"- Total Input Tokens:   {tot_in}")
    print(f"- Total Output Tokens:  {tot_out}")
    print(f"- Total Tokens:         {tot_all}")
    print("=======================================================\n")

    save_state({
        "output_dir": out_dir,
        "generator_model": gen_model,
        "generator_input_tokens": gen_in,
        "generator_output_tokens": gen_out,
        "generator_total_tokens": gen_tot,
        "eval_model": eval_model,
        "eval_input_tokens": eval_in,
        "eval_output_tokens": eval_out,
        "eval_total_tokens": eval_tot,
        "input_tokens": tot_in,
        "output_tokens": tot_out,
        "total_tokens": tot_all,
        "messages": [m.content for m in final_values.get("messages", []) if hasattr(m, "content")],
    })


if __name__ == "__main__":
    main()
