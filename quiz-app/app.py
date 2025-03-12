import streamlit as st
import random
import time

# Set page config
st.set_page_config(page_title="Quiz Application", page_icon="📝", layout="centered")

# Add background image and animations
st.markdown(
    """
    <style>
        .stApp {
    background: linear-gradient(135deg, #f0f4f8, #d1e8e2); /* Soft diagonal gradient */
    color: black;
}
        h1, h2 {
            animation: slideIn 2s ease-out;
        }
        @keyframes slideIn {
            from {
                transform: translateX(-100%);
            }
            to {
                transform: translateX(0);
            }
        }
        .stButton>button {
    background-image: linear-gradient(45deg, #ff6f61, #d4af37);
    color: white;
    font-size: 18px;
    padding: 12px 24px;
    border-radius: 50px;
    border: none;
    position: relative;
    overflow: hidden;
    transition: background-color 0.4s ease, transform 0.3s ease;
}
.stButton>button:before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 300%;
    height: 300%;
    background: linear-gradient(45deg, #ff6f61, #d4af37);
    animation: wave 3s infinite;
    z-index: 0;
    border-radius: 50%;
}
.stButton>button:hover {
    background-color: #f8a502;
    transform: scale(1.05);
    color: white;
}
.stButton>button span {
    position: relative;
    z-index: 1;
}
@keyframes wave {
    0% {
        transform: translateX(0);
    }
    100% {
        transform: translateX(-100%);
    }
}
        .stRadio>label {
            font-size: 18px;
        }
          

    </style>
    """, unsafe_allow_html=True
)

# Title and subheader with animation
st.title("📝 Quiz Application")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Jupiter", "Saturn", "Earth"],
        "answer": "Jupiter"
    },
    {
        "question": "which is the capital of Pakistan?",
        "options": ["Islamabad", "Karachi", "Lahore", "Quetta"],
        "answer": "Islamabad"
    },
    {
        "question" : "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Pushto", "Sindhi", "Urdu"],
        "answer": "Urdu"
    },
    {
        "question": "What is currency of Pakistan?",
        "options": ["Rupees", "Coin", "Dollar", "Euro"],
        "answer": "Rupees"
    }
]

# Manage session state to keep track of current question
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question
st.subheader(question["question"])

# Radio button for answer options
selected_option = st.radio("Choose your answer", question["options"], key="answer")

# Submit button with animation and style
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct Answer!")
        st.balloons()
    else:
        st.error(f"❌ Wrong Answer! The correct answer is: {question['answer']}")
    
    time.sleep(3)
    st.session_state.current_question = random.choice(questions)
    st.rerun()
