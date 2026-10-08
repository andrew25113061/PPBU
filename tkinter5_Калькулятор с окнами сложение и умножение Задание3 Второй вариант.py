from tkinter import *
from tkinter import messagebox as mb

def calc(operation):
    values = [e1.get(), e2.get(), e3.get()]

    for v in values:
        if not v.lstrip('-').isdigit():
            mb.showerror("Ошибка", "В каждое поле должно быть введено число")
            return

    nums = [int(v) for v in values]

    if operation == "sum":
        res = sum(nums)
        expr = f"{nums[0]} + {nums[1]} + {nums[2]} = {res}"
    else:  # "mult"
        res = nums[0] * nums[1] * nums[2]
        expr = f"{nums[0]} * {nums[1]} * {nums[2]} = {res}"

    m1['text'] = expr

    answer = mb.askretrycancel(title="Вопрос", message="Сложить или перемножить еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()

window = Tk()
window.title("Калькулятор")

m = Label(height = 3, text="Введи три числа и нажми на кнопку для вычисления суммы или умножения")
m.pack()

e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()
e3 = Entry()
e3.pack()

b = Button(text="Сложить три числа", command=lambda: calc("sum"))
b.pack()
c = Button(text="Умножить три числа", command=lambda: calc("multip"))
c.pack()

m1 = Label(height=3)
m1.pack()

window.mainloop()
