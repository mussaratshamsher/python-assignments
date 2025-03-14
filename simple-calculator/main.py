import streamlit as st

def main():
    st.title("Simple Calculator")
    st.write("Enter two numbers and select an operation:")

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Number 1", value=0.0)
    with col2:
        num2 = st.number_input("Number 2", value=0.0)

    operation = st.selectbox("Select Operation",["Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Exponent"])

    if st.button("Calculate"):
         try:
             if operation == "Addition":
                 result = num1 + num2
             elif operation == "Subtraction":
                 result = num1 - num2
             elif operation == "Multiplication":
                 result = num1 * num2 
                      
             elif operation == "Modulus":
                 result = num1 % num2
             elif operation == "Exponent":
                 result = num1 ** num2
             elif operation == "Division":
                 result = num1 / num2
             else:
                  if num2 == 0:
                      st.error("Cannot divide by zero")
                  return
             result = num1/ num2     
             st.success(f"Result: {result}")
         except ZeroDivisionError:
             st.error("An error occured: {str(e)}")

if __name__ == "__main__":
    main()
          



