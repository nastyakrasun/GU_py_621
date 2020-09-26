number = int(input('Введите положительное целое число: '))
max = 0
while number:
    digit = number % 10
    number = number // 10
    if digit > max:
        max = digit
print(max)

