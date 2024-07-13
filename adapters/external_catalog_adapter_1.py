from .catalog_adapter_interface import CatalogAdapterInterface

class ExternalCatalogAdapter1(CatalogAdapterInterface):
    def search_books(self, title=None, author=None, category=None):
        external_books = [
            {"id": 1, "title": "Python Programming", "author": "John Doe", "category": "Programming"},
            {"id": 2, "title": "Advanced Python", "author": "Jane Smith", "category": "Programming"},
        ]

        results = [book for book in external_books if
                   (title and title.lower() in book["title"].lower()) or
                   (author and author.lower() in book["author"].lower()) or
                   (category and category.lower() in book["category"].lower())]

        return results
