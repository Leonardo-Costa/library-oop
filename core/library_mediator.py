from adapters.external_catalog_adapter_1 import ExternalCatalogAdapter1
from adapters.external_catalog_adapter_2 import ExternalCatalogAdapter2
from adapters.composite_catalog_adapter import CompositeCatalogAdapter
from core.loan_manager import LoanManager

class LibraryMediator:
    def __init__(self):
        adapter1 = ExternalCatalogAdapter1()
        adapter2 = ExternalCatalogAdapter2()
        self.catalog_adapter = CompositeCatalogAdapter(adapter1, adapter2)
        self.loan_manager = LoanManager()

    def search_books(self, title=None, author=None, category=None):
        return self.catalog_adapter.search_books(title, author, category)

    def borrow_book(self, book, user):
        return self.loan_manager.borrow_book(book, user)

    def return_book(self, book, user):
        return self.loan_manager.return_book(book, user)
