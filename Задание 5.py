from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


currencies = {
    "USD": "Доллар США",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Английский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум",
}



root = Tk()
root.title("Курс обмена валют")
root.geometry("360x500")


# Базовая валюта 1

Label(root, text="Базовая валюта").pack(pady=(30, 0))
base1_combobox = ttk.Combobox(
    root, values=list(currencies.keys()), state="readonly"
)
base1_combobox.set("USD")
base1_combobox.pack(pady=15)

base1_label = ttk.Label(root, text="")
base1_label.pack()

# Базовая валюта 2

Label(root, text="Вторая базовая валюта").pack(pady=(30, 0))
base2_combobox = ttk.Combobox(
    root, values=list(currencies.keys()), state="readonly"
)
base2_combobox.set("EUR")
base2_combobox.pack(pady=15)

base2_label = ttk.Label(root, text="")
base2_label.pack()

# Целевая валюта

Label(root, text="Целевая валюта").pack(pady=(30, 0))
target_combobox = ttk.Combobox(
    root, values=list(currencies.keys()), state="readonly"
)
target_combobox.set("RUB")
target_combobox.pack(pady=15)

target_label = ttk.Label(root, text="")
target_label.pack()




root.mainloop()
