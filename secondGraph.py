from typing import TypedDict,List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    values:list[int]
    name: str
    result:str

def process_value(state:AgentState)->AgentState:
    '''This function handles multiple different inputs'''

    state["result"]=f"Hi there {state["name"]}! Your sum = {sum(state["values"])} "
    return state

graph=StateGraph(AgentState)

graph.add_node("processor",process_value)

graph.set_entry_point("processor")
graph.set_finish_point("processor")

app=graph.compile()

with open("graph2.png","wb") as f:
    f.write(app.get_graph().draw_mermaid_png())


answers=app.invoke({"values":[1,2,3,4],"name":"Noman"})
print(answers)
print(answers["result"])

