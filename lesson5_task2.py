# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк  --> l5_t2.txt
with open('l5_t2.txt', encoding='utf-8') as f:
    str = 0
    words = []
    lines = f.readlines()
    for line in lines:  # выполнить подсчет количества строк
        f.seek(0)
        str += 1
        word = line.split()
        words.append(int(len(word)))
    i = 1
    sum = words[0]
    for value in words:  # количества слов в каждой строке
        while i < int(len(words)):
            sum += words[i]
            i += 1
print('Количество строк: ', str)
print('Количество слов: ', sum)