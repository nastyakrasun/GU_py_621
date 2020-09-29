# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [7, 5, 3, 3, 2]
n = len(my_list)
# У пользователя необходимо запрашивать новый элемент рейтинга.
while True:
    try:
        new_elem = int(input('Введите новый элемент рейтинга (натуральное число): '))
        if type(new_elem) == int:
            break
    except ValueError:
        print('Введено не натуральное число')
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
if (new_elem in my_list):
    my_list.insert(my_list.index(new_elem), new_elem)
else:
    i = 0
    while i <= n:
        if new_elem > my_list[i]:
            my_list.insert(i, new_elem)
            break
        i += 1
        if new_elem < my_list[i]:
            my_list.append(new_elem)
        break

print('\nCтруктурa «Рейтинг», представляющая собой не возрастающий набор натуральных чисел\n', my_list)
