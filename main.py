from core.library_facade import LibraryFacade
from core.configuration_manager import ConfigurationManager
from core.book_category import BookCategory
from core.book import Book
from core.user import StudentUser, TeacherUser, EmployeeUser

def print_with_color(message, color_code="33"):
    print(f"\033[{color_code}m{message}\033[0m")

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
    print_with_color("\n### Buscar livros por título ###", "36")
    title_search = "Python"
    books_by_title = library.search_books(title=title_search)
    print(f"Livros encontrados com o título '{title_search}':\n")
    for book in books_by_title:
        print(book)

    # Buscar livros por autor
    print_with_color("\n### Buscar livros por autor ###", "36")
    author_search = "Jane Smith"
    books_by_author = library.search_books(author=author_search)
    print(f"\nLivros encontrados com o autor '{author_search}':\n")
    for book in books_by_author:
        print(book)

    # Buscar livros por categoria
    print_with_color("\n### Buscar livros por categoria ###", "36")
    category_search = "Data Science"
    books_by_category = library.search_books(category=category_search)
    print(f"\nLivros encontrados na categoria '{category_search}':\n")
    for book in books_by_category:
        print(book)

    # Emprestar um livro
    print_with_color("\n### Emprestar um livro ###", "36")
    borrow_result = library.borrow_book(1, 1)
    print(f"\n{borrow_result}")

    # Tentar emprestar vários livros até o limite
    print_with_color("\n### Emprestar vários livros até o limite ###", "36")
    borrow_result = library.borrow_book(2, 1)
    print(f"{borrow_result}")
    borrow_result = library.borrow_book(3, 1)
    print(f"{borrow_result}")  # Deve retornar que o limite foi atingido

    # Devolver o livro
    print_with_color("\n### Devolver o livro ###", "36")
    return_result = library.return_book(1, 1)
    print(f"\n{return_result}")

    # Tentar devolver o livro novamente
    print_with_color("\n### Tentar devolver o livro novamente ###", "36")
    return_result = library.return_book(1, 1)
    print(f"{return_result}")

    # Consultar histórico de empréstimos de um usuário
    print_with_color("\n### Consultar histórico de empréstimos ###", "36")
    user_id = 1
    loan_history = library.get_user_loan_history(user_id)
    print(f"\nHistórico de empréstimos do usuário {user_id}:")
    for entry in loan_history:
        book, action = entry
        print(f"Livro: {book.title}, Ação: {action}")

    # Adicionar mais exemplos relevantes

    # Remover um usuário
    print_with_color("\n### Remover um usuário (não implementado) ###", "36")
    # library.remove_user(2)  # Placeholder, o método não está implementado

    # Atualizar limites de empréstimos durante a execução
    print_with_color("\n### Atualizar limites de empréstimos ###", "36")
    config_manager.set_configuration("StudentLoanLimit", 3)
    print(f"Novo limite de empréstimos para estudantes: {config_manager.get_configuration('StudentLoanLimit')}")

    # Notificações aos usuários
    print_with_color("\n### Notificações aos usuários ###", "36")
    library.add_book(Book(5, "New Book Title", "New Author", programming_category))

if __name__ == "__main__":
    main()
