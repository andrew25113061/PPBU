from tkinter import ***

def read():
    name = e.get()
    print(name)
    e.delete(0, END)

def read2():
    name = e2.get()
    print(name)
    e2.delete(0, END)


window = Tk()

f1 = Frame()
f2 = Frame()
f1.pack()
f2.pack()

m = Label(f1, text="Введите имя: ", bg="gray", fg="white",
          font="Courier 18 bold")
m.pack(side=LEFT)

e = Entry(f1, width=50, justify="center", bg="gray", fg="white",
          font="Courier 18 bold")
e.pack(side=LEFT)

b = Button(f1, text="Ввод ", bg="gray", fg="white",
          font="Courier 18 bold", command=read)
b.pack(side=LEFT)

m2 = Label(f2, text="Введите город: ", bg="gray", fg="white",
          font="Courier 18 bold")
m2.pack(side=LEFT)

e2 = Entry(f2, width=50, justify="center", bg="gray", fg="white",
          font="Courier 18 bold")
e2.pack(side=LEFT)

b2 = Button(f2, text="Ввод ", bg="gray", fg="white",
          font="Courier 18 bold", command=read2)
b2.pack(side=LEFT)


window.mainloop()
