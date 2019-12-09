"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""

try:
    with open('for_hw5.txt', 'w+', encoding='utf-8') as f_obj:
        line = input('Введите числа через пробел: ').split(' ')
        f_obj.writelines(line)
        content = f_obj.read()
        print(sum(map(int, content)))

except IOError:
    print('Ошибка ввода-вывывода')

except ValueError:
    print('Введено не число.')
