# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))

if revenue > costs:
    profit = revenue - costs
    print(f'Прибыль {profit}')
    print(f'Рентабельность выручки: {(profit) / revenue}')
    staff = int(input('Введите численность сотрудников: '))
    print(f'Прибыль в рассчете на 1 сотрудника: {profit / staff}')
elif revenue < costs:
    print(f'Убыток {costs - revenue}')
else:
    print('В ноль')
