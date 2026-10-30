from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


# Обновление подписей под комбобоксами — названия выбранных валют.

def update_currency_labels(event=None):
    code1 = base1_combobox.get()
    code2 = base2_combobox.get()
    target = target_combobox.get()

    base1_label.config(text=f"{currencies.get(code1, code1)}")
    base2_label.config(text=f"{currencies.get(code2, code2)}")
    target_label.config(text=f"{currencies.get(target, target)}")


def exchange():
    """Запрашивает курсы двух базовых валют к целевой и показывает оба сразу."""
    target = target_combobox.get()
    base1 = base1_combobox.get()
    base2 = base2_combobox.get()

    if not (target and base1 and base2):
        mb.showwarning("Внимание", "Выберите целевую и обе базовые валюты")
        return

    if base1 == base2:
        mb.showwarning("Внимание", "Базовые валюты должны различаться")
        return

    try:
        response = requests.get(
            "https://open.er-api.com/v6/latest/USD", timeout=10)
        response.raise_for_status()
        data = response.json()
        rates = data["rates"]

        for code in (target, base1, base2):
            if code not in rates:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
                return

        # Кросс-курс: 1 базовая = (rate_target / rate_base) целевой
        cross1 = rates[target] / rates[base1]
        cross2 = rates[target] / rates[base2]

        name_t = currencies.get(target, target)
        name_1 = currencies.get(base1, base1)
        name_2 = currencies.get(base2, base2)

        mb.showinfo(
            "Курсы обмена",
            f"1 {name_1} = {cross1:.4f} {name_t}\n"
            f"1 {name_2} = {cross2:.4f} {name_t}",
        )
    except requests.exceptions.Timeout:
        mb.showerror("Ошибка", "Превышено время ожидания запроса")
    except Exception as er:
        mb.showerror("Ошибка", str(er))


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
base1_combobox.bind("<<ComboboxSelected>>", update_currency_labels)
base1_label = ttk.Label(root, text="")
base1_label.pack()

# Базовая валюта 2

Label(root, text="Вторая базовая валюта").pack(pady=(30, 0))
base2_combobox = ttk.Combobox(
    root, values=list(currencies.keys()), state="readonly"
)
base2_combobox.set("EUR")
base2_combobox.pack(pady=15)
base2_combobox.bind("<<ComboboxSelected>>", update_currency_labels)

base2_label = ttk.Label(root, text="")
base2_label.pack()

# Целевая валюта

Label(root, text="Целевая валюта").pack(pady=(30, 0))
target_combobox = ttk.Combobox(
    root, values=list(currencies.keys()), state="readonly"
)
target_combobox.set("RUB")
target_combobox.pack(pady=15)
target_combobox.bind("<<ComboboxSelected>>", update_currency_labels)

target_label = ttk.Label(root, text="")
target_label.pack()

Button(
    root,
    text="Получить курс обмена",
    command=exchange,
).pack(pady=40)


update_currency_labels()


root.mainloop()
