
# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books.
#  Add a class method increment_book_count() to increase the count when a new book is added.

# Solution:

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"Total books:{cls.total_books}")
    def __init__(self):
        Book.increment_book_count()

book1 = Book()
book2 = Book()
book3 = Book()

      

