import streamlit as st

def main():
    st.title("Simple Calculator")
    st.write("Enter two numbers and select an operation:")

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Number 1", value=0.0)
    with col2:
        num2 = st.number_input("Number 2", value=0.0)

    operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Exponent"])

    if st.button("Calculate"):
        try:
            if operation == "Addition":
                result = num1 + num2
            elif operation == "Subtraction":
                result = num1 - num2
            elif operation == "Multiplication":
                result = num1 * num2 
            elif operation == "Division":
                if num2 == 0:
                    st.error("Cannot divide by zero")
                    return
                result = num1 / num2
            elif operation == "Modulus":
                result = num1 % num2
            elif operation == "Exponent":
                result = num1 ** num2
            else:
                result = None
                st.error("Invalid operation")
                
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# CSS to style the app
st.markdown("""
    <style>
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .stTitle {
            font-family: 'Arial', sans-serif;
            font-size: 32px;
            color: #2e3b4e;
        }
        .stTextInput input {
            font-size: 16px;
        }
        .stSelectbox select {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
