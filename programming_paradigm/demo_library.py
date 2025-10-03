
from library_management import Book, Library


def main():
    """Demonstrate the library management system."""
    print("=== Library Management System Demo ===\n")
    
    # Create a library instance
    library = Library()
    
    # Create some books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book4 = Book("Pride and Prejudice", "Jane Austen")
    
    print("1. Adding books to the library:")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    print(f"\nTotal books in library: {library.get_book_count()}\n")
    
    print("2. Listing all available books:")
    library.list_available_books()
    print()
    
    print("3. Checking out books:")
    library.check_out_book("1984")
    library.check_out_book("The Great Gatsby")
    print()
    
    print("4. Listing available books after checkout:")
    library.list_available_books()
    print()
    
    print("5. Trying to check out an already checked-out book:")
    library.check_out_book("1984")
    print()
    
    print("6. Returning a book:")
    library.return_book("1984")
    print()
    
    print("7. Final status of all books:")
    library.list_all_books()
    print()
    
    print("8. Trying to return a book that wasn't checked out:")
    library.return_book("Pride and Prejudice")
    print()
    
    print("9. Trying to check out a non-existent book:")
    library.check_out_book("Nonexistent Book")


if __name__ == "__main__":
    main()