from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageGrab
from tkinter import messagebox as mb


def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color)


def load_image():
    try:
        file_path = fd.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((600, 400))
            image_tk = ImageTk.PhotoImage(image)
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

pen_color = "black"
canvas = Canvas(window, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

colors = ["red", "green", "blue", "black"]
for color in colors:
    lbl = Label(window, text="", bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().update(pen_color=c))

# Button(window, text="Загрузить изображение", command=load_image).pack()
# Button(window, text="Сохранить изображение", command=save_image).pack()


menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить изображение", command=load_image)
file_menu.add_command(label="Сохранить изображение", command=save_image)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=quit)

window.mainloop()

