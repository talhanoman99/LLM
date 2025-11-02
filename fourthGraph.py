from typing import TypedDict
from langgraph.graph import StateGraph,START,END

class AgentState(TypedDict):
    num1:str
    operation:str
    num2:str
    finalNumber:str

def adder(state:AgentState)->AgentState:
    """This node adds the two number"""

    state["finalNumber"]=state["num1"]+state["num2"]
    return state

def subtract(state:AgentState)->AgentState:
    """This node subtract the two nodes"""

    state["finalNumber"]=state["num1"]-state["num2"]
    return state

def decideNextNode(state:AgentState)->AgentState:
    """This node will select the next node of the graph"""

    if state["operation"]=="+":
        return "addition_operation"
    elif state["operation"]=="-":
        return "suntract_operation"
    
graph=StateGraph(AgentState)

graph.add_node("add_node",adder)
graph.add_node("subtarct_node",subtract)
graph.add_node("router",lambda state:state)#passthrough function

graph.add_edge(START,"router")
graph.add_conditional_edges(
    "router",
    decideNextNode,
    {
        #Edge:Node
        "addition_operation":"add_node",
        "suntract_operation":"subtarct_node"
    }
)

graph.add_edge("add_node",END)
graph.add_edge("subtarct_node",END)

app=graph.compile()

with open("graph4.png","wb")as f:
    f.write(app.get_graph().draw_mermaid_png())

initial_state_1=AgentState(num1=10,operation="-",num2=5)
print(app.invoke(initial_state_1))




 




    

    




