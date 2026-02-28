# Abstraction and Encapsulation in Python

# 1. Data abstraction and encapsulation are synonymous as data abstraction is achieved through encapsulation. Abstraction is used to hide internal details and show only functionalities. Abstracting something means to give names to things, so that the name captures the basic idea of what a function or a whole program does. Encapsulation is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by accident.

# 2. This program defines a Python class "Library" with the following attributes and methods:

# . __init__ method: This method is called when an object of the class is created. It initializes the books attribute with the passed books list.
# . list_books method: This method prints the available books list.
# . borrow_book method: This method takes a book name as an argument and removes it from the books list if it is present, or prints a message "Book not Available" otherwise.
# . receive_book method: This method takes a book name as an argument and adds it back to the books list.

# 3 The program then creates an object o of the "Library" class, passing the list of books as an argument. A menu-driven interface is then created using a while loop, which provides the user with three options:

# . Display the list of books
# . Borrow a book
# . Return a book

# 4.The user is prompted to enter their choice, and the corresponding method of the o object is called based on the entered choice. If an invalid choice is entered, the program prints a message "Thank You come again" and quits.


# Define Library Class
class Library:
    def __init__(self, books):
        self._books = books  # Encapsulated attribute with underscore

    # List available books (Abstraction: hides internal list details)
    def list_books(self):
        print("\nAvailable Books:")
        for book in self._books:
            print(f"- {book}")
        print()

    # Borrow a book if available
    def borrow_book(self, book_name):
        if book_name in self._books:
            print(f"Get Your Book Now: {book_name}\n")
            self._books.remove(book_name)
        else:
            print("Book Not Available\n")

    # Return a book to the library
    def receive_book(self, book_name):
        print(f"You have returned the book: {book_name}\n")
        self._books.append(book_name)


# Create Library Object
books_list = ["C", "C++", "Java", "Python", "JavaScript"]
library = Library(books_list)

# Menu-Driven Interface
menu = """
1. Display Books
2. Borrow Book
3. Return Book
4. Exit
"""

while True:
    print(menu)
    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Invalid Input! Enter a number 1-4.\n")
        continue

    if choice == 1:
        library.list_books()
    elif choice == 2:
        book = input("Enter Book Name To Borrow: ")
        library.borrow_book(book)
    elif choice == 3:
        book = input("Enter Book Name To Return: ")
        library.receive_book(book)
    elif choice == 4:
        print("Thank You! Come Again.")
        break
    else:
        print("Invalid Choice! Enter 1-4.\n")
