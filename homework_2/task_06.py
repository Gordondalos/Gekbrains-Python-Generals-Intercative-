# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# catalog = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'единицы': 'шт'}),
# (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'единицы': 'шт'}),
# (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'единицы': 'шт'})]

properties = {'название': 'str', 'цена': 'int', 'количество': 'int', 'единицы': 'str'}

# Ввод данных
goods_number = int(input('Сколько товаров хотите добавить? '))
catalog = []
for i in range(goods_number):
    good_props = {}
    for prop_num in range(len(properties)):
        prop_name = str(list(properties.keys())[prop_num])
        if list(properties.values())[prop_num] == 'str':
            good_props[prop_name] = input(f'Введите {prop_name} {i + 1} товара: ')
        elif list(properties.values())[prop_num] == 'int':
            good_props[prop_name] = int(input(f'Введите {prop_name} {i + 1} товара: '))
    good = (i + 1), good_props
    catalog.append(good)
print(catalog)

analytics = {}
for prop_num in range(len(properties)):
    analytics[str(list(properties.keys())[prop_num])] = 0
    lst = []
    for good in range(goods_number):
        lst.append(catalog[good][1].get(str((list(properties.keys())[prop_num]))))
    analytics[str((list(properties.keys())[prop_num]))] = list(set(lst))

print(analytics)
