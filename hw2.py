"""
Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
time = int(input('Введите время в секундах: '))
hours = time // 3600  # переводим сек в ч
minutes = time % 3600 // 60  # переводим сек в мин
seconds = time % 3600 % 60  # дописываем остаток в сек
full_time = f'{hours} : {minutes} : {seconds}'
print(full_time)
