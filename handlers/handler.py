from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, *args, **kwargs):
        if self.next_handler:
            return self.next_handler.handle(*args, **kwargs)
        return None
