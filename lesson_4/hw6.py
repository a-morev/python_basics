"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного.
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного
заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
# Пункт а
# Импортируем ф-ии count и cycle
from itertools import count, cycle


def my_count_func(start_number, end_number):
    # Создаю бесконечный итератор, генерирующий целые числа
    for el in count(start_number):
        # Ввожу условие обрыва цикла
        if el > end_number:
            break
        else:
            print(el)


start_num = int(input('Введите начальное значение: '))
end_num = int(input('Введите конечное значение: '))
my_count_func(start_num, end_num)

# Пункт б
my_list = [True, 'ABC', 123, ]


def my_cycle_func(i):
    # Создаю бесконечный итератор, повторяющий элементы списка
    _ = 0
    for el in cycle(my_list):
        # Ввожу условие обрыва цикла
        if _ > i:
            break
        print(el)
        _ += 1


iteration = int(input('Число итераций: '))
my_cycle_func(iteration)
