from library import Library
from book import Book

library = Library()

library.add_item(Book("Clean Code", "Robert C. Martin"))
library.add_item(Book("Python Crash Course", "Eric Matthes"))

library.borrow_item("Clean Code")
library.show_items()
