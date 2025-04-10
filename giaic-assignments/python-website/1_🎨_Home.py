import streamlit as st
import streamlit.components.v1 as components
import time

# Set page configuration 
st.set_page_config(
    page_title="Mussarat Shamsher", page_icon="🪐", layout="wide")

# Add custom CSS for background image
st.markdown(
    """
    <style>               
       .stApp{
            margin:0;
            padding-top:0; 
            background: black;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: white;
            font-family: 'Arial', sans-serif;}
        .stSidebar{
            background: black;
            border-radius: 20px;
            box-shadow: 0 4px 5px white;
            color: white;
            margin-top: 58px;}  
            /* Basic Button Style */
         @keyframes pulse {  
            0% { box-shadow: 0 0 10px rgba(255, 87, 34, 0.7); }  
            50% { box-shadow: 0 0 20px rgba(255, 87, 34, 1); }  
            100% { box-shadow: 0 0 10px rgba(255, 87, 34, 0.7); }  
        }  
        .sidebar-button {  
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
        .stWrite{
         width: 90%;
         margin: 5px auto;
         padding: 10px;
         overflow: hidden;}
    </style>
    """, unsafe_allow_html=True
)

#Sidebar content
st.sidebar.title("Mussarat Shamsher")

# --- Button Links ---
portfolio_link = "https://portfolio-mussarat-shamsher.vercel.app/"
resume_link = "https://milestone1-personal-static-resume.vercel.app/"

# --- Buttons using Markdown ---
st.sidebar.markdown(
    f'<a href="{portfolio_link}" target="_blank" class="sidebar-button">📄 View Portfolio</a>',
    unsafe_allow_html=True
)
st.sidebar.markdown(
    f'<a href="{resume_link}" target="_blank" class="sidebar-button">📝 View Resume</a>',
    unsafe_allow_html=True
)

# main content
st.subheader("Personal Website")

st.write("Welcome to my website! I am a passionate web developer. I love creating beautiful & functional web applications.Explore my work here.")

