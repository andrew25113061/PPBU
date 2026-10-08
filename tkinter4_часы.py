from tkinter import *
import time

window = Tk()

def tick():
    t = time.strftime("%H:%M:%S")
    m.config(text=t)
    m.after(1000, tick)

m = Label(font="Verdana 24 bold")
m.pack()

c = Checkbutton(text="Это переключатель цвета", variable=v,
                onvalue="red", offvalue="black", command=show)
c.pack()








tick()

window.mainloop()
