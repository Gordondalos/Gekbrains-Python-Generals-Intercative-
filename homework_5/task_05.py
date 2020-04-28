# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

with open("text_5.txt", "w") as file:
    lst = [random.randint(0, 20) for i in range(20)]
    new = []
    sum = 0  # сумму подсчитаем прямо при создании файла
    for i in lst:
        sum += i
        i = str(i) + ' '
        new.append(i)
    file.writelines(new)

print(f'Сумма: {sum}')
