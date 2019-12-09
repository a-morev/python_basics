"""
Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а
также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли
ее не включать. Далее реализовать список. Он должен содержать словарь с
фирмами и их прибылями, а также словарь со средней прибылью. Если фирма
получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}]. Итоговый список сохранить в виде json-объекта в
соответствующий файл. Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
import json


profit = {}
pr = {}
prof = 0
prof_average = 0
i = 0
with open('for_hw7.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        name, firm, earning, costs = line.split()
        profit[name] = int(earning) - int(costs)
        if profit.setdefault(name) > 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_average = prof / i
        print(f'Прибыль средняя - {prof_average:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_average, 2)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('for_hw7.json', 'w', encoding='utf-8') as j_obj:
    json.dump(profit, j_obj)

json_obj = json.dumps(profit)
print(f'Создан json-файл со следующим содержимым: \n '
      f' {json_obj}')