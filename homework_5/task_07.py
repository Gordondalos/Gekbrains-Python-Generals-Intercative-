# 7. Необходимо построчно прочитать файл text_7.txt, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

# Чтение данных из файла
try:
    with open("text_7.txt", encoding='utf-8') as file:
        data = file.readlines()

except FileNotFoundError:
    print('Файл не найден')

# Создание базы для работы на основе списка
companies = []
for i in range(len(data)):
    companies.append(data[i].split())

# Обработка
summary = {}
profits_sum = 0
for company in companies:
    key = company[0]
    profit = int(company[2]) - int(company[3])
    summary.update({key: profit})

    if profit > 0:  # учитываем только положительную прибыль в рассчете средней
        profits_sum += profit

profit_avg = round(profits_sum / len(companies))
lst_to_export = [summary, {"average_profit": profit_avg}]

# Запись в JSON
with open("my_file.json", "w", encoding='utf-8') as json_file:
    json.dump(lst_to_export, json_file)
