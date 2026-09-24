class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, isbn):
        """
        Initialize a new book.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """Return the book information in a readable format."""
        return (
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"ISBN: {self.isbn}"
        )

    def get_details(self):
        """Return the book details as a dictionary."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
        }