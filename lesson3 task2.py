# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
# с пом **kwargs сказал делать
def info(name, surname, city, email, birth_year, number):
    answer = print(f'имя: {name.title()}, фамилия: {surname.title()}, год рождения: {birth_year}, город проживания: {city.title()}, email: {email}, телефон: {number}')
    return answer

name = input('Введите имя пользователя: ')
surname = input('Введите фамилию пользователя: ')
city = input('Введите город проживания пользователя: ')
email = input('Введите email пользователя: ')
birth_year = input('Введите год рождения пользователя: ')
number = input('Введите номер телефона пользователя: ')

info(name, surname, city, email, birth_year, number)