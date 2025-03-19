import os # for environment variables
import chainlit as cl # for chatbot
import google.generativeai as genai # for generative model
from dotenv import load_dotenv # for loading environment variables

load_dotenv() # load environment variables

gemini_api_key = os.getenv("GEMINI_API_KEY") # get the api key from environment variables

genai.configure(api_key=gemini_api_key) # configure the generative model

model = genai.GenerativeModel(model_name="gemini-2.0-flash") # create the generative model

@cl.on_chat_start # handle chat start event
async def handle_chat_start(): 
 # send a message to the user
    await cl.Message(content="Hello! how can I help you today?").send()

@cl.on_message # handle message event
async def handle_message(message: cl.Message): # handle message event
    
    prompt = message.content # get the message content

    response = model.generate_content(prompt) # generate a response

    response_text = response.text if hasattr(response, "text") else "" # get the response text
    await cl.Message(content=response_text).send() # send the response to the user


