# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name.title()
        self.surname = surname.title()
        self.position = position
        self.wage = wage
        self.bonus = bonus
        dictionary = {}
        dictionary['wage'] = self.wage
        dictionary['bonus'] = self.bonus
        self._income = dictionary.get('wage')  # как элемент должен ссылаться на словарь - непонятно. где должен быть словарь - ? (тоже непонятно) вывела словарь в начало

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.wage + self.bonus

a = Position('лена', 'петрова', 'прораб', 50000, 15000)
print(a.name)
print('полное имя: ', a.get_full_name())
print('оклад + премия: ', a.get_total_income())