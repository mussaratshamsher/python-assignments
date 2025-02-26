import streamlit as st

# Function to convert the input length into meters and centimeters
def convert_length(length, unit):
    if unit == 'Meter':
        meters = length
        centimeters = length * 100
    elif unit == 'Centimeter':
        meters = length / 100
        centimeters = length
    return meters, centimeters

# App layout
st.set_page_config(page_title="Length Converter", page_icon="🌍", layout="centered")

# Dark Background with professional look
st.markdown("""
    <style>
        body {
            background-color: black !important;
            color: white !important;
            font-family: 'Roboto', sans-serif !important;
            border: 1px solid #333 !important;
            border-radius: 8px !important;
        }
        .stTextInput, .stNumberInput, .stSelectbox, .stButton>button {
            background-color: #6200ea !important;
            color: white !important;
            border-radius: 8px !important;
            border: 1px solid #333 !important;
            font-size: 16px !important;
        }
        .stButton>button {
            background-color: #6200ea !important;
            color: white !important;
            font-size: 18px !important;
            font-weight: bold !important;
            padding: 10px 20px !important;
            border-radius: 10px !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2) !important;
            transition: all 0.3s ease !important;
        }
        .stButton>button:hover {
            background-color: #3700b3 !important;
            transform: scale(1.05) !important;
        }
        .stContainer {
            margin-bottom: 50px !important;           
        }
        .stCard {
            background-color: #1a1a1a !important;
            border-radius: 15px !important;
            padding: 20px !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
        }
        .stTitle, .stSubheader {
            color: #bb86fc !important;
        }
        .stMarkdown {
            color: #bb86fc !important;
        }
        .stWrite {
            color: #a5b3d1 !important;
        }
    </style>
""", unsafe_allow_html=True)

# App header
st.title("Length Converter")
st.subheader("Convert between meters and centimeters")

# Input form within a styled container
with st.container():
    # Create an expander for input fields
    with st.expander("Enter Length Details", expanded=True):
        # Create two columns for the inputs (input fields)
        col1, col2 = st.columns([1, 1])

        # Input in the first column
        with col1:
            length = st.number_input("Enter Length", min_value=0.0, step=0.1)
        
        # Unit selector in the second column
        with col2:
            unit = st.selectbox("Select Unit", ["Meter", "Centimeter"])

# Display the Convert button at the bottom center
st.markdown('<div style="display: flex; justify-content: center; margin-top: 30px;">', unsafe_allow_html=True)
convert_button = st.button("Convert", key="convert_button")
st.markdown('</div>', unsafe_allow_html=True)

# If button is pressed, perform conversion
if convert_button:
    meters, centimeters = convert_length(length, unit)
    
    # Display results inside a card-like box
    with st.expander("Conversion Results", expanded=True):
        st.markdown(f"### Results:")
        st.write(f"- Length in meters: **{meters:.2f} m**")
        st.write(f"- Length in centimeters: **{centimeters:.2f} cm**")
