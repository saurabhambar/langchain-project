from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage


load_dotenv()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query:The query to search for
    Returns:
        The search results
    """
    print(f"Searching for: {query}")
    return "Tokyo weather is Sunny"

llm = ChatOllama(model="llama3.1:latest")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    
    print("Hello from langchain-project!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    # agent is runnable - in order to run the agent -> we need to give it a dict with message field.
    print(result)

if __name__ == "__main__":
    main()
