from .catalog_adapter_interface import CatalogAdapterInterface

class CompositeCatalogAdapter(CatalogAdapterInterface):
    def __init__(self, *adapters):
        self.adapters = adapters

    def search_books(self, title=None, author=None, category=None):
        results = []
        for adapter in self.adapters:
            results.extend(adapter.search_books(title, author, category))
        return results
