# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open('l5_t3.txt', encoding='utf-8') as f:
    words = []
    names = []
    salary = []
    lines = f.readlines()
    for line in lines:
        f.seek(0)
        word = line.split()
        words.append(word[0])
        words.append(word[1])

    n = int(len(words))
    j = 0
    while j < n:
        if j % 2 != 0:
            salary.append(int(words[j]))
        else:
            names.append(words[j])
        j += 1

    i = 0  # Выполнить подсчет средней величины дохода сотрудников.
    total_salary = 0
    while i < n / 2:
        total_salary += salary[i]
        i += 1
    print('средняя величина дохода сотрудников равна: ', total_salary / int(len(salary)))

    dictionary = {}
    i = 0
    while i < n / 2:
        dictionary[names[i]] = salary[i]
        i += 1

    names_min = []
    # min_salary = int(input('Введите минимальный размер оплаты: '))
    min_salary = 20000
    for name, salary in dictionary.items():
        if salary <= min_salary:
            names_min.append(name)
    print('Фамилии сотрудников с окладом меньше 20000: ', names_min)

