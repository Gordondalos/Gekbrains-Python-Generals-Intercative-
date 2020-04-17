# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# catalog = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'единицы': 'шт'}),
# (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'единицы': 'шт'}),
# (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'единицы': 'шт'})]

properties = ('название', 'цена', 'количество', 'единицы')

# Ввод данных
goods_number = int(input('Сколько товаров хотите добавить? '))
catalog = []
for i in range(goods_number):
    good_props = {}
    for prop_num in range(len(properties)):
        prop_name = str(properties[prop_num])
        good_props[prop_name] = input(f'Введите {prop_name} {i + 1} товара: ')
    good = (i + 1), good_props
    catalog.append(good)
print(catalog)
# Извиняюсь, что цена и количество строкой. Чтобы свойства имели разный тип, пришлось бы отказаться от
# такого классного цикла и описывать 4 ввода отдельно.

analytics = {}
for prop_num in range(len(properties)):
    analytics[str(properties[prop_num])] = 0
    lst = []
    for good in range(goods_number):
        lst.append(catalog[good][1].get(str(properties[prop_num])))
    analytics[str(properties[prop_num])] = list(set(lst))

print(analytics)
