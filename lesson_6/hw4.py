"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""
from random import choice


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self):  # Направление поворота случайное
        direction = choice(['направо', 'налево'])
        print(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'Текущая скорость - {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):  # Переопределение функции
        if self.speed > 60:
            print('Превышена допустимая скорость, сбавьте до 60')
        else:
            print(f'Текущая скорость - {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):  # Переопределение функции
        if self.speed > 40:
            print('Превышена допустимая скорость, сбавьте до 40')
        else:
            print(f'Текущая скорость - {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


# Примеры экземпляров классов
citizen_car = TownCar(70, 'red', 'Volvo', False)
print(citizen_car.color)
print(citizen_car.name)
print(citizen_car.is_police)
citizen_car.go()
citizen_car.turn()
citizen_car.show_speed()
citizen_car.stop()

rich_car = SportCar(120, 'black', 'Porsche', False)
print(rich_car.color)
print(rich_car.name)
print(rich_car.is_police)
rich_car.go()
rich_car.turn()
rich_car.show_speed()
rich_car.stop()

bulldozer = WorkCar(45, 'yellow', 'Cat', False)
print(bulldozer.color)
print(bulldozer.name)
print(bulldozer.is_police)
bulldozer.go()
bulldozer.turn()
bulldozer.show_speed()
bulldozer.stop()

policeman = PoliceCar(35, 'blue', 'Ford', True)
print(policeman.color)
print(policeman.name)
print(policeman.is_police)
policeman.go()
policeman.turn()
policeman.show_speed()
policeman.stop()
