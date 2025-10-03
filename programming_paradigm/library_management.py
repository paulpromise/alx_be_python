class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and availability status."""
        self.title = title          # Public attribute
        self.author = author        # Public attribute
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False
    
    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book."""
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    """A class representing a library that manages books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Book '{book.title}' by {book.author} has been added to the library.")
        else:
            print("Error: Only Book instances can be added to the library.")
    
    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.is_available():
                    book.check_out()
                    print(f"You have checked out '{book.title}' by {book.author}.")
                    return True
                else:
                    print(f"Sorry, '{book.title}' is already checked out.")
                    return False
        print(f"Book titled '{title}' not found in the library.")
        return False
    
    def return_book(self, title):
        """Return a book by title if it's currently checked out."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if not book.is_available():
                    book.return_book()
                    print(f"Thank you for returning '{book.title}' by {book.author}.")
                    return True
                else:
                    print(f"'{book.title}' was not checked out.")
                    return False
        print(f"Book titled '{title}' not found in the library.")
        return False
    
    def list_available_books(self):
        """List all books that are currently available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- '{book.title}' by {book.author}")
        else:
            print("No books are currently available.")
        
        return available_books
    
    def list_all_books(self):
        """List all books in the library with their status."""
        if self._books:
            print("All books in the library:")
            for book in self._books:
                print(f"- {book}")
        else:
            print("The library has no books.")
    
    def get_book_count(self):
        """Get the total number of books in the library."""
        return len(self._books)