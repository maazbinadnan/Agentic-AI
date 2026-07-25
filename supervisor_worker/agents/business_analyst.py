from supervisor_worker._common_ import llm,load_prompt
from supervisor_worker._state_ import AgentState
from global_layer.state import RequirementsPipelineOutput
from global_layer.functions import _save__requirement_files

from langchain.messages import SystemMessage, HumanMessage
from typing import cast

def generate(state:AgentState):

    #load prompt 
    system_prompt = load_prompt("business_analyst.md")
    input_val = state.get("input")
    assert input_val is not None
    #load data
    data = input_val

    #build message history
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"{data}"),
    ]

    print("Generating Business Analyst Output")
    
    structured_llm = llm.with_structured_output(RequirementsPipelineOutput)
    response = cast(RequirementsPipelineOutput,structured_llm.invoke(messages))

    #save the requirement file
    _save__requirement_files(response, output_dir= state['output_dir'])

    return {
        "messages" : messages
    }
