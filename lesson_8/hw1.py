"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен
проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить
работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_string: str):
        self.date_string = date_string

    @classmethod
    def digit_date(cls, date_string):
        my_date = date_string.split('-')
        return list(map(int, my_date))

    @staticmethod
    def valid_date(date_string: str):
        my_date = list(map(int, date_string.split('-')))
        validator = ['Число', 'Месяц', 'Год']
        return dict(zip(validator, my_date))


print(Date.digit_date('1-12-2019'))
print(Date.valid_date('1-12-2019'))
