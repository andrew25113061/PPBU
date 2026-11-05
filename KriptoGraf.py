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
root.configure(bg='white')

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

root.mainloop()