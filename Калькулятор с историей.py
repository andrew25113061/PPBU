add = lambda x, y: x + y
subtract = lambda x, y: x - y      # исправил опечатку в имени
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

HISTORY_FILE = "calculations.txt"

def save_to_history(expression, result):
    """Дописывает одну строку с вычислением в файл."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{expression} = {result}\n")

def show_history():
    """Читает и выводит всю историю из файла. Если файла нет — сообщает, что история пуста."""
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("История вычислений пуста.")
        else:
            print("\n--- История вычислений ---")
            for line in lines:
                print(line.rstrip())  # rstrip убирает лишний перевод строки
            print("------------------------\n")
    except FileNotFoundError:
        print("История вычислений пока не создана (файл не найден).")

while True:
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Показать историю вычислений")
    print("6. Выход")

    choice = input("Введите номер операции (1/2/3/4/5/6): ").strip()

    if choice == "6":
        print("До свидания!")
        break

    if choice == "5":
        show_history()
        continue

    # Для операций 1–4 запрашиваем числа
    if choice in {"1", "2", "3", "4"}:
        try:
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: нужно вводить целые числа.")
            continue

        result = None
        expression = ""

        if choice == "1":
            result = add(num1, num2)
            expression = f"{num1} + {num2}"
        elif choice == "2":
            result = subtract(num1, num2)
            expression = f"{num1} - {num2}"
        elif choice == "3":
            result = multiply(num1, num2)
            expression = f"{num1} * {num2}"
        elif choice == "4":
            if num2 == 0:
                print("Ошибка: деление на ноль невозможно.")
                continue
            result = divide(num1, num2)
            expression = f"{num1} / {num2}"

        print(f"Результат: {expression} = {result}")
        save_to_history(expression, result)
    else:
        print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")