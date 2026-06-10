from configurations import Config
from retrieval import Retrieval


config = Config()  
retriever = Retrieval(config=config)

query = input("please enter your query \n")

results = retriever.retrieve(query=query, top_k=10)
context = retriever.build_context_string(results)
stream = retriever.generate_response(query=query, context=context)

print("Response: ", end="", flush=True)

for event in stream:
    # 1. Check if the event object has a 'type' attribute matching a text delta
    # (If your library parses json into objects, use dot notation; if it's a dict, use event.get('type'))
    if getattr(event, 'type', None) == 'response.output_text.delta':
        
        # 2. Extract the text chunk safely
        content = getattr(event, 'delta', None)
        
        if content:
            print(content, end="", flush=True)

# 3. Final newline when the stream completely closes
print()