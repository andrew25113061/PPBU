from tkinter import *

window = Tk()
window.title("Главное окно")
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
print(f"Размеры вашего экрана {w} на {h} пикселей")
