import streamlit as st
import requests

st.set_page_config(page_title="Joke Generator", page_icon="😄", layout="centered")
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
st.markdown("""
    <style>
       .stApp{
            background: black;
            color: white;
            }
        h1 {
    animation: fadeIn 3s ease-in-out;
   background-image: linear-gradient(to right, red, rgb(234, 250, 4),rgb(33, 188, 9));
    --webkit-background-clip: text;
    color: transparent; /* Makes the text color transparent so the gradient shows */
}
        /* Stylish Gradient Button */
        .stButton>button {
            background: linear-gradient(45deg, #ff6a00, #ee0979);  /* Gradient from orange to pink */
            color: white;  /* Text color */
            border: none;  /* No border */
            border-radius: 50px;  /* Rounded corners */
            padding: 15px 32px;  /* Spacing around text */
            font-size: 16px;  /* Text size */
            font-weight: bold;  /* Bold text */
            cursor: pointer;  /* Cursor changes to pointer on hover */
            transition: all 0.4s ease;  /* Smooth transition for all effects */
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);  /* Shadow effect */
            text-transform: uppercase;  /* Uppercase text */
        }

        /* Button Hover Effect */
        .stButton>button:hover {
            color: white;
            background: linear-gradient(45deg, #ee0979, #ff6a00);  /* Inverted gradient */
            transform: scale(1.05);  /* Slightly grow the button */
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);  /* Darker shadow on hover */
        }

        /* Fade-in effect for the title */
        @keyframes fadeIn {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("Random J😄ke Generator")
    st.write("Click the button below to generate a random Joke")

    if st.button("Generate Joke! "):
        joke = random_joke()
        st.success(joke)

    st.divider()

    st.markdown(
        """
        <div style='text-align:center;'>
        <p> Joke from Official Joke API</p>
        <p><u> Build by Musssarat Shamsher. </u></p>
        </div>
""", unsafe_allow_html=True
    )         

if __name__ == "__main__":
    main()

