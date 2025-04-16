
import streamlit as st
import time

st.set_page_config( page_title="About", page_icon="🌠", layout="centered")
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
            margin-top: 58px;}   
</style>
""", unsafe_allow_html=True)


st.title("About Application")
st.write("This is a simple web applicaiton to demonstrate the use of Streamlit for creating a Python-based website.")


# Skills list
skills = [
    "HTML",
    "CSS",
    "Tailwind CSS",
    "JavaScript",
    "TypeScript",
    "Next.js"
]
st.title("Skills")

col1, col2 = st.columns(2)

# Loop through each skill and display its progress in one of the columns
for index, skill in enumerate(skills):
    # Choose column based on index (even indices go to col1, odd to col2)
    if index % 2 == 0:
        col = col1
    else:
        col = col2
    
    with col:
        # Display the skill name
        st.write(f"### {skill}")
        
        
        # Create a progress bar for each skill
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Simulate progress (adjust the sleep time for simulation speed)
        for i in range(1, 101):
            time.sleep(0.01)  # Simulate the time taken to learn the skill
            progress_bar.progress(i)  # Update the progress bar
            status_text.text(f"{skill} Progress: {i}%")  # Update text
        
