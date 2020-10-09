# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
with open('l5_t5.txt', 'w+', encoding='utf-8') as write_file:
    text = input('Введите набор чисел, разделённых пробелами: ')
    write_file.write(text)
# Программа должна подсчитывать сумму чисел в файле
    number = text.split()
    n = len(number)
    numbers = []
    i = 0
    sum = 0
    while i < n:
        numbers.append(int(number[i]))
        sum = sum + numbers[i]
        i += 1
    print('Сумма введённых чисел: ', sum)  # и выводить ее на экран - экран текстового файла?
    write_file.write('\nСумма введённых чисел: ')
    write_file.write(str(sum))