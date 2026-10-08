from tkinter import *

def read():
    t = text.get()
    print(t)

window = Tk()

text = Text(width=30, height=8, bg="black", fg="white")
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

b = Button(text="Ввод", command=read)
b.pack()


window.mainloop()

