filename = "proba.txt"

# Сначала записываем
#try:
#   with open(filename, "w", encoding="utf-8") as f:
#        f.write("Новый пробный текст.")
#    print("Файл успешно записан.")
#except OSError as e:
#    print(f"Ошибка при записи: {e}")
#else:
    # Потом читаем
#    try:
#        with open(filename, "r", encoding="utf-8") as f:
#            content = f.read()
#            print("Содержимое файла:")
#            print(content)
#    except OSError as e:
#        print(f"Ошибка при чтении: {e}")

def count(file_name):
    try:
        with open(file_name, encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

words = count("proba.txt")
print(f"Количество слов в файле: {words}")
