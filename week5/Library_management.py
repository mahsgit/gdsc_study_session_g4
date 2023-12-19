class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability_status = "available"

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.ISBN)
        print("Availability:", self.availability_status)

    def update_availability(self, status):
        self.availability_status = status
        
        
        
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        print("User ID:", self.user_id)
        print("Name:", self.name)
        print("Books Borrowed:", self.books_borrowed)

    def borrow_book(self, book):
        if book.availability_status == "available":
            book.update_availability("borrowed")
            self.books_borrowed.append(book)
            print("Book", book.title, " borrowed.")
        else:
            print("Book", book.title, "is not available.")

    def return_book(self, book):
        if book in self.books_borrowed:
            book.update_availability("available")
            self.books_borrowed.remove(book)
            print("Book", book.title, " returned.")
        else:
            print("Book", book.title, "was not borrowed.")
            
            
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    

    def display_all_books(self):
        for book in self.books:
            print("Title:", book.title)
            print("Author:", book.author)
            print("ISBN:", book.ISBN)
            print("Availability:", book.availability_status)


    




class Transaction:
    def __init__(self, user, book, transaction_type):
        self.user = user
        self.book = book
        self.transaction_type = transaction_type

    def generate_report(self):
        print("User ID:", self.user.user_id)
        print("User Name:", self.user.name)
        print("Book Title:", self.book.title)
        print("Transaction Type:", self.transaction_type)
        
book1 = Book("Book 1", "Author 1", "ISBN1")

user1 = User("001", "User 1")

library = Library()

library.add_book(book1)
library.register_user(user1)

library.display_all_books()

user1.borrow_book(book1)

user1.return_book(book1)

transaction = Transaction(user1, book1, "borrow")
transaction.generate_report()