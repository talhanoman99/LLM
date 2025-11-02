from typing import Annotated

from langchain_google_genai import ChatGoogleGenerativeAI
from typing_extensions import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()
# Define the state for the graph
class State(TypedDict):
    messages: Annotated[list, add_messages]


# Set up the chatbot model
# Make sure you have set your GOOGLE_API_KEY environment variable
#llm = ChatGoogleGenerativeAI(model="Gemini-2.5-Flash")
llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0, 
        model_provider="google_genai")


# Define the chatbot node
def chatbot(state: State):
    """
    This function is a node in the graph. It takes the current state,
    invokes the chatbot model with the messages from the state,
    and returns a dictionary with the model's response.
    """
    return {"messages": [llm.invoke(state["messages"])]}


# Build the graph
graph_builder = StateGraph(State)

# Add the chatbot node
graph_builder.add_node("chatbot", chatbot)

# Set the entry point to the chatbot node
graph_builder.set_entry_point("chatbot")

# Set the finish point to the chatbot node
graph_builder.set_finish_point("chatbot")

# Compile the graph
graph = graph_builder.compile()

# Run the graph and stream the output
while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in graph.stream({"messages": ("user", user_input)}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)
