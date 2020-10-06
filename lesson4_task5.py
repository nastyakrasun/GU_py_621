# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
from functools import reduce  # Подсказка: использовать функцию reduce().
# Необходимо получить результат вычисления произведения всех элементов списка.
def reducer_func(elem_prev, elem):
    return elem_prev * elem
# В список должны войти чётные числа от 100 до 1000 (включая границы).
result5 = [elem for elem in range(100, 1001) if elem % 2 == 0]
print(reduce(reducer_func, result5))