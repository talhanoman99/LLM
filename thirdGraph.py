from typing import TypedDict #imports all the data types we need
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name:str
    age:str
    final:str

def first_Node(state:AgentState) -> AgentState:
    """This is the first node of our sequence"""
    state["final"]=f"Hi {state["name"]}!"
    return state

def second_Node(state:AgentState) -> AgentState:
    """This is the second node of our sequence"""
    state["final"]= state["final"]+ f" you are {state["age"]} years old !"
    return state

graph=StateGraph(AgentState)

graph.add_node("first_node",first_Node)
graph.add_node("second_node",second_Node)

graph.set_entry_point("first_node")

graph.add_edge("first_node","second_node")

graph.set_finish_point("second_node")

app=graph.compile()

with open("third.png","wb") as f:
    f.write(app.get_graph().draw_mermaid_png())

result=app.invoke({"name":"Noman","age":"42"})
print(result)








    
