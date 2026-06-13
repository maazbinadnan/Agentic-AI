from langgraph.graph import StateGraph, MessagesState, START, END
from state import BusinessAnalystAgentState
from Agent import parse_input, create_user_stories, write_user_stories

#create the graph 
workflow = StateGraph(BusinessAnalystAgentState)

#add nodes
workflow.add_node("parse_file",parse_input)
workflow.add_node("create_user_stories",create_user_stories)
workflow.add_node("write_stories", write_user_stories)

#edges
workflow.add_edge(START,"parse_file")
workflow.add_edge("parse_file","create_user_stories")
workflow.add_edge("create_user_stories","write_stories")
workflow.add_edge("write_stories",END)

#compile
app = workflow.compile()

initial_state:BusinessAnalystAgentState = {"user_research":"""
Interview Notes: Subject A (First-Year Undergraduate)

"When I went to the freshers' fair, it was completely overwhelming. There are over 150 societies. I'm really into niche things, like mathematical modeling in sports and board games, but I couldn't easily find groups for that. I wish there was a way the university app could just look at my profile, maybe my course or the tags I select, and recommend 3 or 4 societies I'd actually like. Right now, I just rely on word of mouth."

""","filename":"test1000", "user_story": []}

final_state = app.invoke(initial_state)
print(final_state)