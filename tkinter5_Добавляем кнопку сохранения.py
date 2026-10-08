from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd

def delete():
    text.delete(1.0, END)

def insert():
    try:
        file = fd.askopenfilename()
        if file:
            with open(file, "r") as f:
                s = f.read()
            text.insert(1.0, s)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не найден.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка {e}")

def save():
    try:
        file = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("ALL files:", "*.*")))
        if file:
            with open(file, "w") as f:
                s = text.get(1.0, END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не найден.")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка {e}")           


window = Tk()
text = Text(width=30, height=8, bg="black", fg="white", wrap=WORD)
text.pack(side=LEFT)
scroll = Scrollbar(command=text.yview)
scroll.pack(side= LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
b = Button(text="Вставка текста", command=insert)
b.pack(side=LEFT)

b2 = Button(text="Удаление текста", command=delete)
b2.pack(side=LEFT)

b3 = Button(text="Сохранить", command=save)
b3.pack(side=LEFT)



window.mainloop()
