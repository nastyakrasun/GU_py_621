# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class StockOrgTech:
    def __init__(self, stock_dict):
        #self.stock_dict = {'Название': self.name, 'Количество': self.quantity, 'Цена за шт': self.price, 'Срок службы': self.exploitation}
        self.name = stock_dict['Название']
        self.quantity = stock_dict['Количество']
        self.price = stock_dict['Цена за шт']
        self.exploitation = stock_dict['Срок службы']
# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
    def get_item(self):
        pass

    def send_item(self):
        pass

class OrgTechnics:
    def __init__(self, name, number, price, exploitation):
        self.name = name
        self.number = number
        self.price = price
        self.exploitation = exploitation
        #self.number_of_copies =

    def __str__(self):
        return f'''{self.name}, 
количество: {self.number} (шт), 
цена за штуку: {self.price} (руб), 
общая стоимость: {self.number * self.price} (руб),
полных лет в эксплуатации: {self.exploitation}\n'''

class Printer(OrgTechnics):
    def __init__(self, number_of_copies, level_of_ink):
        #super().__init__(self, number_of_copies, level_of_ink)
        self.copies = number_of_copies
        self.ink = int(level_of_ink)
        self.ink_per_copy = 5

    def do_print(self):
        return f'print {self.copies} copies'

    def short_of_ink(self):
        if self.ink < (self.copies * self.ink_per_copy):
            return ('Low level of ink')

class Scaner(OrgTechnics):
    def go_scanning(self):
        return 'Start scanning'

    def stop_scanning(self):
        return 'Stop scanning'

class Xerox(OrgTechnics):
    def __init__(self, number_of_copies, number_of_sheets):
        super().__init__(self, number_of_copies, number_of_sheets)
        self.copies = number_of_copies
        self.paper = number_of_sheets

    def copy(self):
        return f'make {self.copies} copies'

    def short_of_paper(self):
        if self.paper < self.copies:
            return ('Need more paper')
# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

printer = OrgTechnics('Printer', 5, 3000, 3)
print(printer)
printer = Printer(10, 500)
print(printer.do_print())