components.html("""
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <title>Swiper demo</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1" />
  <!-- Link Swiper's CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />

  <!-- Demo styles -->
  <style>
    html,
    body {
      position: relative;
      height: 100%;
    }
    body {
      background: black;
      font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
      font-size: 14px;
      color: #000;
      margin: 0;
      padding: 0;
    }
    body {
      background: black;
      font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
      font-size: 14px;
      color: red;
      margin: 0;
      padding: 0;
    }
    html,
    body {
      position: relative;
      height: 100%;
    }
    body {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .swiper {
      width: 400px;
     height: 350px;
      overflow: hidden;
    }
     @media (max-width: 600px){ 
      .swiper {
      max-width: 200px;
      margin: 0 auto;
      overflow: hidden;         
      } }         
    .swiper-slide {
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 18px;
      font-size: 22px;
      font-weight: bold;
      color: #fff;
      border-radius: 20px;
      box-shadow: 0 0 10px white,
        0 0 20px white,
        0 0 30px white;
    }
    .swiper-slide:nth-child(1n) {
       background: url("https://images.unsplash.com/photo-1738045599472-6d931c3daccf?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D") no-repeat center center;
    }
    .swiper-slide:nth-child(2n) {
     background: url("https://images.unsplash.com/photo-1625670413987-0ae649494c61?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8UXVlc3Rpb24lMjBzeW1ib2x8ZW58MHx8MHx8fDA%3D");
    }
    .swiper-slide:nth-child(3n) {
      background: url("https://plus.unsplash.com/premium_photo-1674217929972-7289cec76f27?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8MzAweCUyMDMwMCUyMCUyMGNsb2NrfGVufDB8fDB8fHww");
    }
    .swiper-slide:nth-child(4n) {
       background: url("https://media.istockphoto.com/id/1908249816/photo/hanging-questions.webp?a=1&b=1&s=612x612&w=0&k=20&c=i4CPowz69gYcW1Ji5_WigG1boq6pH5u2iYzXwdrPEG0=");
    }
    .swiper-slide:nth-child(5n) {
      background: url("https://plus.unsplash.com/premium_photo-1675329253568-447ff9cc04a3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fHBhc3N3b3JkfGVufDB8fDB8fHww");
    }
    .swiper-slide:nth-child(6n) {
      background: url("https://images.unsplash.com/photo-1743105351262-3f9e6944920a?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8ZnVubnklMjBlbW98ZW58MHx8MHx8fDA%3D");
    }
    .swiper-slide:nth-child(7n) {
      background: url("https://plus.unsplash.com/premium_photo-1679456904325-19ca215974a7?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fG1vbmV5fGVufDB8fDB8fHww");
    }
    .swiper-slide:nth-child(8n) {
      background: url("https://images.unsplash.com/photo-1571901020303-b93a0b0ae8d5?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fG1lcmN1cnklMjBtZXRlcnxlbnwwfHwwfHx8MA%3D%3D");
    }
    .swiper-slide:nth-child(9n) {
      background: url("https://plus.unsplash.com/premium_photo-1718169446625-37680c0a3a0a?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bnVtYmVyc3xlbnwwfHwwfHx8MA%3D%3D");
    }
    .swiper-slide:nth-child(10n) {
      background: url("https://plus.unsplash.com/premium_photo-1738677617432-e3bfaad291c1?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bW9vZCUyMGFuYWx5emVyfGVufDB8fDB8fHww");
    }
    .swiper-slide:nth-child(11n) { 
    background: url("https://images.unsplash.com/photo-1494059980473-813e73ee784b?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cHV6emxlfGVufDB8fDB8fHww");
    }
    .swiper-slide:nth-child(12n) {
    background: url("https://plus.unsplash.com/premium_photo-1682339496371-d71e65e3e42d?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cXIlMjBjb2RlfGVufDB8fDB8fHww");
    }
    .swiper-slide:nth-child(13n) {
    background: url("https://plus.unsplash.com/premium_photo-1681487746049-c39357159f69?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cGFzc3dvcmR8ZW58MHx8MHx8fDA%3D");
    }
    .swiper-slide:nth-child(14n) {
    background: url("https://plus.unsplash.com/premium_photo-1679941208761-9c3835f4534b?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    } 
  </style>
</head>

<body>
  <!-- Swiper -->

  <div class="swiper mySwiper">
    <div class="swiper-wrapper">
   
<div class="swiper-slide 1"> <a href="https://my-personal-library-management.streamlit.app/", target="_blank">
  Library Management App</a></div>      
<div class="swiper-slide 2"><a href="https://pythonassignments-challenge.streamlit.app/", target="_blank">
 Growth Mindset Challange</a></div> 
<div class="swiper-slide 3"><a href="https://python-assignments-timezone.streamlit.app/", target="_blank">
 TimeZone App</a></div>
<div class="swiper-slide 4"><a href="https://pythonchallange-quiz-app.streamlit.app/", target="_blank">
Quiz App</a></div>
 <div class="swiper-slide 5"><a href="https://pythonassignments-password-generator.streamlit.app/", target="_blank">
 Password Generator</a></div>
 <div class="swiper-slide 6"><a href="https://joke-generator-by-musssarat.streamlit.app/", target="_blank">
 Joke Generator</a></div>
 <div class="swiper-slide 7"><a href="https://pythonassignments-money-making-machine.streamlit.app/", target="_blank">
Money Making Machine</a></div>
<div class="swiper-slide 8"><a href="https://pythonassignments-converter.streamlit.app/", target="_blank">
 Unit Convertor</a></div>
 <div class="swiper-slide 9"><a href="https://number-guess-game.streamlit.app/", target="_blank">
Guess Number</a></div>
<div class="swiper-slide 10"><a href="https://pythonchallange-mood-analyzer.streamlit.app/", target="_blank">
Mood Analyzer</a></div>
<div class="swiper-slide 11"><a href="https://pythonchallange-mystery-adventure.streamlit.app/", target="_blank">
Mystery Adventure</a></div>
<div class="swiper-slide 12"><a href="https://mussarat-qr-code-generator.streamlit.app/", target="_blank">
QR Code Generator</a></div>
<div class="swiper-slide 13"><a href="https://pythonassignments-guess-the-number.streamlit.app/", target="_blank">
Password Strength Meter</a></div>  
<div class="swiper-slide 14"><a href="https://pythonassignments-guess-the-number.streamlit.app/", target="_blank">  
Anagram Checker</a></div>    
    </div>
  </div>

  <!-- Swiper JS -->
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

  <!-- Initialize Swiper -->
  <script>
    var swiper = new Swiper(".mySwiper", {
      effect: "cards",
      grabCursor: true,
      autoplay: {
        delay: 1000,
        disableOnInteraction: false,
        hoverpause: true,
      },
    });
  </script>
</body>
</html>

""",  height=400, scrolling=True)
