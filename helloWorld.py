from typing import TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    message:str

def greeting_Node(state:AgentState) -> AgentState:
    """Simple node that adds a greeting message to the state"""
    state['message']="Hey"+ state['message'] + "how is your day going "
    return state

graph=StateGraph(AgentState)

graph.add_node("greeter",greeting_Node)

graph.set_entry_point("greeter")    
graph.set_finish_point("greeter")

app=graph.compile()

with open("graph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())

result=app.invoke({'message':"Bob"})
print(result)