t = {
    "кошка": "cat",
    "собака": "dog",
    "зима": "winter",
    "слово": "word",
    "мир": "world"
    }

w = input("Введите слово: ").lower()
try:
# w in t:
          print(f"Перевод слова: '{w}' : '{t[w]}'")
#else:
except KeyError:
          print("Такого слова нет в словаре")
