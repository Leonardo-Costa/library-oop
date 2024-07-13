- [Sistema de Biblioteca](#sistema-de-biblioteca)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Descrição das Classes](#descrição-das-classes)
  - [Instruções de Uso](#instruções-de-uso)
    - [Pré-requisitos](#pré-requisitos)
    - [Instalação](#instalação)
    - [Executando o Projeto](#executando-o-projeto)
  - [Funcionalidades](#funcionalidades)
  - [Exemplo de Uso](#exemplo-de-uso)
  - [Diagrama UML](#diagrama-uml)
  - [Contato](#contato)

# Sistema de Biblioteca
Este projeto é um sistema de biblioteca implementado em Python que utiliza diversos padrões de design para facilitar a busca, empréstimo e devolução de livros, além de gerenciar categorias de livros, usuários, e notificações.

## Estrutura do Projeto
A estrutura do projeto está organizada em pastas conforme abaixo:

```
librarySystem/
│
├── adapters/
│   ├── catalog_adapter_interface.py
│   ├── external_catalog_adapter_1.py
│   ├── external_catalog_adapter_2.py
│   └── composite_catalog_adapter.py
│
├── core/
│   ├── library_mediator.py
│   ├── library_facade.py
│   ├── book_category.py
│   ├── book.py
│   ├── observer.py
│   ├── user.py
│   ├── loan.py
│   ├── loan_manager.py
│   ├── configuration_manager.py
│   └── book_availability_notifier.py
│
├── handlers/
│   ├── handler.py
│   ├── book_availability_handler.py
│   └── user_eligibility_handler.py
│   └── loan_limit_handler.py
│
└── main.py
```

## Descrição das Classes
|\#|	Nome da Classe	|Resumo do que a Classe Faz|
|---|---|---|
|1	|CatalogAdapterInterface	|Interface abstrata para busca de livros em catálogos externos|
|2|	ExternalCatalogAdapter1| 	Adapter para buscar livros em um catálogo externo específico|
|3|	ExternalCatalogAdapter2| 	Adapter para buscar livros em outro catálogo externo específico|
|4|	CompositeCatalogAdapter| 	Combina resultados de múltiplos adapters de catálogos externos|
|5|	LibraryMediator| 	Coordena interações de busca, empréstimo e devolução de livros|
|6|	LibraryFacade| 	Fornece uma interface simplificada para operações de biblioteca|
|7|	BookCategory| 	Gerencia categorias de livros de forma hierárquica|
|8|	Book| 	Representa um livro, com atributos como título, autor e disponibilidade|
|9|	Observer| 	Interface abstrata para o padrão Observer|
|10|	User| 	Usuário da biblioteca que recebe notificações (Observer)|
|11|	StudentUser| 	Subclasse de User representando um estudante|
|12|	TeacherUser| 	Subclasse de User representando um professor|
|13|	EmployeeUser| 	Subclasse de User representando um funcionário|
|14|	Loan| 	Representa um empréstimo de livro|
|15|	LoanManager| 	Gerencia empréstimos e devoluções de livros|
|16|	ConfigurationManager| 	Gerencia configurações globais do sistema|
|17|	BookAvailabilityNotifier| 	Notifica usuários sobre mudanças no status dos livros|
|18|	Handler| 	Classe base abstrata para implementar a cadeia de responsabilidade|
|19|	BookAvailabilityHandler| 	Verifica se o livro está disponível para empréstimo|
|20|	UserEligibilityHandler| 	Verifica se o usuário é elegível para realizar empréstimos|
|21|	LoanLimitHandler| 	Verifica se o usuário não ultrapassou seu limite de empréstimos|
|22|	main| 	Configura o sistema de biblioteca e realiza operações de exemplo|

## Instruções de Uso

### Pré-requisitos
Certifique-se de ter o Python 3.x instalado em sua máquina.

### Instalação
Clone o repositório para sua máquina local:

```bash
git clone https://github.com/Leonardo-Costa/library-oop.git
cd library-oop
```

### Executando o Projeto
Para começar a usar o sistema de biblioteca, execute o script main.py:

```
python main.py
```
## Funcionalidades

O sistema de biblioteca oferece as seguintes funcionalidades principais:

1. Buscar Livros: Pesquisa livros disponíveis no sistema e em catálogos externos por título, autor ou categoria.
2. Emprestar Livros: Permite que usuários qualificados empréstem livros disponíveis.
3. Devolver Livros: Permite que usuários devolvam livros que emprestaram.
4. Gerenciar Categorias: Adiciona e gerencia categorias de livros de forma hierárquica.
5. Notificar Usuários: Notifica usuários sobre eventos importantes, como adição de novos livros ou empréstimos bem-sucedidos.
6. Exemplo de Uso
7. No arquivo main.py, há exemplos de como adicionar livros e usuários, buscar livros, emprestar e devolver livros. Aqui está um pequeno exemplo:

```python
from core.library_facade import LibraryFacade
from core.book_category import BookCategory
from core.book import Book
from core.user import StudentUser

def main():
    library = LibraryFacade()

    programming_category = BookCategory("Programming")
    library.add_book(Book(1, "Python Programming", "John Doe", programming_category))

    student = StudentUser(1, "Alice")
    library.add_user(student)

    print(library.search_books(title="Python"))  # Busca livros pelo título "Python"
    print(library.borrow_book(1, 1))             # Empréstimo do livro com ID 1 pelo usuário com ID 1
    print(library.return_book(1, 1))             # Devolução do livro com ID 1 pelo usuário com ID 1

if __name__ == "__main__":
    main()
```

## Diagrama UML

```mermaid
classDiagram
    class CatalogAdapterInterface {
        +search_books(title, author, category)
    }
    class ExternalCatalogAdapter1 {
        +search_books(title, author, category)
    }
    class ExternalCatalogAdapter2 {
        +search_books(title, author, category)
    }
    class CompositeCatalogAdapter {
        -adapters
        +search_books(title, author, category)
    }
    class LibraryMediator {
        -catalog_adapter
        -loan_manager
        +search_books(title, author, category)
        +borrow_book(book, user)
        +return_book(book, user)
    }
    class LibraryFacade {
        -mediator
        -books
        -users
        -notifier
        +add_book(book)
        +add_user(user)
        +search_books(title, author, category)
        +borrow_book(book_id, user_id)
        +return_book(book_id, user_id)
        +get_user_loan_history(user_id)
    }
    class BookCategory {
        -name
        -subcategories
        +add_subcategory(subcategory)
        +get_all_subcategories()
    }
    class Book {
        -book_id
        -title
        -author
        -category
        -is_available
    }
    class Observer {
        +update(message)
    }
    class User {
        -user_id
        -name
        -user_type
        -loan_history
        -borrowed_books
        +update(message)
        +add_to_history(book, action)
        +get_loan_history()
        +get_borrowed_books()
        +borrow_book(book)
        +return_book(book)
    }
    class StudentUser {
    }
    class TeacherUser {
    }
    class EmployeeUser {
    }
    class Loan {
        -book
        -user
    }
    class LoanManager {
        -loans
        -chain
        +borrow_book(book, user)
        +return_book(book, user)
    }
    class ConfigurationManager {
        -_configurations
        +get_configuration(key)
        +set_configuration(key, value)
    }
    class BookAvailabilityNotifier {
        -observers
        +register_observer(observer)
        +unregister_observer(observer)
        +notify_observers(message)
    }
    class Handler {
        +handle(*args, **kwargs)
    }
    class BookAvailabilityHandler {
        +handle(book, user)
    }
    class UserEligibilityHandler {
        +handle(book, user)
    }
    class LoanLimitHandler {
        +handle(book, user)
    }

    CatalogAdapterInterface <|-- ExternalCatalogAdapter1
    CatalogAdapterInterface <|-- ExternalCatalogAdapter2
    CatalogAdapterInterface <|-- CompositeCatalogAdapter
    CompositeCatalogAdapter o-- CatalogAdapterInterface
    LibraryMediator o-- CompositeCatalogAdapter
    LibraryMediator o-- LoanManager
    LibraryFacade o-- LibraryMediator
    LibraryFacade o-- BookAvailabilityNotifier
    User <|-- StudentUser
    User <|-- TeacherUser
    User <|-- EmployeeUser
    LoanManager o-- Loan
    LoanManager o-- Handler
    Handler <|-- BookAvailabilityHandler
    Handler <|-- UserEligibilityHandler
    Handler <|-- LoanLimitHandler
    Loan o-- Book
    Loan o-- User
    Book o-- BookCategory
    BookAvailabilityNotifier o-- Observer
    User o-- Observer
    ConfigurationManager "1" -- "*" LoanLimitHandler : singleton instance
```

Contato
Leonardo Loureiro Costa - leonardo.costa@unifesp.br

Link do Projeto: https://github.com/Leonardo-Costa/library-oop
