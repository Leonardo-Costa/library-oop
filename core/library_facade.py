from core.library_mediator import LibraryMediator
from core.book_availability_notifier import BookAvailabilityNotifier

class LibraryFacade:
    def __init__(self):
        self.mediator = LibraryMediator()
        self.books = {}
        self.users = {}
        self.notifier = BookAvailabilityNotifier()

    def add_book(self, book):
        self.books[book.book_id] = book
        self.notifier.notify_observers(f"New book added: {book.title} by {book.author}")

    def add_user(self, user):
        self.users[user.user_id] = user
        self.notifier.register_observer(user)

    def search_books(self, title=None, author=None, category=None):
        internal_books = [
            book.__dict__ for book in self.books.values() if
            (title and title.lower() in book.title.lower()) or
            (author and author.lower() in book.author.lower()) or
            (category and category.lower() in book.category.name.lower())
        ]
        external_books = self.mediator.search_books(title, author, category)
        return internal_books + external_books

    def borrow_book(self, book_id, user_id):
        if book_id in self.books and user_id in self.users:
            book = self.books[book_id]
            user = self.users[user_id]
            result = self.mediator.borrow_book(book, user)
            if "has been borrowed" in result:
                user.add_to_history(book, "borrowed")
                self.notifier.notify_observers(f"Book borrowed: {book.title} by {user.name}")
            return result
        return "Invalid book or user ID."

    def return_book(self, book_id, user_id):
        if book_id in self.books and user_id in self.users:
            book = self.books[book_id]
            user = self.users[user_id]
            result = self.mediator.return_book(book, user)
            if "has been returned" in result:
                user.add_to_history(book, "returned")
                self.notifier.notify_observers(f"Book returned: {book.title}")
            return result
        return "Invalid book or user ID."

    def get_user_loan_history(self, user_id):
        if user_id in self.users:
            user = self.users[user_id]
            return user.get_loan_history()
        return "Invalid user ID."
