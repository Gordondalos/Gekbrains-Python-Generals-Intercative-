# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input('Введите число: ')



max = 0

i = 0
while i < len(number):
    tmp = int(number[i])
    if int(number[i]) > max:
        max = int(number[i])
    i = i +1

print(max)