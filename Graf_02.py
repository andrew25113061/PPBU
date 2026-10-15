from tkinter import *
from PIL import Image, ImageTk, ImageOps
from tkinter import filedialog as fd
from tkinter import messagebox as mb

pen_color = "black"

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color)

def fit_image_to_canvas(image, canvas_width=600, canvas_height=400):
    img_w, img_h = image.size
    scale_w = canvas_width / img_w
    scale_h = canvas_height / img_h
    scale = min(scale_w, scale_h)
    new_w = int(img_w * scale)
    new_h = int(img_h * scale)
    return image.resize((new_w, new_h), Image.LANCZOS)

def load_image():
    try:
        file_path = fd.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if not file_path:
            return

        image = Image.open(file_path)
        image_resized = fit_image_to_canvas(image, 600, 400)
        image_tk = ImageTk.PhotoImage(image_resized)

        canvas.delete("all")
        canvas.create_image(0, 0, anchor=NW, image=image_tk)
        canvas.image = image_tk
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось загрузить: {e}")

def save_image():
    """Сохраняет ТОЛЬКО содержимое холста без полей, рамок и фона окна."""
    try:
        file_path = fd.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not file_path:
            return

        # 1. Postscript — это «векторный снимок» всего, что нарисовано на Canvas
        ps = canvas.postscript(colormode='color')

        # 2. Конвертируем PostScript в изображение через Pillow
        img = Image.open(ps)

        # 3. Если на холсте есть белый фон (bg="white"), можно его убрать, оставив только рисунок
        # Но если ты хочешь сохранить и фон тоже — просто не используй ImageOps.expand и mask
        # Ниже — вариант, который сохраняет ровно то, что видно на холсте (включая белый фон Canvas),
        # но без рамок окна и лишних полей.
        img.save(file_path, format='PNG')

        mb.showinfo("Сохранено!", "Изображение успешно сохранено без лишних полей!")
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось сохранить: {e}")

def set_color(color):
    global pen_color
    pen_color = color

window = Tk()
window.title("Графический редактор")

# Холст: фиксированный размер, белый фон
canvas = Canvas(window, width=600, height=400, bg="white")
canvas.pack()
canvas.bind("<B1-Motion>", draw)

# Панель цветов
color_frame = Frame(window)
color_frame.pack(fill=X, padx=5, pady=5)

colors = ["red", "green", "blue", "black"]
for color in colors:
    lbl = Label(color_frame, text="", bg=color, width=8, height=2)
    lbl.pack(side=LEFT, padx=2)
    lbl.bind("<Button-1>", lambda e, c=color: set_color(c))

# Панель кнопок
btn_frame = Frame(window)
btn_frame.pack(fill=X, padx=5, pady=5)

Button(btn_frame, text="Загрузить изображение", command=load_image).pack(side=LEFT, padx=5)
Button(btn_frame, text="Сохранить холст", command=save_image).pack(side=LEFT, padx=5)

window.mainloop()

