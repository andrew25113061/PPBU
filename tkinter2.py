#from tkinter import *

#a = 1

#def change():
#    global a
#    a += 1
#    metka["text"] = a

#window = Tk()
#metka = Label(text="1", width=30, height=3)
#metka.pack()

#knopka = Button(text="Инкремент", width=15, height=3)
#knopka.config(command=change)
#knopka.pack()

#window.mainloop()


from tkinter import *

a = 100

def change():
    global a
    a -= 1
    metka["text"] = a

window = Tk()
metka = Label(text="100", width=30, height=3)
metka.pack()

knopka = Button(text="Декремент", width=15, height=3)
knopka.config(command=change)
knopka.pack()

window.mainloop()
