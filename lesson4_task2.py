# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
given = [int(i) for i in input().split()]
# given = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]  # Пример исходного списка
result2 = [given[i] for i in range(1, len(given)) if given[i] > given[i - 1]]
print(result2)