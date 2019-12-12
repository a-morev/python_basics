"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для
каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры
классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):  # Переопределение метода
        print(f'ручкой нарисовали годный {self.title}!')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):  # Переопределение метода
        print(f'{self.title} мастер-класс!')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):  # Переопределение метода
        print(f'{self.title} накидана маркером!')


major = Stationery('кисть')
major.draw()

picture_1 = Pen('скетч')
picture_1.draw()

picture_2 = Pencil('шарж')
picture_2.draw()

picture_3 = Handle('схема')
picture_3.draw()
