# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name.title()
        self.is_police = is_police

    def go(self):
        print('машина поехала')
    def stop(self):
        print('машина остановилась')
    def turn(self, direction):
        print('машина повернула ', direction)
    def show_speed(self):
        print('текущая скорость автомобиля: ', self.speed)

class TownCar(Car):
    def show_speed(self):
        print('текущая скорость автомобиля: ', self.speed)
        if self.speed > 60:
            print('Внимание! Превышение скорости!')

class SportCar(Car):
    def max_speed(self):
        print('Максимально допустимая скорость: 200км/ч')

class WorkCar(Car):
    def show_speed(self):
        print('текущая скорость автомобиля: ', self.speed)
        if self.speed > 40:
            print('Внимание! Превышение скорости!')

class PoliceCar(Car):
    def on_duty(self):
        print('Автомобиль находится на задании')

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
t = TownCar(70, 'navy', 'peugeot', 'is_police')
t.go()
t.show_speed()
p = PoliceCar(100, 'white', 'renault', 'is_police')
print(p.name)
p.on_duty()
p.turn('налево')