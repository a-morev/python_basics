"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

# Открываем файл на запись
with open('file.txt', 'w') as f_obj:
    # Создаем цикл, куда заносим данные
    while True:
        line = input('Введите текст: ')
        # Условие для обрыва цикла
        if line == '':
            break
        # Записываем список строк в файл
        f_obj.write(f'{line}\n')