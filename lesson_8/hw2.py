"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class MyError(Exception):
    def __init__(self, txt: str):
        self.txt = txt

    @staticmethod
    def situation(dividend: int, divider: int):
        try:
            if divider == 0:
                raise MyError('Делитель не может быть 0')
            return dividend / divider
        except MyError as err:
            print(err)
        finally:
            print('Программа завершена')


MyError.situation(1, 0)
