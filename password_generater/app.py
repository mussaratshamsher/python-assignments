import streamlit as st
import random 
import string

# Set the page configuration
st.set_page_config(page_title="Password Generator", page_icon='🔐', layout="centered")

# Function to generate password
def gene_password(length, use_digits, use_special):
    characters = string.ascii_letters  
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Custom CSS for gradient button and smooth color transform
st.markdown("""
    <style>
        /* Title Animation */
        h1 {
            animation: fadeIn 3s ease-in-out;
            animation-iteration-count: infinite;
            color:red;
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

# App title
st.title("🔓Password Generator🔐")

# Slider for password length
length = st.slider("Select Password Length", min_value=6, max_value=30, value=8)

# Checkboxes for including digits and special characters
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

# Generate button
if st.button("Generate Password"):
    password = gene_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")

# Footer
st.write("-------------------------------------------")
st.write("Designed with 💖 by [Mussarat Shamsher](https://github.com/mussaratshamsher?tab=repositories)")
