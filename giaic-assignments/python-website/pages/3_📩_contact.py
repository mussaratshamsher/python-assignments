import streamlit as st
import streamlit.components.v1 as components

st.set_page_config( page_title="About", page_icon="📩", layout="centered")

st.title("Contact")
st.write("Feel free to explore my work and get in touch if you have any questions or opportunities for collaboration.")

# form for user input
with st.form("contact_form"):
    name = st.text_input("Name", placeholder="Enter your name", max_chars=20)
    email = st.text_input("Email", placeholder="Enter your email")
    message = st.text_area("Message", placeholder="Enter your message", max_chars=1000)
    submit_button = st.form_submit_button("Submit")

# form submission
if submit_button:
    if not name or not email or not message:
        st.error("Please fill in all fields.")
    else:
        # Display a success message (replace with actual email sending logic)
        st.success("Thank you for your message! We'll get back to you soon.")

st.markdown("""
<style>
    .stApp {
    background: linear-gradient(45deg, #FFB6C1, #D3CCE3, #B2F3D2, #FFEB6A); /* Soft pastel colors */
    background-size: 400% 400%; 
    animation: gradientShift 10s ease infinite;
}
@keyframes gradientShift {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}
    .stSidebar{
            background: lavender;
            box-shadow: 0 4px 5px white;
            color: white;
            margin-top: 58px;} 
      .stSubmit_ button{
            background: linear-gradient(45deg, #FF5722, #FFC107);  
            color: white;  
            font-size: 18px;  
            font-weight: bold;  
            padding: 12px;  
            margin: 10px 0;  
            border-radius: 8px;  
            text-decoration: none;  
            transition: all 0.3s ease-in-out;  
        }       
</style>
""", unsafe_allow_html=True)
