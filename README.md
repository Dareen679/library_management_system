# Library Management System

## Project Overview

This project is a simple Python library management system. It allows a user to add books, list all books, search for a book by title or author, and exit the program.

The project uses functions, modules, and object-oriented programming to keep the code organized and easy to understand.

## Files

### book.py

This file contains the `Book` class.

Each book stores:
- Title
- Author
- ISBN

The class also includes:
- `__str__()` to display book information in a readable format
- `get_details()` to return the book information as a dictionary

### library_manager.py

This is the main program file.

It imports the `Book` class from `book.py` and includes functions for:
- Adding a book
- Listing all books
- Finding a book
- Running the main menu

## How to Run the Program

1. Make sure Python is installed.
2. Keep `book.py` and `library_manager.py` in the same folder.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run:

```bash
python3 library_manager.py
```

## Menu Options

The program includes four menu options:

1. Add a new book
2. List all books
3. Find a book
4. Exit

## Screencast

Screencast video link: https://www.loom.com/share/fab51d9b94e94eee9dccb9288d8131c6