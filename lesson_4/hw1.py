"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv  # Импортирую функцию argv из sys

_, production, rate, prize = argv  # Параметры вводимые в терминал

# Функция расчета заработной платы сотрудника


def salary_man(param_1, param_2, param_3):
    if param_1.isdigit() and param_2.isdigit() and param_3.isdigit():
        param_1 = int(param_1)
        param_2 = int(param_2)
        param_3 = int(param_3)
        result = param_1 * param_2 + param_3
        return result


print("Выработка в часах: ", production)
print("Ставка в час: ", rate)
print("Премия: ", prize)
print(f'Зарплата сотрудника составляет: {salary_man(production, rate, prize)}')
