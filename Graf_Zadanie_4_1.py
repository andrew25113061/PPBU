from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageDraw
from tkinter import messagebox as mb

pen_color = "black"
pen_width = 5
last_x = None
last_y = None

# Список всех нарисованных штрихов: (x1, y1, x2, y2, color, width)
strokes = []

# Загруженное фоновое изображение (PIL) или None
base_image = None

CANVAS_W = 600
CANVAS_H = 400


def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y
    r = pen_width / 2
    canvas.create_oval(event.x - r, event.y - r,
                       event.x + r, event.y + r,
                       fill=pen_color, outline=pen_color)
    strokes.append((event.x, event.y, event.x, event.y, pen_color, pen_width))


def draw(event):
    global last_x, last_y
    if last_x is None:
        last_x, last_y = event.x, event.y
        return
    canvas.create_line(last_x, last_y, event.x, event.y,
                       fill=pen_color, width=pen_width,
                       capstyle=ROUND, joinstyle=ROUND, smooth=True)
    strokes.append((last_x, last_y, event.x, event.y, pen_color, pen_width))
    last_x, last_y = event.x, event.y


def reset_last(event=None):
    global last_x, last_y
    last_x, last_y = None, None


def update_pen_width():
    global pen_width
    value = width_entry.get().strip()
    try:
        new_width = int(value)
        if new_width <= 0:
            raise ValueError
        pen_width = new_width
        status_label.config(text=f"Толщина пера: {pen_width}")
    except ValueError:
        mb.showerror("Ошибка ввода",
                     "Введите корректное целое число (больше 0) для толщины пера.")
        width_entry.delete(0, END)
        width_entry.insert(0, str(pen_width))


def set_color(color):
    global pen_color
    pen_color = color


def load_image():
    global base_image
    try:
        file_path = fd.askopenfilename(
            filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')]
        )
        if not file_path:
            return

        image = Image.open(file_path)
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGB")

        img_w, img_h = image.size
        scale = min(CANVAS_W / img_w, CANVAS_H / img_h)
        new_w = max(1, int(img_w * scale))
        new_h = max(1, int(img_h * scale))
        image = image.resize((new_w, new_h), Image.LANCZOS)

        # Кладём на белый холст размером с canvas (по центру)
        base_image = Image.new("RGB", (CANVAS_W, CANVAS_H), "white")
        offset_x = (CANVAS_W - new_w) // 2
        offset_y = (CANVAS_H - new_h) // 2
        if image.mode == "RGBA":
            base_image.paste(image, (offset_x, offset_y), image)
        else:
            base_image.paste(image, (offset_x, offset_y))

        image_tk = ImageTk.PhotoImage(base_image)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor=NW, image=image_tk)
        canvas.image = image_tk

        # Штрихи, нарисованные до загрузки, оставляем — они лягут поверх
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось загрузить: {e}")


def save_image():
    """Рендерим изображение из модели strokes в PIL.Image — точно 1:1 с canvas."""
    try:
        file_path = fd.asksaveasfilename(
            defaultextension='.png',
            filetypes=[('PNG files', '*.png'), ('All files', '*.*')]
        )
        if not file_path:
            return

        # Фон
        if base_image is not None:
            result = base_image.copy()
        else:
            result = Image.new("RGB", (CANVAS_W, CANVAS_H), "white")

        # Рисуем все штрихи
        drawer = ImageDraw.Draw(result)
        for (x1, y1, x2, y2, color, width) in strokes:
            if x1 == x2 and y1 == y2:
                # Точка — рисуем кружок радиуса width/2
                r = width / 2
                drawer.ellipse((x1 - r, y1 - r, x1 + r, y1 + r),
                               fill=color, outline=color)
            else:
                drawer.line((x1, y1, x2, y2),
                            fill=color, width=width, joint="curve")
                # Круглые «шапки» на концах сегмента
                r = width / 2
                drawer.ellipse((x1 - r, y1 - r, x1 + r, y1 + r), fill=color)
                drawer.ellipse((x2 - r, y2 - r, x2 + r, y2 + r), fill=color)

        result.save(file_path)
        mb.showinfo("Сохранено!", "Изображение успешно сохранено.")
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось сохранить: {e}")


def clear_canvas():
    global base_image
    canvas.delete("all")
    canvas.image = None
    strokes.clear()
    base_image = None


def exit_app():
    window.destroy()


window = Tk()
window.title("Графический редактор")

canvas = Canvas(window, width=CANVAS_W, height=CANVAS_H, bg="white")
canvas.pack()
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset_last)

tools_frame = Frame(window)
tools_frame.pack(fill=X, padx=5, pady=5)

color_frame = Frame(tools_frame)
color_frame.pack(side=LEFT)

colors = ["red", "green", "blue", "black", "salmon"]
for color in colors:
    lbl = Label(color_frame, text="", bg=color, width=8, height=2,
                relief=RAISED, bd=2)
    lbl.pack(side=LEFT, padx=2)
    lbl.bind("<Button-1>", lambda e, c=color: set_color(c))

width_frame = Frame(tools_frame)
width_frame.pack(side=RIGHT)

Label(width_frame, text="Толщина:").pack(side=LEFT)
width_entry = Entry(width_frame, width=5)
width_entry.pack(side=LEFT, padx=5)
width_entry.insert(0, str(pen_width))

Button(width_frame, text="Установить", command=update_pen_width).pack(side=LEFT)

status_label = Label(window, text=f"Толщина пера: {pen_width}", fg="gray")
status_label.pack(pady=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить изображение", command=load_image)
file_menu.add_command(label="Сохранить изображение", command=save_image)
file_menu.add_separator()
file_menu.add_command(label="Очистить холст", command=clear_canvas)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_app)

window.mainloop()