import vertexai
from google.adk.agents import Agent
from vertexai import agent_engines

from agent_tools.forex_tool import get_exchange_rate

client = vertexai.Client(
    project="agent-labs-445716",
    location="europe-west2",
)

agent = Agent(
    model="gemini-2.0-flash",
    name="currency_exchange_agent",
    tools=[get_exchange_rate],
)

app = agent_engines.AdkApp(agent=agent)
