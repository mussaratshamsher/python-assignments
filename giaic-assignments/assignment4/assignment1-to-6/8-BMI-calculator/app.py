
# BMI Calculator

# Solution:
import streamlit as st
import pandas as pd
import numpy as np

st.title("BMI Calculator")

height = st.slider("Enter your height in cm: \t", 100, 250, 175)
weight = st.slider("Enter your weight in kg: \t", 30, 200, 70)

if st.button("Calculate BMI"):
    bmi = weight / ((height/100) ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

st.write("BMI Categories:")
st.write("Underweight: BMI < 18.5")
st.write("Normal weight: BMI 18.5–24.9")
st.write("Overweight: BMI 25–29.9")
st.write("Obesity: BMI ≥ 30")
