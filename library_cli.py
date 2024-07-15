import cmd
from core.library_facade import LibraryFacade
from core.configuration_manager import ConfigurationManager
from core.book_category import BookCategory
from core.book import Book
from core.user import StudentUser, TeacherUser, EmployeeUser

def print_with_color(message, color_code="33"):
    print(f"\033[{color_code}m{message}\033[0m")

class LibraryCLI(cmd.Cmd):
    intro = 'Bem-vindo ao sistema de biblioteca. Digite help ou ? para listar os comandos.\n'
    prompt = '(biblioteca) '
    
    def __init__(self):
        super().__init__()
        self.library = LibraryFacade()
        self.config_manager = ConfigurationManager()
        self.config_manager.set_configuration("StudentLoanLimit", 2)
        self.config_manager.set_configuration("TeacherLoanLimit", 4)
        self.config_manager.set_configuration("EmployeeLoanLimit", 3)
        
        # Criar categorias e subcategorias
        programming_category = BookCategory("Programming")
        data_science_category = BookCategory("Data Science")
        advanced_programming_category = BookCategory("Advanced Programming")
        programming_category.add_subcategory(advanced_programming_category)
        
        # Adicionar livros
        self.library.add_book(Book(1, "Python Programming", "John Doe", programming_category))
        self.library.add_book(Book(2, "Advanced Python", "Jane Smith", advanced_programming_category))
        self.library.add_book(Book(3, "Learning Java", "Alan Turing", programming_category))
        self.library.add_book(Book(4, "Data Science with Python", "Ada Lovelace", data_science_category))
        
        # Adicionar usuários
        student = StudentUser(1, "Alice")
        teacher = TeacherUser(2, "Bob")
        employee = EmployeeUser(3, "Charlie")
        self.library.add_user(student)
        self.library.add_user(teacher)
        self.library.add_user(employee)

    def do_search_by_title(self, title):
        """Buscar livros por título"""
        books = self.library.search_books(title=title)
        if books:
            print(f"Livros encontrados com o título '{title}':")
            for book in books:
                print(book)
        else:
            print(f"Nenhum livro encontrado com o título '{title}'.")

    def do_search_by_author(self, author):
        """Buscar livros por autor"""
        books = self.library.search_books(author=author)
        if books:
            print(f"Livros encontrados com o autor '{author}':")
            for book in books:
                print(book)
        else:
            print(f"Nenhum livro encontrado com o autor '{author}'.")

    def do_search_by_category(self, category):
        """Buscar livros por categoria"""
        books = self.library.search_books(category=category)
        if books:
            print(f"Livros encontrados na categoria '{category}':")
            for book in books:
                print(book)
        else:
            print(f"Nenhum livro encontrado na categoria '{category}'.")

    def do_borrow_book(self, args):
        """Emprestar um livro. Use o formato: borrow_book <user_id> <book_id>"""
        try:
            user_id, book_id = map(int, args.split())
            result = self.library.borrow_book(user_id, book_id)
            print(result)
        except ValueError:
            print("Uso incorreto. O formato correto é: borrow_book <user_id> <book_id>")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def do_return_book(self, args):
        """Devolver um livro. Use o formato: return_book <user_id> <book_id>"""
        try:
            user_id, book_id = map(int, args.split())
            result = self.library.return_book(user_id, book_id)
            print(result)
        except ValueError:
            print("Uso incorreto. O formato correto é: return_book <user_id> <book_id>")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def do_get_user_loan_history(self, user_id):
        """Consultar histórico de empréstimos de um usuário. Use o formato: get_user_loan_history <user_id>"""
        try:
            history = self.library.get_user_loan_history(int(user_id))
            if history:
                print(f"Histórico de empréstimos do usuário {user_id}:")
                for book, action in history:
                    print(f"Livro: {book.title}, Ação: {action}")
            else:
                print(f"Nenhum histórico encontrado para o usuário {user_id}.")
        except ValueError:
            print("Uso incorreto. O formato correto é: get_user_loan_history <user_id>")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def do_set_loan_limit(self, args):
        """Atualizar limites de empréstimos. Use o formato: set_loan_limit <role> <limit>"""
        try:
            role, limit = args.split()
            limit = int(limit)
            if role == "Student":
                self.config_manager.set_configuration("StudentLoanLimit", limit)
            elif role == "Teacher":
                self.config_manager.set_configuration("TeacherLoanLimit", limit)
            elif role == "Employee":
                self.config_manager.set_configuration("EmployeeLoanLimit", limit)
            else:
                print("Papel inválido. Use Student, Teacher ou Employee.")
                return
            print(f"Novo limite de empréstimos para {role.lower()}s: {self.config_manager.get_configuration(f'{role}LoanLimit')}")
        except ValueError:
            print("Uso incorreto. O formato correto é: set_loan_limit <role> <limit>")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def do_add_book(self, args):
        """Adicionar um novo livro. Use o formato: add_book <book_id> <title> <author> <category>"""
        try:
            book_id, title, author, category_name = args.split(maxsplit=3)
            book_id = int(book_id)
            category = BookCategory(category_name)
            book = Book(book_id, title, author, category)
            self.library.add_book(book)
            print(f"Livro '{title}' adicionado com sucesso.")
        except ValueError:
            print("Uso incorreto. O formato correto é: add_book <book_id> <title> <author> <category>")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def do_exit(self, line):
        """Sair do sistema"""
        print('Saindo...')
        return True

    def do_clear(self, line):
        """Limpa a tela"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    LibraryCLI().cmdloop()
