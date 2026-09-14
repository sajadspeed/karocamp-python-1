import tkinter as tk

counter = 1

window = tk.Tk()
window.geometry("300x300")

label_welcome = tk.Label(window, text=counter, font=("Console", 24))
label_welcome.pack()


def button_change_name_clicked():
    global counter
    counter += 1
    label_welcome.config(text=counter)


button_change_name = tk.Button(
    window, text="Press me. Please.", command=button_change_name_clicked
)
button_change_name.pack()

# Widgets are added here

window.mainloop()
