def get_number(prompt):
    while True:
        value = input(prompt)
        if value.lstrip("-").isdigit():
            return int(value)
        else:
            print("Это не целое число. Пожалуйста, введите целое число.")


add = lambda x, y:x + y
subtruct = lambda x, y:x - y
multiply = lambda x, y:x * y
divide = lambda x, y: "Ошибка. Деление на ноль!" if y ==0 else x / y


            

#def add(x, y):
#   return x + y


#def subtruct(x, y):
#    return x - y

#def multiply(x, y):
#    return x * y

#def divide(x, y):
#    if y == 0:
#        return ("Ошибка. Деление на ноль")
#    else:
#        return x / y


print("Выберите операцию: ")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

valid_choices = ['1', '2', '3', '4']
choice = None

while choice not in valid_choices:
    choice = input("Введите номер операции (1/2/3/4): ")
    if choice not in valid_choices:
        print("Неверный ввод. Пожалуйста, выберите 1, 2, 3 или 4.")
        

num1 = get_number("Введите первое число: ")
num2 = get_number("Введите второе число: ")

if choice == '1':
    print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"Результат: {num1} - {num2} = {subtruct(num1, num2)}")
elif choice == '3':
    print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    result = divide(num1, num2)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Результат: {num1} / {num2} = {result:.2f}")
else:
    print("Неверный ввод")





    


