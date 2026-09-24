from book import Book


def add_book(library):
    """
    Ask the user for book information and add the book to the library.

    Args:
        library (list): The list that stores Book objects.

    Returns:
        None
    """
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    isbn = input("Enter the ISBN: ").strip()

    new_book = Book(title, author, isbn)
    library.append(new_book)

    print("Book added successfully!")


def list_books(library):
    """
    Display every book currently stored in the library.

    Args:
        library (list): The list that stores Book objects.

    Returns:
        None
    """
    if not library:
        print("The library is empty.")
        return

    print("\nBooks in the library:")
    for book in library:
        print(book)


def find_book(library, query):
    """
    Search for a book by its title or author.

    Args:
        library (list): The list that stores Book objects.
        query (str): The title or author to search for.

    Returns:
        Book or None: The matching Book object, or None if no match is found.
    """
    search_text = query.strip().lower()

    for book in library:
        if (
            book.title.lower() == search_text
            or book.author.lower() == search_text
        ):
            return book

    return None


def main():
    """Run the main menu for the library management program."""
    my_library = []

    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Find a book")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_book(my_library)

        elif choice == "2":
            list_books(my_library)

        elif choice == "3":
            query = input("Enter a book title or author: ")
            found_book = find_book(my_library, query)

            if found_book:
                print("Book found:")
                print(found_book)
            else:
                print("Book not found.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()