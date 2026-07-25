from supervisor_worker.local_states._state_ import AgentState


def route(state: AgentState) -> str:
    iteration = state.get("iteration_count", 0)
    max_iterations = state.get("max_iterations", 3)
    verdict = state.get("verdict", "APPROVE")
    phase = state.get("phase", "ba")
    has_ixd_output = bool(state.get("ixd_output"))

    # 1. Safety valve: stop loop if max iterations reached
    if iteration >= max_iterations:
        print(f"[Router] Safety valve: Max iterations ({max_iterations}) reached for phase '{phase}'.")
        if not has_ixd_output:
            print("[Router] Advancing to Interaction Designer.")
            return "interaction_designer"
        print("[Router] Finishing workflow.")
        return "FINISH"

    # 2. Explicit END phase check
    if phase in ("END", "finish"):
        print("[Router] Workflow complete.")
        return "FINISH"

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

    print("[Router] Interaction Designer approved! Finishing workflow.")
    return "FINISH"