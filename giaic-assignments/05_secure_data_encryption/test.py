import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

st.set_page_config(page_title="Secure Data Encryption System", page_icon="🔐", layout="centered")

# Constants and Data File Paths
DATA_FILE = "secure_data.json"  # File to store data
SALT = b"secure_salt_value"  # Salt for password hashing
LOCKOUT_DURATION = 60  # Lockout duration in seconds

# Initialize session state variables
if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# Load and save user data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}  # Return an empty dictionary if no data file exists

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Generate a key from the passkey
def generate_key(passkey):
    key = pbkdf2_hmac("sha256", passkey.encode(), SALT, 100000)
    return urlsafe_b64encode(key)

# Hash the password to store in the database
def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()

# Encryption function using cryptography.fernet
def encrypt_text(text, key):
    cipher = Fernet(key)
    return cipher.encrypt(text.encode()).decode()

# Decryption function using cryptography.fernet
def decrypt_text(encrypted_text, key):
    try:
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_text.encode()).decode()
    except Exception as e:
        return None  # If decryption fails, return None

stored_data = load_data()  # Load existing user data

# Custom CSS for the app
st.markdown("""
    <style>
        /* General app styles */
        .stApp {
            background-color: black;
            color: white;
        }        
        /* Sidebar styles */
        .stSidebar{
            background: black !important;
            box-shadow: 0 4px 5px white;
            color: white;
            margin-top: 58px;}

        /* Input field styles */
        .stTextInput, .stTextArea, .stPasswordInput {
            background-color: #333;
            color: white;
            border: 1px solid #666;
            padding: 10px;
        }
        /* Text and code styling */
        .stMarkdown {
            color: orange;
        }
        button{
        background: orange !important;
        color: white !important; 
        width: 150px !important;
        border-radius: 10px;}
        button:hover{
        background: white !important;
        color: orange !important;
        border: 1px solid orange;
        box-shadow: 0 4px 5px white;
        }
         
      
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("🔒 Secure Data Encryption System")

# Navigation menu
st.sidebar.title("Navigation")
menu = ["Home", "Register", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.subheader("🎨✍ Features:")
    st.write(""" 📌Users store data with a unique passkey. \n
📌 Users decrypt data by providing the correct passkey. \n
📌 Multiple failed attempts result in a forced reauthorization (login page). \n
📌 The system operates entirely in memory without external databases.""")
elif choice == "Register":
    st.subheader("🔐 Register new user")
    username = st.text_input("Enter Username:")
    password = st.text_input("Enter Password:", type="password")

    if st.button("Register"):
        if username and password:
            if username in stored_data:
                st.warning("Username already exists. Please choose a different one.")
            else:
                stored_data[username] = {
                    "password": hash_password(password),
                    "data": [],
                    "lockout_time": 0
                }
                save_data(stored_data)
                st.success("✅ User registered successfully!")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Login")
    if time.time() < st.session_state.lockout_time:
        remaining = int(st.session_state.lockout_time - time.time())
        st.error(f"Too many failed attempts. Please try again after {remaining} seconds.")
        st.stop()  # Stop further execution if lockout is active

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in stored_data and stored_data[username]["password"] == hash_password(password):
            st.session_state.authenticated_user = username
            st.session_state.failed_attempts = 0
            st.success(f"✅ Welcome, {username}!")
        else:
            st.session_state.failed_attempts += 1
            remaining = 3 - st.session_state.failed_attempts
            st.error(f"❌ Incorrect username or password. Attempts remaining: {remaining}")
            if st.session_state.failed_attempts >= 3:
                st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
                st.error("Too many failed attempts. Please try again later.")
                st.stop()

elif choice == "Store Data":
    if not st.session_state.authenticated_user:
        st.warning("Please login first!")
    else:
        st.subheader("📁 Store Encrypted Data.")
        data = st.text_area("Enter Data:")
        passkey = st.text_input("Enter Passkey:", type="password")

        if st.button("Encrypt & Save"):
            if data and passkey:
                key = generate_key(passkey)  # Generate key for encryption
                encrypted = encrypt_text(data, key)  # Encrypt the data
                stored_data[st.session_state.authenticated_user]["data"].append(encrypted)  # Store encrypted data
                save_data(stored_data)  # Save the updated data
                st.success("✅ Data stored securely!")
            else:
                st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    if not st.session_state.authenticated_user:
        st.warning("⚠️ Please login first!")
    else:
        st.subheader("🔍 Retrieve Your Data")
        user_data = stored_data.get(st.session_state.authenticated_user, {}).get("data", [])
        if not user_data:
            st.info("No data found for this user.")
        else:
            st.write("**Encrypted Data:**")
            for i, item in enumerate(user_data):
                st.code(item, language="text")

            encrypted_input = st.text_area("Enter Encrypted Text")
            passkey = st.text_input("Enter Passkey:", type="password")

            if st.button("Decrypt"):
                key = generate_key(passkey)  # Generate key for decryption
                result = decrypt_text(encrypted_input, key)  # Decrypt the data
                if result:
                    st.success(f"✅ Decrypted Data: {result}")
                else:
                    st.error("❌ Incorrect passkey or corrupted data!")
