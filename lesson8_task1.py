# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import datetime

class Data:
    def __init__(self):
        # self.day = int(input('day'))
        # self.month = int(input('month'))
        # self.year = int(input('year'))
        # self.data = datetime.date(self.day, self.month, self.year)
        self.data = datetime.date.today()

    @classmethod
    def turn_to_number(cls, data):  # Метод класса, ссылается сначала на класс
        data_list = str(data).split('-')
        # day = int(data_list[0])
        # month = int(data_list[1])
        # year = int(data_list[2])
        day = int(data_list[2])
        month = int(data_list[1])
        year = int(data_list[0])
        print(day, type(day), month, type(month), year, type(year))
        return(cls, data)

    @staticmethod
    def validation_of_date(data):

        print('pass')

    def __str__(self):
        return f'{self.data}'

data = Data()
print(data)
Data.turn_to_number(data)