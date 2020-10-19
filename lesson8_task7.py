# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.re = real
        self.im = imaginary

    def __str__(self):  # запускается на вывод в консоль в принте
        return f'{self.re} + {self.im}i'

    def __add__(self, other):
        return f'{self.re + other.re} + {self.im + other.im}i'

    def __sub__(self, other):
        return f'{self.re - other.re} + {self.im - other.im}i'

    def __mul__(self, other):
        return f'{self.re * other.re - self.im * other.im} + {self.re * other.im + self.im * other.re}i'

a = ComplexNumber(2, 5)
b = ComplexNumber(1, 2)
print(a + b)
print(a - b)
print(a * b)