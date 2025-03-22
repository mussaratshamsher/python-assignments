import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(  # AsyncOpenAI
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(  # OpenAIChatCompletionsModel
    model="gemini-2.0-flash",
    openai_client=provider
)

agent = Agent(
    name="Greeting Agent",
    instructions="I am a greeting agent. I can help you with greetings.",
    model=model,
)
result = Runner.run_sync(agent, "Hello, how are you?")
print(result.final_output)
