import streamlit as st
import json

st.set_page_config(page_icon="📚", page_title=" Book Collection Manager 📚", layout="wide")

# BookCollection Class
class BookCollection:
    """A class to manage books"""
    def __init__(self):
        """Initialize the book collection"""
        self.books_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Read books from a file"""
        try:
            with open(self.storage_file, "r") as file:
                self.books_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books_list = []

    def save_to_file(self):
        """Save books to a file"""
        with open(self.storage_file, "w") as file:
            json.dump(self.books_list, file, indent=4)

    def create_new_book(self, title, author, year, genere, read):
        """Add a new book to the collection"""
        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "genere": genere,
            "read": read
        }
        self.books_list.append(new_book)
        self.save_to_file()

    def delete_book(self, title):
        """Remove a book from the collection"""
        for book in self.books_list:
            if book["title"].lower() == title.lower():
                self.books_list.remove(book)
                self.save_to_file()
                return True
        return False

    def find_book(self, search_type, search_text):
        """Find a book in the collection"""
        found_books = []
        if search_type == "Title":
            found_books = [book for book in self.books_list if search_text.lower() in book["title"].lower()]
        elif search_type == "Author":
            found_books = [book for book in self.books_list if search_text.lower() in book["author"].lower()]
        return found_books

    def update_book(self, title, new_title, new_author, new_year, new_genere, new_read):
        """Update book details"""
        for book in self.books_list:
            if book["title"].lower() == title.lower():
                book["title"] = new_title if new_title else book["title"]
                book["author"] = new_author if new_author else book["author"]
                book["year"] = new_year if new_year else book["year"]
                book["genere"] = new_genere if new_genere else book["genere"]
                book["read"] = new_read
                self.save_to_file()
                return True
        return False

    def show_all_books(self):
        """Return all books in the collection"""
        return self.books_list

# Adding CSS for background, title, and button styling
st.markdown(
    """
    <style>
        /* Dynamic Gradient Background with Beautiful Colors */
        .stApp {
            background: linear-gradient(135deg, #FFB6C1, #87CEEB); /* Peach to Light Sky Blue */
            background-size: 400% 400%;  /* Make sure the gradient fills the entire page */
            animation: gradientAnimation 20s ease infinite; /* Smooth transition every 20 seconds */
            height: 100vh;
            font-family: 'Arial', sans-serif;
        }
        /* Animation for Dynamic Gradient Background */
        @keyframes gradientAnimation {
            0% {
                background: linear-gradient(135deg, #FFB6C1, #87CEEB); 
            }
            25% {
                background: linear-gradient(135deg, #fc765f,  #f8f8f7);
            }
            50% {
                background: linear-gradient(135deg, #8af3f1, #f5b470);
            }
            75% {
                background: linear-gradient(135deg, #92e092, #9ba9ed); 
            }
            100% {
                background: linear-gradient(135deg, #FFB6C1, #d29cfa); 
            }
        }
        /* Title Animation (Bounce Effect) */
        @keyframes bounce {
            0% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0); }
        }
        .title {
            animation: bounce 1s infinite;
            font-size: 3rem;
            color: #ffffff;
            font-weight: bold;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.4);
        }
        /* Stylish Buttons */
          .css-1emrehy.edgvbvh3, .stButton>button {
            background-color: #FF6347 !important; /* Coral Red */
            background-image: linear-gradient(to right, #FF6347, #FFD700) !important; /* Gradient from Coral Red to Golden Yellow */
            width: 50%;
            color: white !important;
            border-radius: 12px !important;
            font-weight: bold !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: background 0.3s ease !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
        }
        /* Button Hover Effect */
        .css-1emrehy.edgvbvh3:hover, .stButton>button:hover {
            background-color: #FFD700 !important; /* Golden Yellow */
            background-image: linear-gradient(to right, #FFD700, #FF6347) !important; /* Reversed Gradient */
            cursor: pointer !important;
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2) !important;
        }
        st.sidebar{
        background: black !important;
        color: white;
        }
    </style>
    """, unsafe_allow_html=True)

# Animated title
st.markdown('<div class="title">📚 Book Collection Manager 📚</div>', unsafe_allow_html=True)

# Initialize BookCollection class
book_collection = BookCollection()

# Sidebar Menu
with st.sidebar:
    st.title("Menu")
    option = st.selectbox(
        "Choose an option:",
        ["Add a New Book", "Delete a Book", "Find a Book", "Update Book", "Show All Books", "Show Reading Progress"]
    )

# Main content
st.subheader(option)

if option == "Add a New Book":
    st.write("### Add New Book Details:")
    book_title = st.text_input("Enter the Book Title:")
    book_author = st.text_input("Enter the Author Name:")
    publication_year = st.text_input("Enter the Publication Year:")
    book_genere = st.text_input("Enter the Book Genre:")
    is_book_read = st.radio("Have you read this book?", ["Yes", "No"])
    is_book_read = True if is_book_read == "Yes" else False

    if st.button("Add Book"):
        book_collection.create_new_book(book_title, book_author, publication_year, book_genere, is_book_read)
        st.success("Book added successfully!")

elif option == "Delete a Book":
    book_title_to_delete = st.text_input("Enter the Title of the Book to Delete:")
    if st.button("Delete Book"):
        if book_collection.delete_book(book_title_to_delete):
            st.success("Book deleted successfully!")
        else:
            st.error("Book not found!")

elif option == "Find a Book":
    search_type = st.selectbox("Search by:", ["Title", "Author"])
    search_term = st.text_input("Enter the search term:")
    if st.button("Find Book"):
        found_books = book_collection.find_book(search_type, search_term)
        if found_books:
            for book in found_books:
                st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genere']} - {'Read' if book['read'] else 'Not Read'}")
        else:
            st.error("No matching books found!")

elif option == "Update Book":
    book_title_to_update = st.text_input("Enter the Title of the Book to Update:")
    new_title = st.text_input("New Title (leave blank to keep existing):")
    new_author = st.text_input("New Author (leave blank to keep existing):")
    new_year = st.text_input("New Publication Year (leave blank to keep existing):")
    new_genere = st.text_input("New Genre (leave blank to keep existing):")
    new_read = st.radio("Have you read this book?", ["Yes", "No"])
    new_read = True if new_read == "Yes" else False

    if st.button("Update Book"):
        if book_collection.update_book(book_title_to_update, new_title, new_author, new_year, new_genere, new_read):
            st.success("Book updated successfully!")
        else:
            st.error("Book not found!")

elif option == "Show All Books":
    all_books = book_collection.show_all_books()
    if all_books:
        for book in all_books:
            st.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genere']} - {'Read' if book['read'] else 'Not Read'}")
    else:
        st.write("No books in the collection.")

elif option == "Show Reading Progress":
    total_books = len(book_collection.books_list)
    completed_books = sum(1 for book in book_collection.books_list if book["read"])
    progress = (completed_books / total_books * 100) if total_books > 0 else 0
    st.write(f"Total Books: {total_books}")
    st.write(f"Reading Progress: {progress:.2f}%")

# Add Footer
st.markdown("---")
st.write("Created with ❤️ using Streamlit")
