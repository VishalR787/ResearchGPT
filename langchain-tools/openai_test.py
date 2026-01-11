from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import tool

# Define tool
@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# OpenAI model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Create agent
agent = initialize_agent(
    tools=[get_weather],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
)

# Run agent
response = agent.invoke("what is the weather in sf?")
print(response)
