from handlers.handler import Handler
from core.configuration_manager import ConfigurationManager

class LoanLimitHandler(Handler):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self.config_manager = ConfigurationManager()

    def handle(self, book, user):
        user_type_limit = self.config_manager.get_configuration(f"{user.user_type}LoanLimit")
        if len(user.get_borrowed_books()) >= user_type_limit:
            return f"{user.user_type}s can only borrow up to {user_type_limit} books."
        return super().handle(book, user)
