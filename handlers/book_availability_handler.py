from handlers.handler import Handler

class BookAvailabilityHandler(Handler):
    def handle(self, book, user):
        if not book.is_available:
            return f"Book '{book.title}' is not available."
        return super().handle(book, user)
