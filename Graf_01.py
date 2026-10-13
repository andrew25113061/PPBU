# Графический редактор


from tkinter import *

pen_color = "black"

# Функция для рисования на холсте
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color)


window = Tk()
window.title("Графический редактор")

canvas = Canvas(window, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

colors = ["red", "green", "blue", "black"]
for color in colors:
    lbl = Label(window, text="", bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().update(pen_color=c))


window.mainloop()

