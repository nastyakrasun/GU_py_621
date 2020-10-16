# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
class Clothes:
    def __init__(self, size, height):
        self.wishes = []
        self.size = size
        self.height = height
    def __add__(self, other): # реализуется добавление элементов в класс
        self.wishes.append(other)

    def __str__(self):  # запускается на вывод в консоль в принте общем
        return f'wishes on clothes: {self.wishes}'

    def tissue_coat(self):
            return f'расход ткани на пальто: {round(self.size / 6.5 + 0.5)}'

    def tissue_suit(self):
            return f'расход ткани на костюм: {round(2 * self.height + 0.3)}'

    @property
    def tissue_total(self):
        return f'расход ткани вместе на пальто и костюм: {round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3))}'

class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def __str__(self):  # запускается на вывод в консоль в принте для Coat
        return f'пальто должно быть: {self.wishes}'

class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def __str__(self):  # запускается на вывод в консоль в принте для Suit
        return f'костюм должен быть: {self.wishes}'

coat = Coat(42, 1.7)
wish1 = 'красное'
wish2 = 'длинное'
coat + wish1
coat + wish2
suit = Suit(36, 1.30)
wish3 = 'тёплый'
wish4 = 'шерстяной'
suit + wish3
suit + wish4
print(coat)
print(suit)
print(coat.tissue_coat())
print(coat.tissue_suit())
print(suit.tissue_coat())
print(suit.tissue_suit())
print(coat.tissue_total)
print(suit.tissue_total)