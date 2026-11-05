from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import datetime


# Обновляем название выбранной криптовалюты под Combobox.
def update_currency_label(event=None):
    code = combobox.get()
    name = currencies.get(code, code)
    currency_label.config(text=name)


currencies = {
    'bitcoin': 'Bitcoin (BTC)',
    'ethereum': 'Ethereum (ETH)',
    'bitway': 'Bitway (BTW)',
    'ripple': 'Ripple (XRP)',
    'cardano': 'Cardano (ADA)',
    'solana': 'Solana (SOL)',
    'dogecoin': 'Dogecoin (DOGE)',
    'tether': 'Tether (USDT)',
    'zcash': 'Zcash (ZEC)',
}


root = Tk()
root.title('Курс криптовалют к USD')
root.geometry('420x360')
root.configure(bg='#f5f5f5')

# Выбор криптовалюты
Label(root, text='Выберите криптовалюту',
      bg='#f5f5f5', font=('Arial', 11)).pack(pady=(15, 5))

crypto_ids = list(currencies.keys())
combobox = ttk.Combobox(root, values=crypto_ids, state='readonly', width=30)
combobox.pack(pady=5)
combobox.bind('<<ComboboxSelected>>', update_currency_label)

# Название выбранной криптовалюты
currency_label = ttk.Label(root, text='', font=('Arial', 10, 'italic'))
currency_label.pack()

# Отображение курса
price_frame = Frame(root, bg='#ffffff', bd=1, relief='solid')
price_frame.pack(pady=20, padx=20, fill='x')

# Надпись с ценой
price_label = Label(
    price_frame,
    text='—',
    font=('Arial', 24, 'bold'),
    bg='#ffffff',
    fg='#2e7d32',
)
price_label.pack(pady=(15, 0))

# Подпись валюты
usd_label = Label(
    price_frame,
    text='USD за 1 единицу криптовалюты',
    font=('Arial', 9),
    bg='#ffffff',
    fg='gray',
)
usd_label.pack()

# Время обновления
updated_label = Label(
    price_frame,
    text='',
    font=('Arial', 8),
    bg='#ffffff',
    fg='gray',
)
updated_label.pack(pady=(0, 15))

# Кнопки
button_frame = Frame(root, bg='#f5f5f5')
button_frame.pack(pady=10)

fetch_button = Button(
    button_frame,
    text='Получить курс к USD',
    font=('Arial', 10, 'bold'),
    bg='forest green',
    fg='white',
    relief='flat',
    padx=15,
    pady=8,
    cursor='hand2',
    activebackground='black',
    activeforeground='white',
)
fetch_button.pack(side=LEFT, padx=5)


def exit_app():
    root.destroy()


exit_button = Button(
    button_frame,
    text='Выход',
    command=exit_app,
    font=('Arial', 10),
    bg='lightgray',
    fg='black',
    relief='raised',
    padx=15,
    pady=8,
    cursor='hand2',
    activebackground='lightgray',
)
exit_button.pack(side=LEFT, padx=5)

root.mainloop()