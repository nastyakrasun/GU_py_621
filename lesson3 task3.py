# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def sum_of_max():
    my_list = []
    for i in range (1, 4):
        arg = int(input(f'Введите {i}-й аргумент: '))
        my_list.append(arg)
    print("Список аргументов: ", my_list)
    k = 1
    while k < len(my_list):
        max_1 = my_list[0]
        if max_1 < my_list[k]:
            max_1 = my_list[k]
        k += 1
    j= 0
    while j < len(my_list):
        if max_1 == my_list[j]:
            del my_list[j]
        j += 1
    k = 1
    while k < len(my_list):
        max_2 = my_list[0]
        if max_2 < my_list[k]:
            max_2 = my_list[k]
        k += 1
    result = max_1 + max_2
    print('Cумма наибольших двух аргументов равна: ', result)
    return result

sum_of_max()



