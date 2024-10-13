class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size        # Initialize the file size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count      # Initialize the page count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list to store books

    def add_book(self, book):
        self.books.append(book)  # Add a book to the library

    def list_books(self):
        for book in self.books:
            print(book)  # Print each book's details