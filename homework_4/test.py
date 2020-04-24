# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle


# Решил поупражняться в yield (не понял, какое именно усложнение этой задачи вы задачи устно :(( )

def first(n, m):
    for el in count(n):
        if el < m:
            yield el
        else:
            break


for i in first(3, 11):
    print(i, end=' ')

print()
source = [2, 5, 3]


def second(src, max):
    i = 0
    for el in cycle(src):
        if i > max:
            break
        else:
            yield el
        i += 1


for i in second(source, 11):
    print(i, end=' ')
