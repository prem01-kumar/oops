from abc import ABC, abstractmethod

# Abstract Class
class LibraryOperations(ABC):
    @abstractmethod
    def issue_book(self):
        pass

    @abstractmethod
    def return_book(self):
        pass


# Parent Class
class Person:
    def __init__(self, name):
        self.name = name


# Child Class
class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(name)
        self.student_id = student_id

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")


# Book Class (Encapsulation)
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__status = "Available"

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def display_book(self):
        print("\nBook Details")
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)
        print("Status  :", self.__status)


# Library Class
class Library(LibraryOperations):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book Added Successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                book.display_book()

    def search_book(self, title):
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                book.display_book()
                found = True
                break

        if not found:
            print("Book Not Found!")

    def issue_book(self):
        book_id = int(input("Enter Book ID to issue: "))

        for book in self.books:
            if book.book_id == book_id:
                if book.get_status() == "Available":
                    book.set_status("Issued")
                    print("Book Issued Successfully!")
                else:
                    print("Book Already Issued!")
                return

        print("Book Not Found!")

    def return_book(self):
        book_id = int(input("Enter Book ID to return: "))

        for book in self.books:
            if book.book_id == book_id:
                if book.get_status() == "Issued":
                    book.set_status("Available")
                    print("Book Returned Successfully!")
                else:
                    print("This book was not issued.")
                return

        print("Book Not Found!")


# Main Program
library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Register Student")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == 2:
        library.view_books()

    elif choice == 3:
        title = input("Enter Book Title to Search: ")
        library.search_book(title)

    elif choice == 4:
        library.issue_book()

    elif choice == 5:
        library.return_book()

    elif choice == 6:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")

        student = Student(student_id, name)

        print("\nStudent Registered Successfully!")
        student.display()

    elif choice == 7:
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")