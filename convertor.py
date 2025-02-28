import streamlit as st

# Function to convert different units
def convert_length(length, unit_from, unit_to):
    if unit_from == 'Meter' and unit_to == 'Centimeter':
        return length * 100
    elif unit_from == 'Centimeter' and unit_to == 'Meter':
        return length / 100
    return None  # Return None if conversion is not possible

def convert_weight(weight, unit_from, unit_to):
    if unit_from == 'Kilogram' and unit_to == 'Pound':
        return weight * 2.20462
    elif unit_from == 'Pound' and unit_to == 'Kilogram':
        return weight / 2.20462
    elif unit_from == 'Gram' and unit_to == 'Ounce':
        return weight * 0.035274
    elif unit_from == 'Ounce' and unit_to == 'Gram':
        return weight / 0.035274
    return None  # Return None if conversion is not possible

def convert_temperature(temp, unit_from, unit_to):
    if unit_from == 'Celsius' and unit_to == 'Fahrenheit':
        return (temp * 9/5) + 32
    elif unit_from == 'Fahrenheit' and unit_to == 'Celsius':
        return (temp - 32) * 5/9
    elif unit_from == 'Celsius' and unit_to == 'Kelvin':
        return temp + 273.15
    elif unit_from == 'Kelvin' and unit_to == 'Celsius':
        return temp - 273.15
    elif unit_from == 'Fahrenheit' and unit_to == 'Kelvin':
        return (temp - 32) * 5/9 + 273.15
    elif unit_from == 'Kelvin' and unit_to == 'Fahrenheit':
        return (temp - 273.15) * 9/5 + 32
    return None  # Return None if conversion is not possible

# Set page configuration for the app
st.set_page_config(page_title="Unit Converter", page_icon="💫", layout="wide")

# Apply custom styling for the dark theme with attractive button and card colors
st.markdown("""
    <style>
        /* General body styling */
        body {
            background-color: #121212 !important;
            color: white !important;
            font-family: 'Roboto', sans-serif !important;
        }

        /* Stylish button */
        .stButton>button {
            background: linear-gradient(145deg, #ff6a00, #ee0979) !important;
            color: white !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            padding: 14px 32px !important;
            border-radius: 50px !important;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3) !important;
            transition: all 0.3s ease !important;
            margin-top: 20px !important;
            cursor: pointer !important;
            border: none !important;
            outline: none !important;
            transform: scale(1) !important;
        }

        /* Hover effect for button */
        .stButton>button:hover {
            background: linear-gradient(145deg, #ff416c, #ff4b2b) !important;
            transform: scale(1.1) !important;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4) !important;
            transition: all 0.3s ease-in-out !important;
        }

        /* Focused state for button */
        .stButton>button:focus {
            box-shadow: 0 0 0 4px rgba(255, 105, 180, 0.6) !important;
        }

        /* Active state for button (slightly shrunk on click) */
        .stButton>button:active {
            background: linear-gradient(145deg, #ff6a00, #ee0979) !important;
            transform: scale(0.98) !important;
        }

        /* Stylish input fields */
        .stSelectbox, .stNumberInput, .stTextInput {
            background-color: #333333 !important;
            color: white !important;
            border: 2px solid #ff6a00 !important;
            border-radius: 10px !important;
            padding: 12px 15px !important;
            font-size: 16px !important;
        }

        /* Hover effect for input fields */
        .stSelectbox:hover, .stNumberInput:hover, .stTextInput:hover {
            border-color: #ee0979 !important;
        }

        /* Card background and styling */
        .stCard {
            background-color: #1f1f1f !important;
            border-radius: 20px !important;
            padding: 20px 30px !important;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3) !important;
        }

        /* Card content styling */
        .stCard h1, .stCard h2, .stCard h3 {
            color: #ff6a00 !important;
        }

        /* Header and subheader color */
        .stTitle, .stSubheader {
            color: #ff6a00 !important;
        }

        /* Improve spacing and alignment */
        .stTitle, .stSubheader, .stButton, .stCard {
            margin-bottom: 20px !important;
        }
    </style>
""", unsafe_allow_html=True)

# App Title and Header
st.title("📀⏳ Unit Converter 📀⏳")
st.subheader("🔄🎨 Choose a converter and input your values")

# Sidebar menu with buttons for selecting the conversion type
menu_option = st.sidebar.selectbox("Select Converter", ["Length", "Weight", "Temperature"])

# Show content based on sidebar selection
if menu_option == "Length":
    # Length Conversion Interface
    st.sidebar.subheader("Length Converter")
    with st.sidebar.expander("Length Details", expanded=True):
        length = st.number_input("Enter Length", min_value=0.0, step=0.1, format="%.2f")
        unit_from = st.selectbox("From Unit", ["Meter", "Centimeter"])
        unit_to = st.selectbox("To Unit", ["Meter", "Centimeter"])

    if st.sidebar.button("Convert Length"):
        result = convert_length(length, unit_from, unit_to)
        if result is not None:
            with st.expander("Conversion Results", expanded=True):
                st.markdown(f"### Results:")
                st.write(f"- Input Length: **{length} {unit_from}**")
                st.write(f"- Converted Length: **{result:.2f} {unit_to}**")
        else:
            st.error("Invalid unit combination for length conversion!")

elif menu_option == "Weight":
    # Weight Conversion Interface
    st.sidebar.subheader("Weight Converter")
    with st.sidebar.expander("Weight Details", expanded=True):
        weight = st.number_input("Enter Weight", min_value=0.0, step=0.1, format="%.2f")
        unit_from = st.selectbox("From Unit", ["Kilogram", "Pound", "Gram", "Ounce"])
        unit_to = st.selectbox("To Unit", ["Kilogram", "Pound", "Gram", "Ounce"])

    if st.sidebar.button("Convert Weight"):
        result = convert_weight(weight, unit_from, unit_to)
        if result is not None:
            with st.expander("Conversion Results", expanded=True):
                st.markdown(f"### Results:")
                st.write(f"- Input Weight: **{weight} {unit_from}**")
                st.write(f"- Converted Weight: **{result:.2f} {unit_to}**")
        else:
            st.error("Invalid unit combination for weight conversion!")

elif menu_option == "Temperature":
    # Temperature Conversion Interface
    st.sidebar.subheader("Temperature Converter")
    with st.sidebar.expander("Temperature Details", expanded=True):
        temp = st.number_input("Enter Temperature", min_value=-273.15, step=0.1, format="%.2f")  # Avoiding below absolute zero
        unit_from = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        unit_to = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

    if st.sidebar.button("Convert Temperature"):
        result = convert_temperature(temp, unit_from, unit_to)
        if result is not None:
            with st.expander("Conversion Results", expanded=True):
                st.markdown(f"### Results:")
                st.write(f"- Input Temperature: **{temp} {unit_from}**")
                st.write(f"- Converted Temperature: **{result:.2f} {unit_to}**")
        else:
            st.error("Invalid unit combination for temperature conversion!")
