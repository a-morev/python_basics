"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для формирования
матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде. Далее реализовать перегрузку метода add() для реализации
операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения
должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д.
"""

from random import randint


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str('\n'.join(['\t'.join([str(idx) for idx in row]) for row in self.data]))

    def __add__(self, other):
        result = []  # Получаем результ сложения матриц
        numbers = []
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                sum_matrix = self.data[i][j] + other.data[i][j]
                numbers.append(sum_matrix)
                if len(numbers) == len(self.data[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


# Пример реализации объекта
# Матрица 3 на 3 будет генерироваться с помощью генератора
matrix = [[randint(0, 9) for i in range(3)] for i in range(3)]
a1 = Matrix(matrix)
a2 = Matrix(matrix)
print(a1)
print(a2)
print(a1 + a2)
