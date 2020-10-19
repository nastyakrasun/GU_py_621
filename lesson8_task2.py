# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = int(input("Введите делимое: "))

try:
    b = int(input("Введите делитель: "))
    if b == 0:
        raise OwnError('Деление на ноль!')
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    result = a / b
    print(f'Результат: {result}')