class Book:
    """A class to represent a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Return a human-readable string representation of the book.

        Returns:
            str: A string in the format "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Return an official string representation that could recreate the Book instance.

        Returns:
            str: A string in the format "Book('title', 'author', year)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
