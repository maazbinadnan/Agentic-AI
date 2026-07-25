from supervisor_worker.local_states._state_ import AgentState

def route(state: AgentState) -> str:
    iteration = state.get("iteration_count", 0)
    max_iterations = state.get("max_iterations", 3)
    verdict = state.get("verdict", "APPROVE")

    # 1. Safety valve: stop if max iterations reached
    if iteration > max_iterations:
        print("ending due to max iterations reached")
        return "FINISH"

    # 2. Re-run BA worker if revision requested
    if verdict == "REVISE":
        print("sending to BA to revise again")
        return "business_analyst"

    # 3. Approved or default -> finish workflow
    print("finished")
    return "FINISH"