# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list(list_of_lists)
        self.row_length = len(self.matrix)
        self.column_length = len(self.matrix[0])
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    def __str__(self):
        return '\n'.join('\t'.join(map(str, list_i)) for list_i in self.matrix)
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
    def __add__(self, other):
        if self.row_length == other.row_length and self.column_length == other.column_length:
            result = []
            for i in range(self.row_length) and range(other.row_length):
                for j in range(self.column_length) and range(other.column_length):
                    res_of_sum = (self.matrix[i])[j] + (other.matrix[i])[j]
                    result.append(res_of_sum)

            k = len(result)
            result_matrix = []
            while k >= self.row_length:
                result_matrix.append(list(result[0:self.row_length]))
                del result[0:self.row_length]
                k = k - self.row_length
            return Matrix(result_matrix)  # Результатом сложения должна быть новая матрица.

        else:
            return 'Введёные матрицы имеют разные размерности\n         СЛОЖЕНИЕ НЕВОЗМОЖНО'

m1 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
m2 = Matrix([[3, 3, 3], [4, 4, 4], [5, 5, 5]])
m3 = Matrix([[1, 1], [2, 2]])
print('Matrix 1')
print(m1)
print('Matrix 2')
print(m2)
print('Matrix 3')
print(m3)
m4 = m1 + m2
print('Matrix 1 + Matrix 2')
print(m4)
m5 = m1 + m3
print('Matrix 1 + Matrix 3')
print(m5)