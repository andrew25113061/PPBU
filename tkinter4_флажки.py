from tkinter import *

def show():
    c["fg"] = v.get()
    m["text"] = v.get()

window = Tk()
window.title("Это флажки")

v = StringVar()
v.set("black")

c = Checkbutton(text="Это переключатель цвета", variable=v,
                onvalue="red", offvalue="black", command=show)
c.pack()

m = Label(text="Метка", width=15, height=3, bg="lightgray")
m.pack()


window.mainloop()
