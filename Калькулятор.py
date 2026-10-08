def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    if y == 0:
        return ("Ошибка! Деление на ноль.")
    else:
        return x / y

print(add(7, 8))
print(subtract(25, 8))
print(multiply(7, 8))
print(divide(100, 4))
