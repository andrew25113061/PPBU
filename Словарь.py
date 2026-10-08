t = {
    "кошка": "cat"
    "собака": "dog"
    "зима": "winter"
    }

w = input("Введите слово: ".lower()


if w in t:
          print(f"Перевод слова: '{w}' : '{t(w)}'")
        else:
            print("Такого слова нет в словаре")
