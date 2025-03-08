import streamlit as st  
import pandas as pd  
import os  
from io import BytesIO  

# App setup  
st.set_page_config(page_title="Growth Mindset Challenge",page_icon="🎨🌱" layout='wide')  

# Sidebar setup  
st.sidebar.title("Mussarat Shamsher")  
resume_link = "https://milestone1-personal-static-resume.vercel.app/"  

# Gradient Pulse Button CSS  
button_style = """  
    <style>  
        @keyframes pulse {  
            0% { box-shadow: 0 0 10px rgba(255, 87, 34, 0.7); }  
            50% { box-shadow: 0 0 20px rgba(255, 87, 34, 1); }  
            100% { box-shadow: 0 0 10px rgba(255, 87, 34, 0.7); }  
        }  
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
    </style>  
"""  
# Inject CSS into the app  
st.sidebar.markdown(button_style, unsafe_allow_html=True)  

# Create the pulse effect button  
st.sidebar.markdown(f'<a href="{resume_link}" target="_blank" class="pulse-button">📝 View Resume</a>', unsafe_allow_html=True)  

# Sidebar Projects Section  
st.sidebar.title("Projects")  

# Define project links  
projects = {  
    "🛏 Furniro": "https://functional-hackthon-jet.vercel.app/",  
    "🥧 FoodTuck": "https://ui-ux-hackthon-lac.vercel.app/",  
    "🏨 Restaurant": "https://resturant-flavourfusion.vercel.app/",  
    "💺 Hire Developers": "https://hiredevelopers-hiredev.vercel.app/"  
}  

# Display buttons for each project  
for name, link in projects.items():  
    if st.sidebar.button(name):  
        st.sidebar.markdown(f'<meta http-equiv="refresh" content="0;URL={link}">', unsafe_allow_html=True)  

# Main content  
st.title("🌱🌾Growth Mindset Challenge")  
st.write("🛠Transform your files between CSV & Excel formats with built-in data cleaning & visualization!")  

# File uploader  
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)  

# Store processed dataframes  
dataframes = []  

if uploaded_files:  
    for file in uploaded_files:  
        file_ext = os.path.splitext(file.name)[-1].lower()  


        if file_ext == ".csv":  
            df = pd.read_csv(file)  
        if file_ext == ".xlsx":
            df = pd.read_excel(file, engine='openpyxl')
 
        else:  
            st.error(f"Unsupported file type: {file_ext}")  
            continue  

        # Display file info  
        st.write(f"**File Name:** {file.name}")  
        st.write(f"**File Size:** {len(file.getbuffer()) / 1024:.2f} KB")  

        # Show first 5 rows of the dataframe  
        st.write("Preview of the DataFrame:")  
        st.dataframe(df.head())  

        # Data Cleaning Options  
        st.subheader(f"Data Cleaning Options for {file.name}")  

        if st.checkbox(f"Clean Data for {file.name}"):  
            col1, col2 = st.columns(2)  

            with col1:  
                if st.button(f"Remove Duplicates from {file.name}"):  
                    df.drop_duplicates(inplace=True)  
                    st.write("Duplicates Removed!")  

            with col2:  
                if st.button(f"Fill Missing Values for {file.name}"):  
                    numeric_cols = df.select_dtypes(include=['number']).columns  
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())  
                    st.write("Missing Values have been Filled!")  

        # Choose Specific Columns to Keep  
        st.subheader(f"Select Columns to Keep for {file.name}")  
        columns = st.multiselect(f"Choose Columns for {file.name}", list(df.columns), default=list(df.columns))  
        df = df[columns]  
        st.dataframe(df)  

        # Add processed dataframe to the list  
        dataframes.append((file.name, df))  

# Visualization  
if dataframes:  
    last_file_name, last_df = dataframes[-1]  # Get the last processed dataframe  
    st.subheader(f"📊 Data Visualization for {last_file_name}")  
    if st.checkbox(f"Show Visualization for {last_file_name}"):  
        numeric_cols = last_df.select_dtypes(include='number').columns  # Get numeric columns  

        if len(numeric_cols) >= 2:  # Ensure at least two numeric columns exist  
            st.bar_chart(last_df[numeric_cols].iloc[:, :2])  
        else:  
            st.warning("Not enough numerical columns for visualization!")  

    # Convert the file -> CSV to Excel  
    st.subheader(f"Conversion Options for {last_file_name}")  
    conversion_type = st.radio(f"Convert {last_file_name} to:", ["CSV", "Excel"], key=last_file_name)  

    if st.button(f"Convert {last_file_name}"):  
        buffer = BytesIO()  

        if conversion_type == "CSV":  
            last_df.to_csv(buffer, index=False)  
            file_name = last_file_name.replace(os.path.splitext(last_file_name)[-1], ".csv")  
            mime_type = "text/csv"  

        elif conversion_type == "Excel":  
            last_df.to_excel(buffer, index=False)  
            file_name = last_file_name.replace(os.path.splitext(last_file_name)[-1], ".xlsx")  
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  

        buffer.seek(0)  # Reset buffer position  

        # Download button  
        st.download_button(  
            label=f"🔽 Download {file_name} as {conversion_type}",  
            data=buffer,  
            file_name=file_name,  
            mime=mime_type  
        )  

        # Success message after processing  
        st.success("✔ All files processed!")