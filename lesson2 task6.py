# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
my_list = []
a = ['название', 'цена', 'количество', 'eд']
my_dict = dict.fromkeys(a)
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
number = int(input('Введите количество товаров (число): '))
n = 1
i = 0
while n <= number:
    list_tuple = [None, None]
    list_tuple[0] = n
    list_tuple[1] = my_dict
    my_dict['название'] = input('Введите название товара: ')
    my_dict['цена'] = input('Введите цену товара: ')
    my_dict['количество'] = int(input('Введите количество единиц товара: '))
    my_dict['eд'] = 'шт'
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
    import copy
    new_list = copy.deepcopy(list_tuple)
    my_tuple = tuple(new_list)
    my_list.append(my_tuple)
    n += 1
    i += 1
print('\nCтруктура данных «Товары», представляющая собой список кортежей: ', my_list)
print()
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором
# каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
list_final = []
k = 0
while k < len(my_list):
    list_final.append(list(my_list[k]))
    k += 1

dict_final = {}
j = 0
while j < len(list_final):
        b = list_final[j]
        dict_extra = (b[1])
        dict_final.setdefault('название', []).append(dict_extra.get('название', ''))
        dict_final.setdefault('цена', []).append(dict_extra.get('цена', ''))
        dict_final.setdefault('количество', []).append(dict_extra.get('количество', ''))
        dict_final['eд'] = ['шт']
        j += 1
print('\nАналитика о товарах, реализованная в словаре: ', dict_final)