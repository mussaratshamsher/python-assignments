import json

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

    def create_new_book(self):
        """"Add a new to the collection"""
        book_title = input("Enter the book title: ")
        book_author = input("Enter the book author: ")
        publication_year = input("Enter the publication year: ")
        book_genere = input("Enter the book genere: ")
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes")

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genere": book_genere,
            "read": is_book_read
        }
        self.books_list.append(new_book)
        self.save_to_file()
        print("Book added successfully! \n")

    def delete_book(self):
        """Remove a book from the collection❗"""
        book_title = input("Enter the title of the book to delete: ")
        for book in self.books_list:
            if book["title"].lower() == book_title.lower():
                self.books_list.remove(book)
                self.save_to_file()
                print("Book deleted successfully❗ \n")
                return
        print("Book not found❗ \n")

    def find_book(self):
        """Find a book in the collection"""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice (1 or 2): ")
        search_text = input("Enter search term: ").lower()
        found_books = []
        if search_type == "1":
            found_books = [book for book in self.books_list if search_text in book["title"].lower()]
        elif search_type == "2":
            found_books = [book for book in self.books_list if search_text in book["author"].lower()]
        else:
            print("Invalid search type.")
            return

        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Not Read"
                print(f"{index}. {book['title']} by {book['author']} - {reading_status}")
        else:
            print("No matching books found.")

    def update_book(self):
        """Modify the details of an existing book in the collection"""
        book_title = input("Enter the title of the book to update: ")
        for book in self.books_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                new_title = input(f"New title ({book['title']}): ")
                book["title"] = new_title if new_title else book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]   
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genere"] = input(f"New genere ({book['genere']}): ") or book["genere"]
                book["read"] = (
                    input("Have you read this book? (yes/no): ").strip().lower() == "yes")
                self.save_to_file()
                print("Book updated successfully! \n")
                return
        print("Book not found! \n")
  
    def show_all_books(self):
        """Display all books in the collection with details"""
        if not self.books_list:
            print("No books in the collection.")
            return
        print("All Books Collection:")
        for index, book in enumerate(self.books_list, 1):
            reading_status = "Read" if book["read"] else "unread"
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genere']} - {reading_status}"
                )        
        print()

    def show_reading_progress(self):
        """Calcualtion and display statistics abut your reading progress."""
        total_books = len(self.books_list)
        completed_books = sum(1 for book in self.books_list if book["read"])
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0    
        )
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")

    def start_application(self):
        """Run the main applicaiton loop with a user-friendly menu interface.""" 
        while True:
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Delete a book")
            print("3. Find a book")
            print("4. Update book details")
            print("5. Show all books")
            print("6. Show reading progress")
            print("7. Exit")
            user_choice = input("Please choose option: (1-7) ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                print("Thank you for using Book Collection Manager. Goodbye❗")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    book_collection = BookCollection()
    book_collection.start_application()
