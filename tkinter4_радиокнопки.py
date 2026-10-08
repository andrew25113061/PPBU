from tkinter import *
import time

window = Tk()

kvas = "квас"
tea = "чай"
coffee = "кофе"
limonad = "лимонад"

width = len(limonad) + 2

drink = StringVar(value=coffee)

m = Label(text="Выбери любимый напиток: ")
m.pack()

m2 = Label(textvariable=drink, bg="salmon")
m2.pack(padx=25) 

b1 = Radiobutton(text=kvas, value=kvas, variable=drink, width=width, anchor="w")
b1.pack(padx=5)

b2 = Radiobutton(text=tea, value=tea, variable=drink, width=width, anchor="w")
b2.pack(padx=5)

b3 = Radiobutton(text=coffee, value=coffee, variable=drink, width=width, anchor="w")
b3.pack(padx=5)

b4 = Radiobutton(text=limonad, value=limonad, variable=drink, width=width, anchor="w")
b4.pack(padx=5)




window.mainloop()
