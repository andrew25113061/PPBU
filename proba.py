from tkinter import *
import tkinterweb

window = Tk()
frame = tkinterweb.HtmlFrame(window)
frame.load_website("https://www.google.com")
frame.pack(fill='both', expand=1)

window.mainloop()
