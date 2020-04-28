# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("text_1_2.txt", "w") as file:
    to_write = []
    while True:
        cur_str = input('Введите новую строку или нажмите Enter, чтобы закончить: ')
        if cur_str:
            to_write.append(cur_str + '\n')
        else:
            break

    file.writelines(to_write)
