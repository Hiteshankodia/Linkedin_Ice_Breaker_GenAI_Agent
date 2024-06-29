import os
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.tools import Tool
#tool is the interface that helps langchain agents, chains or llm used and interact with the external world 
from langchain.agents import (
    create_react_agent, 
    AgentExecutor,
)
from langchain import hub
#This will have the premade prompt form the community 


def lookup(name : str) -> str: 
    #This will search the name on the linkedin By name and fetch the linkedin URL. 

    return 