from supervisor_worker.local_states._state_ import AgentState


def route(state: AgentState) -> str:
    iterations = state.get("iterations", {})
    max_iter_per_phase = state.get("max_iterations_per_phase", 3)
    verdict = state.get("verdict", "APPROVE")
    phase = state.get("phase", "ba")
    has_ixd_output = bool(state.get("ixd_output"))

    # Determine current iteration count for the active phase
    current_iter = iterations.get(phase if phase in ("ba", "ixd") else "ixd", 0)

    # 1. Safety valve: check iteration limits per phase
    if current_iter >= max_iter_per_phase:
        print(f"[Router] Safety valve: Max iterations ({max_iter_per_phase}) reached for phase '{phase}'.")
        if not has_ixd_output:
            print("[Router] Advancing to Interaction Designer.")
            return "interaction_designer"
        print("[Router] Advancing to Deliverables Compiler.")
        return "compile_deliverables"

    # 2. Explicit END / Completed phase check
    if phase in ("END", "finish", "completed"):
        print("[Router] Workflow approved. Compiling deliverables.")
        return "compile_deliverables"

    # 3. BA Phase (Before IxD has produced output)
    if not has_ixd_output:
        if verdict == "REVISE":
            print("[Router] Routing to Business Analyst for revisions.")
            return "business_analyst"
        print("[Router] BA approved! Routing to Interaction Designer.")
        return "interaction_designer"

    # 4. IxD Phase (After IxD has produced output)
    if verdict == "REVISE":
        print("[Router] Routing to Interaction Designer for revisions.")
        return "interaction_designer"

    print("[Router] IxD approved! Advancing to Deliverables Compiler.")
    return "compile_deliverables"