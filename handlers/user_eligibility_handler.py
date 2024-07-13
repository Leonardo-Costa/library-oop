from handlers.handler import Handler

class UserEligibilityHandler(Handler):
    def handle(self, book, user):
        # Assumindo que todos os usuários são elegíveis
        return super().handle(book, user)
