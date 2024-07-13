from core.library_facade import LibraryFacade
from core.configuration_manager import ConfigurationManager
from core.book_category import BookCategory
from core.book import Book
from core.user import StudentUser, TeacherUser, EmployeeUser

def main():
    # Configurar o sistema de biblioteca
    library = LibraryFacade()

    # Configurar limites de empréstimos pela configuração
    config_manager = ConfigurationManager()
    config_manager.set_configuration("StudentLoanLimit", 2)
    config_manager.set_configuration("TeacherLoanLimit", 4)
    config_manager.set_configuration("EmployeeLoanLimit", 3)

    # Criar categorias e subcategorias
    programming_category = BookCategory("Programming")
    data_science_category = BookCategory("Data Science")
    advanced_programming_category = BookCategory("Advanced Programming")
    programming_category.add_subcategory(advanced_programming_category)

    # Adicionar livros
    library.add_book(Book(1, "Python Programming", "John Doe", programming_category))
    library.add_book(Book(2, "Advanced Python", "Jane Smith", advanced_programming_category))
    library.add_book(Book(3, "Learning Java", "Alan Turing", programming_category))
    library.add_book(Book(4, "Data Science with Python", "Ada Lovelace", data_science_category))

    # Adicionar usuários
    student = StudentUser(1, "Alice")
    teacher = TeacherUser(2, "Bob")
    employee = EmployeeUser(3, "Charlie")
    library.add_user(student)
    library.add_user(teacher)
    library.add_user(employee)

    # Buscar livros por título
    title_search = "Python"
    books_by_title = library.search_books(title=title_search)
    print(f"Livros encontrados com o título '{title_search}':")
    for book in books_by_title:
        print(book)

    # Buscar livros por autor
    author_search = "Jane Smith"
    books_by_author = library.search_books(author=author_search)
    print(f"\nLivros encontrados com o autor '{author_search}':")
    for book in books_by_author:
        print(book)

    # Buscar livros por categoria
    category_search = "Data Science"
    books_by_category = library.search_books(category=category_search)
    print(f"\nLivros encontrados na categoria '{category_search}':")
    for book in books_by_category:
        print(book)

    # Emprestar um livro
    borrow_result = library.borrow_book(1, 1)
    print(f"\n{borrow_result}")

    # Tentar emprestar vários livros até o limite
    borrow_result = library.borrow_book(2, 1)
    print(f"{borrow_result}")
    borrow_result = library.borrow_book(3, 1)
    print(f"{borrow_result}")  # Deve retornar que o limite foi atingido

    # Devolver o livro
    return_result = library.return_book(1, 1)
    print(f"\n{return_result}")

    # Tentar devolver o livro novamente
    return_result = library.return_book(1, 1)
    print(f"{return_result}")

    # Consultar histórico de empréstimos de um usuário
    user_id = 1
    loan_history = library.get_user_loan_history(user_id)
    print(f"\nHistórico de empréstimos do usuário {user_id}:")
    for entry in loan_history:
        book, action = entry
        print(f"Livro: {book.title}, Ação: {action}")

if __name__ == "__main__":
    main()