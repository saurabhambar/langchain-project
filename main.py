from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel, Field

class Source(BaseModel):
    """Schema for a source used by the agent"""
    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for the agent's response with answer and sources"""
    answer: str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

load_dotenv()

llm = ChatOllama(model="llama3.1:latest")
tools = [TavilySearch]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    
    print("Hello from langchain-project!")
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkdien and list thier details")]})
    # agent is runnable - in order to run the agent -> we need to give it a dict with message field.
    print(result)

if __name__ == "__main__":
    main()
