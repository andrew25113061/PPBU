from tkinter import *
from tkinter import messagebox as mb


def summ():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено число")
        return  # Возвращаемся из функции, если ввод некорректен
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return  # Возвращаемся из функции, если ввод некорректен
    s3 = e3.get()
    if not s3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В третье поле должно быть введено число")
        return  # Возвращаемся из функции, если ввод некорректен
    slag1 = int(s1)
    slag2 = int(s2)
    slag3 = int(s3)
    summa = slag1 + slag2 + slag3
    m1['text']= f"{s1} + {s2} + {s3}= {str(summa)}"
        
    answer = mb.askretrycancel(title="Вопрос", message="Сложить или перемножить еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text']= ""
    else:
        window.destroy()

def multip():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено число")
        return  # Возвращаемся из функции, если ввод некорректен
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return  # Возвращаемся из функции, если ввод некорректен
    s3 = e3.get()
    if not s3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В третье поле должно быть введено число")
        return  # Возвращаемся из функции, если ввод некорректен
    factor1 = int(s1)
    factor2 = int(s2)
    factor3 = int(s3)
    multiply = factor1 * factor2 * factor3
    m1['text']= f"{s1} * {s2} * {s3}= {str(multiply)}"
        
    answer = mb.askretrycancel(title="Вопрос", message="Сложить или умножить еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text']= ""
    else:
        window.destroy()


    

window = Tk()

window.title("Калькулятор")
m = Label(height=3, text="Введи три числа и нажми на кнопку для вычисления суммы или умножения")
m.pack()
e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()
e3 = Entry()
e3.pack()


b = Button(text="Сложить три числа", command=summ)
b.pack()

c = Button(text="Умножить три числа", command=multip)
c.pack()

m1 = Label(height=3)
m1.pack()



window.mainloop()
