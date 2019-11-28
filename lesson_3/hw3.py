"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""


def my_func():
    numbers = []  # Здесь будут храниться запрашиваемые цифры
    max_num = []  # Здесь будут храниться 2 максимальные цифры
    # Цикл реализует запрос только 3 цифр
    for i in range(3):
        number = int(input('Введите число: '))
        numbers.append(number)

    while True:
        # Добавление в список max_num макс. числа из списка numbers
        max_num.append(max(numbers))
        # Удаление проверенного числа списка numbers
        numbers.remove(max(numbers))
        # Выход из цикла
        if len(max_num) == 2:
            break
    return sum(max_num)


print(my_func())