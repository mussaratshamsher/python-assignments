

import streamlit as st
import random
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000 )
st.subheader("Instant Cash Generater")
if st.button("Generate Money")
   st.write("Counting your money") 
   time.sleep(1)
   amount = generate_money()
   st.success(f"You made ${amount}..❗") 


def fetch_side_hustle():
    try:
       response = requests.get(url)
        if response,status_code == 200:
            hustles = response.json()
            return hustles
        else:
            return ("Freelancing")    

    except:
        return ("Something went wrong.")

st.button("Generate Hustle")
