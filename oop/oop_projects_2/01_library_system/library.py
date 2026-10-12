class Library:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def borrow_item(self, title):
        for item in self._items:
            if item.title == title:
                if item.borrow():
                    print(f"{title} borrowed successfully.")
                else:
                    print(f"{title} is already borrowed.")
                return
        print("Item not found.")

    def show_items(self):
        for item in self._items:
            print(item.get_info())
