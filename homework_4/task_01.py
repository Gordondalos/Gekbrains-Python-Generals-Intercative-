# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv


def salary(hours, cost, prize):
    # Функция определения зарплаты
    try:
        return int(hours) * int(cost) + int(prize)
    except ValueError:
        return "Arguments must be numbers!"


script, hours, cost, prize = argv
print(salary(hours, cost, prize))
