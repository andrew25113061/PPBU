from tkinter import *
import tkinterweb

def read():
    site = e.get()
    frame.load_website(site)

window = Tk()

f = Frame()
f.pack()

m = Label(f, text="введите адрес сайта: ")
m.pack(side=LEFT)
e = Entry(f, width=20)
e.pack(side=LEFT)

d = Button(f, text="Ввод", command=read)
d.pack(side=LEFT)

frame = tkinterweb.HtmlFrame(window)

frame.pack(fill="both", expand = 1)


window.mainloop()
