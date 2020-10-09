# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
with open('l5_t7.txt', 'r+', encoding='utf-8') as main_file:  # Подсказка: использовать менеджеры контекста.
    firm = main_file.readlines()
    n = 5
    #n = len(firm)
    i = 0
    while i < n:
        firm[i] = (firm[i]).split()
        i += 1
    keys = []
    income = []
    output = []  # нужно убрать точку в конце
    profit = []

    j = 0
    while j < n:
        keys.append((firm[j])[0])
        income.append(int((firm[j])[2]))
        output.append(int((firm[j])[3]))
        j += 1

    k=0
    while k < n:
        profit.append(income[k] - output[k])
        k += 1

    aver_profit = []
    m = 0
    while m < n:  # Если фирма получила убытки, в расчет средней прибыли ее не включать.
        if profit[m] > 0:
            aver_profit.append(profit[m])
            m += 1
        else:
            pass  # как избавиться от заглушки?
            m += 1

    average_profit = 0 / len(aver_profit)
    for value in aver_profit:
        average_profit = (average_profit + value)
    av_prof_val = average_profit / len(aver_profit)

    dictionary_1 = {}
    j = 0
    while j < n:
        dictionary_1[keys[j]] = profit[j]
        j += 1

    dictionary_2 = {}
    dictionary_2['average_profit'] = av_prof_val

    final_list = []
    final_list.append(dictionary_1)
    final_list.append(dictionary_2)
    print(final_list)  # Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

    import json  # Итоговый список сохранить в виде json-объекта в соответствующий файл.

    data = final_list
    main_file.write('\n')
    json.dump(data, main_file)  # Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]