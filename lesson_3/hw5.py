"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа
вводится специальный символ, выполнение программы завершается. Если
специальный символ введен после нескольких чисел, то вначале нужно
добавить сумму этих чисел к полученной ранее сумме и после этого завершить
программу.
"""
my_sum = 0  # Здесь будет вычисляться сумма
try:
    # Создан бесконечный цикл
    while True:
        # В цикле for переводим каждый элемент в число функцией map
        for number in map(int, input('Вводите числа через пробел. Введите букву для выхода:\n').split(' ')):
            # Суммирование всех элементов
            my_sum += number
        print(my_sum)
except ValueError:
    # Обрыв цикла и выход при вводе символа
    print(my_sum)