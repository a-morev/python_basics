"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по
этому предмету и их количество. Важно, чтобы для каждого предмета не
обязательно были все типы занятий. Сформировать словарь, содержащий название
предмета и общее количество занятий по нему. Вывести словарь на экран.
"""

# Функция делит список по символам и суммирует цифры из этого списка


def sum_from_string(value: str):
    value_split = (val.split('(') for val in value.split(' '))
    value_digit = (int(val) for val_ar in value_split for val in val_ar if val.isdigit())
    return sum(value_digit)


with open('for_hw6.txt', 'r', encoding='utf-8') as file:
    lessons = file.readlines()
    # Генератор, делящий строки по разделителю
    lessons_split = (line.split(':') for line in lessons)
    # Собираем словарь
    lessons = {
        lesson_name: sum_from_string(les_hours) for lesson_name, les_hours in lessons_split
    }
    print(lessons)
