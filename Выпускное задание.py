from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import datetime


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

# Выбор криптовалюты
Label(root, text='Выберите криптовалюту',
      font=('Arial', 11)).pack(pady=(15, 5))

crypto_ids = list(currencies.keys())
combobox = ttk.Combobox(root, values=crypto_ids, state='readonly', width=30)
combobox.pack(pady=5)

root.mainloop()