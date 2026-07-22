from global_client_layer.llm_client import get_llm

llm = get_llm(test=True)

print(llm.get_num_tokens("hello"))
for chunk in llm.stream("hello"):
    print(chunk.content, end= "")

print(llm.to_json())