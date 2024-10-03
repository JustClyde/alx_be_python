class Book:
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if self._is_checked_out:
            return False  # Book is already checked out
        self._is_checked_out = True
        return True  # Successfully checked out

    def return_book(self):
        if not self._is_checked_out:
            return False  # Book was not checked out
        self._is_checked_out = False
        return True  # Successfully returned

    def is_available(self):
        return not self._is_checked_out  # Return availability status


class Library:
    def __init__(self):
        self._books = []  # Private list to store instances of Book

    def add_book(self, book):
        self._books.append(book)  # Add book to the library collection

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()  # Invoke the check_out method of the book
        return False  # Book not found

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()  # Invoke the return_book method of the book
        return False  # Book not found

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")  # Print details of available books
