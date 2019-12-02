"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
"""
my_list = [20, 7, 8, 6, 13, 10, 9, 15]

# Создаем list comprehension, в которое добавляем условие
my_new_list = [el for el in my_list if el > my_list[my_list.index(el) - 1]]
print(f'Исходный список: {my_list}')
print(f'Новый список: {my_new_list}')