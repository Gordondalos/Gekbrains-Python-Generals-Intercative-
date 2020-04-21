# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle

source = [2, 5, 3]

first = []
for el in count(3):
    if el > 10:
        break
    else:
        first.append(el)

second = []
i = 0
for el in cycle(source):
    if i > 10:
        break
    else:
        second.append(el)
        i += 1

print(first)
print(second)
