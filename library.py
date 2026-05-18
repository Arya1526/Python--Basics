class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book issued")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print("Book returned")

    def display_books(self):
        print("\nAvailable Books:")

        for book in self.books:
            print(book)


library = Library()

library.add_book("Python")
library.add_book("Java")

library.display_books()

library.issue_book("Python")

library.display_books()

library.return_book("Python")

library.display_books()