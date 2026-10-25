from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_currency_label(event):
    code = combobox.get()
    name = currencies.get(code, code)
    currency_label.config(text=name)


def exchange():
    code = combobox.get()
    if not code:
        mb.showwarning('Внимание', 'Выберите криптовалюту')
        return

    try:
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {'ids': code, 'vs_currencies': 'usd'}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if code in data and 'usd' in data[code]:
            price = data[code]['usd']
            name = currencies.get(code, code)
            mb.showinfo('Цена', f'1 {name} = ${price:,.6f} USD')
        else:
            mb.showerror('Ошибка', f'Не удалось получить цену для {code}')
    except requests.exceptions.Timeout:
        mb.showerror('Ошибка', 'Превышено время ожидания запроса')
    except Exception as er:
        mb.showerror('Ошибка', str(er))


currencies = {
    'bitcoin': 'Bitcoin (BTC)',
    'ethereum': 'Ethereum (ETH)',
    'binancecoin': 'BNB',
    'ripple': 'XRP',
    'cardano': 'Cardano (ADA)',
    'solana': 'Solana (SOL)',
    'dogecoin': 'Dogecoin (DOGE)',
}

root = Tk()
root.title('Курс криптовалют к USD')
root.geometry('360x180')

Label(root, text='Выберите криптовалюту').pack(pady=10, padx=10)

crypto_ids = list(currencies.keys())
combobox = ttk.Combobox(root, values=crypto_ids, state='readonly')
combobox.pack(pady=10, padx=10)
combobox.bind('<<ComboboxSelected>>', update_currency_label)

currency_label = ttk.Label(root, text='')
currency_label.pack()

Button(text='Получить курс к USD', command=exchange).pack(pady=10, padx=10)

root.mainloop()