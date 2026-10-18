# Знакомство с библиотеками OS и shutil
# Вывод списка файлов директории в консоль

from tkinter import *
from tkinter import filedialog as fd
import os

# Создание корневого окна и скрытие его
window = Tk()
window.withdraw()

# Открытие диалогового окна для выбора директории
dir = fd.askdirectory()

# Если директория была выбрана, выводим список файлов
if dir:
    for file in os.listdir(dir):
        print(file)


