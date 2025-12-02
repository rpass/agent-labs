import os

import vertexai
from dotenv import load_dotenv
from google.adk.agents import Agent
from vertexai import agent_engines

from agent_tools.forex_tool import get_exchange_rate

# Load environment variables from .env file
load_dotenv()

client = vertexai.Client(
    project=os.getenv("GOOGLE_CLOUD_PROJECT_ID"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
)

agent = Agent(
    model="gemini-2.0-flash",
    name="currency_exchange_agent",
    tools=[get_exchange_rate],
)

app = agent_engines.AdkApp(agent=agent)
