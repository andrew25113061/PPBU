#from tkinter import *

#a = 128512

#def change():
#    global a
#    a += 1
#    metka["text"] = chr(a)

#window = Tk()
#metka = Label(text=chr(a), font="Arial 64")
#metka.pack()

#knopka = Button(text="Следующий смайлик", width=25, height=3)
#knopka.config(command=change)
#knopka.pack()

#window.mainloop()

from tkinter import *


window = Tk()

frame_top = Frame(window)
frame_top.pack()
frame_bottom = Frame(window)
frame_bottom.pack()


metka1 = Label(frame_top, text="Метка 1", bg="red")
metka1.pack(side=LEFT)

metka2 = Label(frame_top, text="Метка 2", bg="yellow")
metka2.pack(side=LEFT)

metka3 = Label(frame_top, text="Метка 3", bg="green")
metka3.pack(side=LEFT)

metka4 = Label(frame_bottom, text="Метка 4", bg="blue")
metka4.pack(side=LEFT)

metka5 = Label(frame_bottom, text="Метка 5", bg="gray")
metka5.pack(side=LEFT)

metka6 = Label(frame_bottom, text="Метка 6", bg="salmon")
metka6.pack(side=LEFT)

window.mainloop()
