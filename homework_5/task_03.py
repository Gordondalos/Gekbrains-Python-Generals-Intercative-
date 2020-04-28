# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

try:
    with open("text_3.txt") as file:
        data = file.readlines()

except FileNotFoundError:
    print('Файл не найден')

# Создание базы для работы на основе словаря
base = {}
for i in range(len(data)):
    base.update({data[i].split()[0]: float(data[i].split()[1])})

# Рассчет и вывод
print('Список сотрудников с зарплатой меньше 20000:')
sum_salary = 0
for unit, salary in base.items():
    if salary < 20000:
        print(f'- {unit}')
    sum_salary += salary
avg_salary = sum_salary / len(base)
print(f'Средняя зарплата по всей компании: {avg_salary}')
