

import streamlit as st
import random
import time
import requests

st.set_page_config(page_title="Money Making Machine", page_icon="", layout="centered")
st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000 )
st.subheader("Instant Cash Generater")
if st.button("Generate Money"):
   st.write("Counting your money...") 
   time.sleep(1)  #1s delay
   amount = generate_money()
   st.success(f"You made ${amount}..❗") 

def fetch_side_hustle():
    try:
       response = requests.get("https://fastapi-api.vercel.app/side_hustles")
       if response.status_code == 200:
            hustles = response.json()
            print(hustles)
            return hustles["side_hustle"]
       else:      
            return ("Freelancing")    

    except:
        return ("Something went wrong.")

st.subheader("Side Hustle Ideas")
st.button("Generate Hustle")
idea = fetch_side_hustle()
st.success(idea)

def fetch_money_quote():
    try:
       response = requests.get("https://fastapi-api.vercel.app/money_quotes")
       if response.status_code == 200:
           quotes = response.json()
           return quotes["money_quote"]
       else:
           return ("Money is the root of all evil❗")
    except:
        return("Something went wrong❗")

st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quote()
    st.info(quote)

