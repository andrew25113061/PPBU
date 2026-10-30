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

root.mainloop()
