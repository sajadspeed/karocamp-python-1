import tkinter as tk
from shapes import Rectangle, Square, Circle, Triangle

shapes = [
    Rectangle(30, 40, 150, 90, "skyblue"),
    Square(230, 40, 100, "salmon", "darkred", 4),
    Circle(450, 90, 50, "gold"),
    Triangle(540, 40, 120, 100, "lightgreen", "darkgreen", 3),
]

window = tk.Tk()
window.title("Shapes")
canvas = tk.Canvas(window, width=700, height=220, bg="white")
canvas.pack()

for shape in shapes:
    shape.draw(canvas)
    print(shape.info())

window.mainloop()
