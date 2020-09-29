# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = []
n = int(len(my_list))
num = int(input('Введите число элементов в списке: '))
while n < num:
    a = input('Введите элемент списка: ')
    my_list.append(a)
    n = int(len(my_list))
print('Введён список: ', my_list)
# При нечетном количестве элементов последний сохранить на своем месте.
if n % 2 != 0:
    last_elem = my_list.pop()
    my_list == my_list.pop
    my_list_odd = my_list[::2]
    my_list_even = my_list[1::2]
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
    my_list.append(last_elem)
else:
    my_list_odd = my_list[::2]
    my_list_even = my_list[1::2]
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]

print('Cписок с обменом значений соседних элементов: ', my_list)
