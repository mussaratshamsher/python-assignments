import streamlit as st
import requests

def random_joke():
    """"Fetch a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random")
        
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']}\n\n{joke_data['punchline']}"
        else: 
            return "Failed to fetch a joke. Please try again later."
    except:
          return "An error occurred while fetching a joke. Please try again later."

def main():
    st.title(" Random J😄ke Generator")
    st.write("Click the button below to generate a random Joke")

    if st.button("Generate Joke! "):
        joke = random_joke()
        st.success(joke)

    st.markdown("---")
    st.divider()

    st.markdown(
        """"
        <div style='text-align:center;'>
        <p>Joke from Official Joke API</p>
        <p>Build by Musssarat Shamsher
        </div>
""", unsafe_allow_html=True
    )         

if __name__ == "__main__":
    main()





