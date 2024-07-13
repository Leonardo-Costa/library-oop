class BookCategory:
    def __init__(self, name):
        self.name = name
        self.subcategories = []

    def add_subcategory(self, subcategory):
        self.subcategories.append(subcategory)

    def get_all_subcategories(self):
        return self.subcategories

    def __str__(self):
        return self.name
