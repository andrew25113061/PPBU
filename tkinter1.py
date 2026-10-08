from tkinter import *

window = Tk()

def change():
    metka["text"] = "Черная метка"
    metka["bg"] = "black"

metka = Label(text="Привет всем!", bg="Salmon", fg="Green", width=15,
              height=5)
metka.pack()

knopka = Button(text="Изменить метку", width=15, height=3)
knopka.config(command=change)
knopka.pack()

window.mainloop()
