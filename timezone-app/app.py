import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import pytz
from PIL import Image

st.set_page_config(page_title="Time Zone App", page_icon="⏰", layout="centered")

# Custom CSS for styling
st.markdown(
    """
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
        /* Keyframes animation for the button */
        @keyframes pulse {  
            0% { box-shadow: 0 0 10px rgba(255, 87, 34, 0.7); }  
            50% { box-shadow: 0 0 20px rgba(255, 87, 34, 1); }  
            100% { box-shadow: 0 0 10px rgba(255, 87, 34, 0.7); }  
        }  
        /* Styling for the custom pulse button */
        .pulse-button {  
            display: block;  
            width: 100%;  
            text-align: center;  
            background: linear-gradient(45deg, #FF5722, #FFC107);  
            color: white;  
            font-size: 18px;  
            font-weight: bold;  
            padding: 12px;  
            margin: 10px 0;  
            border-radius: 8px;  
            text-decoration: none;  
            transition: all 0.3s ease-in-out;  
            animation: pulse 1.5s infinite;  
        }  

        /* Custom styling for streamlit's button */
.stButton > button {
    background: linear-gradient(45deg, #FF5722, #FFC107);
    width: 100%;
    text-align: center;
    display: block;
    color: white;
    font-size: 18px;
    font-weight: bold;
    padding: 12px;
    margin: 10px 0;
    border-radius: 8px;
    border: none;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease-in-out;
}

/* Animation for the moving border */
.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 3px solid #FFC107;
    border-radius: 50%;
    transition: all 0.3s ease-in-out;
    transform: scale(0);
    animation: animateBorder 2s linear infinite;
}

/* Animation for the circle border */
@keyframes animateBorder {
    0% {
        transform: scale(0);
    }
    50% {
        transform: scale(1.2);
    }
    100% {
        transform: scale(0);
    }
}

/* Hover effect to highlight the button */
.stButton > button:hover {
    color: white;
    font: bold;
    padding: 12px;
    margin: 10px 0;
    border-radius: 8px;
    transition: all 0.3s ease-in-out;
    background: linear-gradient(45deg, #FFC107, #FF5722);
}

/* On hover, start the circle animation */
.stButton > button:hover::before {
    transform: scale(1);
    animation: animateBorder 2s linear infinite;
}
    </style>
    """, 
    unsafe_allow_html=True
)

# --- Data ---
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Africa/Lagos",
    "Asia/Kolkata",
    "Asia/Tokyo",
]

# --- Main App ---
st.title("🕛🕰️ Time Zone App ⏰")

selected_timezones = st.multiselect(
    "Select Time Zones", TIME_ZONES, default=["UTC", "Africa/Lagos"]
)

st.subheader("Selected Time Zones")

# Show current time for each selected time zone
for tz in selected_timezones:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

# --- Convert Time Between Time Zones ---
st.subheader("Convert Time Between Time Zones")

now_time = datetime.now().time()
current_time = st.time_input("Current Time", value=now_time)

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"Converted Time in {to_tz}: {converted_time}")
    st.snow()
    

    
