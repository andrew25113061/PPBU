from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageGrab
from tkinter import messagebox as mb

pen_color = "black"
pen_width = 5


def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + pen_width, y + pen_width, fill=pen_color, outline=pen_color)


def update_pen_width():
    global pen_width
    value = width_entry.get().strip()
    try:
        new_width = int(value)
        if new_width <= 0:
            raise ValueError("Толщина должна быть больше 0")
        pen_width = new_width
        status_label.config(text=f"Толщина пера: {pen_width}")
    except ValueError:
        mb.showerror("Ошибка ввода", "Введите корректное целое число (больше 0) для толщины пера.")
        width_entry.delete(0, END)
        width_entry.insert(0, str(pen_width))  # возвращаем старое значение


def set_color(color):
    global pen_color
    pen_color = color


def load_image():
    try:
        file_path = fd.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        image = Image.open(file_path)
#  вписываем по пропорциям, а не жёстко 600x400
        img_w, img_h = image.size
        scale = min(600 / img_w, 400 / img_h)
        new_w = int(img_w * scale)
        new_h = int(img_h * scale)
        image = image.resize((new_w, new_h))

        image_tk = ImageTk.PhotoImage(image)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor=NW, image=image_tk)
        canvas.image = image_tk
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось загрузить: {e}")


def save_image():
    try:
        file_path = fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
        if file_path:  # Проверяем, был ли указан путь для сохранения
            x = window.winfo_rootx() + canvas.winfo_x()
            y = window.winfo_rooty() + canvas.winfo_y()
            x1 = x + canvas.winfo_width()
            y1 = y + canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            mb.showinfo("Сохранено!", "Изображение успешно сохранено.")
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось сохранить: {e}")


def quit():
    window.destroy()


window = Tk()
window.title("Графический редактор")


canvas = Canvas(window, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

tools_frame = Frame(window)
tools_frame.pack(fill=X, padx=5, pady=5)

color_frame = Frame(tools_frame)
color_frame.pack(side=LEFT)

colors = ["red", "green", "blue", "black", "salmon"]
for color in colors:
    lbl = Label(color_frame, text="", bg=color, width=8, height=2)
    lbl.pack(side=LEFT, padx=2)
    lbl.bind("<Button-1>", lambda e, c=color: set_color(c))

width_frame = Frame(tools_frame)
width_frame.pack(side=RIGHT)

Label(width_frame, text="Толщина:").pack(side=LEFT)
width_entry = Entry(width_frame, width=5)
width_entry.pack(side=LEFT, padx=5)
width_entry.insert(0, str(pen_width))

Button(width_frame, text="Установить", command=update_pen_width).pack(side=LEFT)

status_label = Label(window, text=f"Толщина пера: {pen_width}", fg="gray") # строка текущей толщины пера
status_label.pack(pady=2)


menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить изображение", command=load_image)
file_menu.add_command(label="Сохранить изображение", command=save_image)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=quit)

window.mainloop()

