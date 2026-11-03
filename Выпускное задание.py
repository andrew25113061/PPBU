from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import datetime

# Обновляем название выбранной криптовалюты под Combobox

def update_currency_label(event=None):
    code = combobox.get()
    name = currencies.get(code, code)
    currency_label.config(text=name)

# Сбрасываем старый курс при смене криптовалюты
    price_label.config(text="—")
    updated_label.config(text="")

# Запрашиваем цену у CoinGecko. Возвращаем число или None при ошибке.

def fetch_price(code):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': code, 'vs_currencies': 'usd'}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    if code in data and 'usd' in data[code]:
        return data[code]['usd']
    return None

# Получаем курс и отображаем его в окне

def exchange():
    code = combobox.get()
    if not code:
        mb.showwarning('Ошибка.', 'Выберите криптовалюту')
        return

# Блокируем кнопку на время запроса

    fetch_button.config(state='disabled', text='Загрузка...')

# Принудительно перерисовываем окно

    root.update()

    try:
        price = fetch_price(code)

        if price is None:
            mb.showerror('Ошибка', f'Не удалось получить цену для {code}')
            price_label.config(text='—')
            updated_label.config(text='')
            return

# Отображаем в окне
        price_label.config(text=f"${price:,.6f}")
        now = datetime.datetime.now().strftime('%H:%M:%S')
        updated_label.config(text=f"Обновлено в {now}")

    except requests.exceptions.Timeout:
        mb.showerror('Ошибка', 'Превышено время ожидания запроса')
        price_label.config(text='—')
    except Exception as er:
        mb.showerror('Ошибка', str(er))
        price_label.config(text='—')
    finally:

# Возвращаем кнопку в рабочее состояние
        fetch_button.config(state='normal', text='Получить курс к USD')


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
      bg='snow', font=('Arial', 11)).pack(pady=(15, 5))

crypto_ids = list(currencies.keys())
combobox = ttk.Combobox(root, values=crypto_ids, state='readonly', width=30)
combobox.pack(pady=5)
combobox.bind('<<ComboboxSelected>>', update_currency_label)

# Название выбранной криптовалюты

currency_label = ttk.Label(root, text='', font=('Arial', 10, 'italic'))
currency_label.pack()

# Отображение курса

price_frame = Frame(root, bg='white', bd=1, relief='solid')
price_frame.pack(pady=20, padx=20, fill='x')

# Надпись с ценой

price_label = Label(
    price_frame,
    text='—',
    font=('Arial', 24, 'bold'),
    bg='white',
    fg='green',
)
price_label.pack(pady=(15, 0))

# Подпись валюты

usd_label = Label(
    price_frame,
    text='USD за 1 единицу криптовалюты',
    font=('Arial', 9),
    bg='white',
    fg='gray',
)
usd_label.pack()

# Время обновления

updated_label = Label(
    price_frame,
    text='',
    font=('Arial', 8),
    bg='white',
    fg='gray',
)
updated_label.pack(pady=(0, 15))

# Кнопки

button_frame = Frame(root, bg='snow')
button_frame.pack(pady=10)

fetch_button = Button(
    button_frame,
    text='Получить курс к USD',
    command=exchange,
    font=('Arial', 10, 'bold'),
    bg='forest green',
    fg='white',
    relief='flat',
    padx=15,
    pady=8,
    cursor='hand2',
    activebackground='indigo',
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