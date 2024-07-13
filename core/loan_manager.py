from core.loan import Loan
from core.configuration_manager import ConfigurationManager
from handlers.book_availability_handler import BookAvailabilityHandler
from handlers.user_eligibility_handler import UserEligibilityHandler
from handlers.loan_limit_handler import LoanLimitHandler

class LoanManager:
    def __init__(self):
        self.loans = []
        self.chain = BookAvailabilityHandler(
            UserEligibilityHandler(
                LoanLimitHandler()
            )
        )

    def borrow_book(self, book, user):
        approval_message = self.chain.handle(book, user)
        if approval_message:
            return approval_message

        book.is_available = False
        user.borrow_book(book)
        loan = Loan(book, user)
        self.loans.append(loan)
        return f"Book '{book.title}' has been borrowed by {user.name}."

    def return_book(self, book, user):
        if book in user.get_borrowed_books():
            book.is_available = True
            user.return_book(book)
            self.loans = [loan for loan in self.loans if loan.book != book or loan.user != user]
            return f"Book '{book.title}' has been returned by {user.name}."
        else:
            return f"Book '{book.title}' was not borrowed by {user.name}."
