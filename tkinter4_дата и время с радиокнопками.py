from tkinter import *
import datetime as dt


def f1():
    m.config(text = f"{date} {time}")

def f2():
    m.config(text = f"{date}")

def f3():
    m.config(text = f"{time}")

def night():
    m.config(bg="black", fg="white")
    r1.config(bg="black", fg="white")
    r2.config(bg="black", fg="white")
    r3.config(bg="black", fg="white")
    r4.config(bg="black", fg="white")



window = Tk()

d = dt.datetime.now()
date = d.strftime("%d %B %Y")
time = d.strftime("%X")

var = IntVar()
var.set(0)

r1 = Radiobutton(text="Дата и время", command=f1, variable=var, value=0)
r1.pack(side=LEFT)

r2 = Radiobutton(text="Дата", command=f2, variable=var, value=1)
r2.pack(side=LEFT)

r3 = Radiobutton(text="Время", command=f3, variable=var, value=2)
r3.pack(side=LEFT)

r4 = Radiobutton(text="Ночная тема", command=night, variable=var, value=3)
r4.pack(side=LEFT)



m = Label(text=f"{date} {time}", font="Verdana 24 bold")
m.pack(side=LEFT)


window.mainloop()
