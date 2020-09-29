# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
month_number = int(input('Введите номер месяца в виде целого числа от 1 до 12: '))
while month_number < 1 or month_number > 12:
    print('Введено некорректное значение')
    month_number = int(input('Введите номер месяца в виде целого числа от 1 до 12: '))
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Решение через list.
print('\nРешение через list')
season = ['зима', 'весна', 'лето', 'осень']
if month_number > 2 and month_number < 6:
    print('Месяц относится к времени года: ', season[1])
elif month_number > 5 and month_number < 9:
    print('Месяц относится к времени года: ', season[2])
elif month_number > 8 and month_number < 12:
    print('Месяц относится к времени года: ', season[3])
else:
    print('Месяц относится к времени года: ', season[0])
# Решение через dict.
print('\nРешение через dict')
months = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
find_months = dict((v, k) for k, vals in months.items() for v in vals)
print('Месяц относится к времени года: ', find_months.get(month_number))