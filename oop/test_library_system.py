#!/usr/bin/env python3

from library_system import Book, EBook, PrintBook, Library


def main():
    """Test function to demonstrate the library system functionality."""
    
    # Create a library instance
    library = Library()
    
    # Create different types of books
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    ebook = EBook("The Digital Fortress", "Dan Brown", 2048)
    print_book = PrintBook("The Great Gatsby", "F. Scott Fitzgerald", 180)
    
    # Add books to the library
    library.add_book(classic_book)
    library.add_book(ebook)
    library.add_book(print_book)
    
    # List all books in the library
    print("Library Collection:")
    print("-" * 40)
    library.list_books()


if __name__ == "__main__":
    main()