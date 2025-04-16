import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Generate a key (this should be stored securely in production)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# In-memory data storage
stored_data = {}  # {"user1_data": {"encrypted_text": "xyz", "passkey": "hashed"}}

# Initialize session state for failed_attempts if it doesn't exist
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

# Function to hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Function to encrypt data
def encrypt_data(text, passkey):
    return cipher.encrypt(text.encode()).decode()

# Function to decrypt data
def decrypt_data(encrypted_text, passkey):
    if st.session_state.failed_attempts >= 3:
        return None

    hashed_passkey = hash_passkey(passkey)

    for key, value in stored_data.items():
        if value["encrypted_text"] == encrypted_text and value["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0  # Reset attempts after successful decryption
            return cipher.decrypt(encrypted_text.encode()).decode()
    
    st.session_state.failed_attempts += 1
    return None

# Streamlit UI
st.title("🔒 Secure Data Encryption System")
st.markdown("""
    <style>
    /* General app background */
    .stApp {
        background-color: black;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: black !important; 
        border-radius: 20px;
        box-shadow: 0 4px 5px white;
        color: white;
    }

    /* Sidebar selectbox, radio buttons, and buttons */
    .css-1d391kg .stSidebar .stSelectbox, 
    .css-1d391kg .stSidebar .stRadio, 
    .css-1d391kg .stSidebar .stButton {
        background-color: transparent !important;
        color: white !important;
    }

    /* Title and subheader customizations */
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
    }
    .subheader {
        font-size: 30px;
        font-weight: bold;
        color: #2980b9;
    }

    /* Styling for buttons and text */
    .button {
        background-color: #3498db;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }

    /* Error and success message styles */
    .error {
        color: red;
    }
    .success {
        color: green;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data, passkey)
            stored_data[encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            st.success("✅ Data stored securely!")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    encrypted_text = st.text_area("Enter Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            decrypted_text = decrypt_data(encrypted_text, passkey)

            if decrypted_text:
                st.success(f"✅ Decrypted Data: {decrypted_text}")
            else:
                st.error(f"❌ Incorrect passkey! Attempts remaining: {3 - st.session_state.failed_attempts}")

                if st.session_state.failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "abc123":  
            st.session_state.failed_attempts = 0  # Reset failed attempts on successful login
            st.success("✅ Reauthorized successfully! Redirecting to Retrieve Data...")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password!")
