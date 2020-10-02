# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
def division(a, b):
    return a / b

while True:  # Числа запрашивать у пользователя
    try:
        a = int(input('Введите делимое (число): '))
        if type(a) == int:
            break
    except ValueError:
        print('Введено не число')
while True:
    try:
        b = int(input('Введите делитель, отличный от нуля: '))
        if type(b) == int:
            if b != 0:  # предусмотреть обработку ситуации деления на ноль.
                break
            else:
                print('Делитель не может быть нулём')
    except ValueError:
        print('Введено не число')

print(round(division(a, b), 1))