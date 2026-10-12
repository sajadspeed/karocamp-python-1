import tkinter as tk


class Shape:
    def __init__(self, x, y, color, border_color="black", border_width=2):
        self.x = x
        self.y = y
        self.color = color
        self.border_color = border_color
        self.border_width = border_width

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def area(self):
        return 0

    def draw(self, canvas):
        pass

    def info(self):
        return f"{self.__class__.__name__}  area = {self.area():.0f}"



class Rectangle(Shape):
    def __init__(self, x, y, width, height, color, border_color="black", border_width=2):
        super().__init__(x, y, color, border_color, border_width)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self, canvas):
        canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height,
            fill=self.color, outline=self.border_color, width=self.border_width)


class Square(Rectangle):
    def __init__(self, x, y, side, color, border_color="black", border_width=2):
        super().__init__(x, y, side, side, color, border_color, border_width)


class Circle(Shape):
    def __init__(self, x, y, radius, color, border_color="black", border_width=2):
        super().__init__(x, y, color, border_color, border_width)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def draw(self, canvas):
        canvas.create_oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            fill=self.color, outline=self.border_color, width=self.border_width)


class Triangle(Shape):
    def __init__(self, x, y, base, height, color, border_color="black", border_width=2):
        super().__init__(x, y, color, border_color, border_width)
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

    def draw(self, canvas):
        canvas.create_polygon(
            self.x, self.y + self.height,
            self.x + self.base, self.y + self.height,
            self.x + self.base / 2, self.y,
            fill=self.color, outline=self.border_color, width=self.border_width)
