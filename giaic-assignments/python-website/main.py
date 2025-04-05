import streamlit as st
import streamlit.components.v1 as components

# Create the navbar HTML and CSS code with Hamburger Menu
navbar_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Navbar</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: black;
        }
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent background */
            padding: 10px 20px;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 10;
        }
        .navbar .title {
            color: white;
            font-size: 24px;
            font-weight: bold;
        }
        .hamburger {
            display: none;
            flex-direction: column;
            justify-content: space-between;
            height: 24px;
            width: 30px;
            cursor: pointer;
        }
        .hamburger div {
            background-color: white;
            height: 4px;
            width: 100%;
        }
        @media (max-width: 768px) {
            .navbar .title {
                font-size: 18px;
            }
            .hamburger {
                display: flex;
            }
            .menu {
                display: none;
                position: absolute;
                top: 60px;
                left: 0;
                width: 100%;
                background-color: rgba(0, 0, 0, 0.9);
                padding: 10px;
                text-align: center;
            }
            .menu a {
                color: white;
                text-decoration: none;
                padding: 10px;
                display: block;
            }
            .menu a:hover {
                background-color: #575757;
            }
            .navbar.open .menu {
                display: block;
            }
        }
    </style>
    <!-- Swiper.js CDN -->
    <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css" />
    <script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>
</head>
<body>
    <div class="navbar">
        <div class="title">Mussarat Shamsher</div>
        <div class="hamburger" onclick="toggleMenu()">
            <div></div>
            <div></div>
            <div></div>
        </div>
        <div class="menu">
            <a href="javascript:void(0)" onclick="showPage('home')">Home</a>
            <a href="javascript:void(0)" onclick="showPage('about')">About</a>
            <a href="javascript:void(0)" onclick="showPage('contact')">Contact</a>
        </div>
    </div>
    <script>
        function toggleMenu() {
            const navbar = document.querySelector('.navbar');
            navbar.classList.toggle('open');
        }
        function showPage(page) {
            // This function will trigger the page content change in Streamlit
            window.parent.postMessage({type: 'change_page', page: page}, '*');
        }

        // Initialize Swiper
        var swiper = new Swiper('.swiper-container', {
            loop: true,
            spaceBetween: 10,
            autoplay: {
                delay: 3000,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });
    </script>
</body>
</html>
"""

# Rendering the HTML navbar using Streamlit components
components.html(navbar_html, height=120)

# Swiper Slider HTML and CSS
swiper_html = """
<style>
    .swiper-container {
        width: 100%;
        height: 400px;
    }
    .swiper-slide img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .swiper-button-next, .swiper-button-prev {
        color: white;
    }
</style>

<div class="swiper-container">
    <div class="swiper-wrapper">
        <div class="swiper-slide"><img src="https://via.placeholder.com/800x400?text=Project+1" alt="Project 1"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/800x400?text=Project+2" alt="Project 2"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/800x400?text=Project+3" alt="Project 3"></div>
        <div class="swiper-slide"><img src="https://via.placeholder.com/800x400?text=Project+4" alt="Project 4"></div>
    </div>
    <!-- Pagination and Navigation buttons -->
    <div class="swiper-pagination"></div>
    <div class="swiper-button-next"></div>
    <div class="swiper-button-prev"></div>
</div>
"""

# Streamlit content for the pages
def home_page():
    st.title("Home")
    st.write("Welcome to the Home Page!")
    
    # Display the Swiper.js slider
    components.html(swiper_html, height=450)

def about_page():
    st.title("About")
    st.write("This is the About page. You can include information about yourself or your company here.")

def contact_page():
    st.title("Contact")
    st.write("This is the Contact page. Provide contact details here.")

# Page routing based on messages from JavaScript (via postMessage)
def main():
    # Placeholder for page navigation
    page = "home"  # Default to home page

    # Listen for messages to change page (message type 'change_page')
    if 'type' in st.session_state:
        if st.session_state['type'] == 'change_page':
            page = st.session_state['page']

    # Show the relevant content based on the page selected
    if page == "home":
        home_page()
    elif page == "about":
        about_page()
    elif page == "contact":
        contact_page()

# Run the app
if __name__ == "__main__":
    main()
