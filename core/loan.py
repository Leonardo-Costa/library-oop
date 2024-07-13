class Loan:
    def __init__(self, book, user):
        self.book = book
        self.user = user

    def __str__(self):
        return f"Loan(Book: {self.book.book_id}, User: {self.user.user_id})"
