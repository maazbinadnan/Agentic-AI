from langchain.tools import tool
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "claude-sonnet-4-6",
    temperature=0
)

# Define tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a * b


# Augment the LLM with tools
tools = [multiply]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)

