class Book:
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.is_available = True

    def __str__(self):
        return f"Book(ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Category: {self.category}, Available: {self.is_available})"
