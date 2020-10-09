# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
with open('l5_t6.txt', 'r+', encoding='utf-8') as main_file:
    lines = main_file.readlines()
    n = len(lines)
    i = 0
    keys = []
    values = []
    sum_values = []
    dictionary = {}
    while i < n:
        keys.append((lines[i].split(':'))[0])
        values.append((lines[i].split(':'))[1])
        i += 1

    for value in values:
        import re  # чтобы вывести все цифры из строки. Где импортировать - в самом начале программы, после with open...?
        val_str = str(value)
        result_list = re.findall(r'\d+', val_str)  # чтобы вывести все цифры из строки
        k = 0
        sum = 0
        while k < len(result_list):
            sum = sum + int(result_list[k])
            k += 1
        sum_values.append(sum)

    j = 0  # Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
    while j < n:
        dictionary[keys[j]] = sum_values[j]
        j += 1
    print('dictionary: ', dictionary)

    main_file.write('\nCловарь, содержащий название предмета и общее количество занятий по нему: \n')
    main_file.write(str(dictionary))
