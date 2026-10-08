from tkinter import *
import time

window = Tk()

month = time.strftime("%B")
year = time.strftime("%Y")
day = time.strftime("%d")

match month:
    case "October":
        month = "Октября"




time = time.strftime("%d %B %Y")
m = Label(text=f"{day} {month} {year}", font="Verdana 24 bold")
m.pack()


window.mainloop()
