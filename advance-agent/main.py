import os
import chainlit as cl
from dotenv import load_dotenv
from typing import Optional, Dict
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(model="gemini-2,0-flash", openai_client=provider)

@function_tool("get_weather")
def get_weather(location: str, unit: str = "C") -> str:
    """
    Fetch the weather for a given location, reutrn the weather.
    """
    return f"The weather in {location} is 22 degrees{unit}"

agent = Agent()
# agent.add_tool(get_weather)
# runner = Runner(agent=agent, model=model)
#docorator
@cl.oauth_callback
def oath_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],  
    default_user: cl.User,  
) -> Optional[cl.User]: 
    """
    Handle the OAuth callback from the provider
    """
    print(f"Provider: {provider_id}")
    print(f"User data: {raw_user_data}")

    return default_user

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])

    await cl.Message(content="Hello! How can I help you today?").send()

@cl.on_message
async def handel_message(message: cl.Message):

    history = cl.user_session.get("history")

    history.append({"role": "user", "content": message.content})
     
    formatted_history = []
    for msg in history:
        role = "user" if msg["role"] == "user" else "model"
        formatted_history.append({"role": role, "parts": [{"text": msg["content"]}] }) 

    response = model.generate_content(formatted_history)

    response_text = response.text if hasattr(response, "text") else ""
    
    history.append({"role": "assistant", "content": response_text})

    cl.user_session.set("history", history)
     
    await cl.Message(content=response_text).send()


