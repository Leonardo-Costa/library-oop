from .catalog_adapter_interface import CatalogAdapterInterface

class ExternalCatalogAdapter2(CatalogAdapterInterface):
    def search_books(self, title=None, author=None, category=None):
        external_books = [
            {"id": 3, "title": "Learning Java", "author": "Alan Turing", "category": "Programming"},
            {"id": 4, "title": "Data Science with Python", "author": "Ada Lovelace", "category": "Data Science"},
        ]

        results = [book for book in external_books if
                   (title and title.lower() in book["title"].lower()) or
                   (author and author.lower() in book["author"].lower()) or
                   (category and category.lower() in book["category"].lower())]

        return results
