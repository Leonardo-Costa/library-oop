from abc import ABC, abstractmethod

class CatalogAdapterInterface(ABC):
    @abstractmethod
    def search_books(self, title=None, author=None, category=None):
        pass
