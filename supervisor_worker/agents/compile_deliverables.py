from typing import Dict, Any
from global_layer.functions import _compile_deliverables
from supervisor_worker.local_states._state_ import AgentState


def generate(state: AgentState) -> Dict[str, Any]:
    return _compile_deliverables(state, architecture_name="Supervisor-Worker Pattern")
