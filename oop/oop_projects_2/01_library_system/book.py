from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title
        self._available = True

    def borrow(self):
        if not self._available:
            return False
        self._available = False
        return True

    def return_item(self):
        self._available = True

    @abstractmethod
    def get_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def get_info(self):
        status = "available" if self._available else "borrowed"
        return f"{self.title} by {self.author} ({status})"


class Magazine(LibraryItem):
    def __init__(self, title, issue):
        super().__init__(title)
        self.issue = issue

    def get_info(self):
        status = "available" if self._available else "borrowed"
        return f"{self.title}, issue {self.issue} ({status})"
