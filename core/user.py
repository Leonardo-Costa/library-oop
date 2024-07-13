from core.observer import Observer

class User(Observer):
    def __init__(self, user_id, name, user_type):
        self.user_id = user_id
        self.name = name
        self.user_type = user_type
        self.loan_history = []
        self.borrowed_books = []

    def update(self, message):
        print(f"Notification for {self.name}: {message}")

    def add_to_history(self, book, action):
        self.loan_history.append((book, action))

    def get_loan_history(self):
        return self.loan_history

    def get_borrowed_books(self):
        return self.borrowed_books

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.name}', type='{self.user_type}')"

class StudentUser(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "Student")

class TeacherUser(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "Teacher")

class EmployeeUser(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "Employee")
