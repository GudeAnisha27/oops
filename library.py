class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.book_id})"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        for book in available_books:
            print(book)

    def borrow_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)

        if member and book and book.is_available:
            member.books_borrowed.append(book)
            book.is_available = False
            print(f"{member.name} borrowed '{book.title}'.")

    def return_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = next((b for b in member.books_borrowed if b.book_id == book_id), None)

        if member and book:
            member.books_borrowed.remove(book)
            book.is_available = True
            print(f"{member.name} returned '{book.title}'.")

    def find_member_by_id(self, member_id):
        return next((member for member in self.members if member.member_id == member_id), None)

    def find_book_by_id(self, book_id):
        return next((book for book in self.books if book.book_id == book_id), None)



book1 = Book(1, "The Hobbit", "J.R.R. Tolkien")
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")

member1 = Member(101, "Alice")
member2 = Member(102, "Bob")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.add_member(member2)

library.display_available_books()

library.borrow_book(101, 1)
library.borrow_book(102, 2)

library.return_book(101, 1)

library.display_available_books()
