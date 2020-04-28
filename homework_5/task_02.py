# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


def words(cnt):
    # Функция вычисления падежа слова "слово" для чисел от 0 до 20
    if cnt == 1:
        return 'слово'
    elif cnt in [2, 3, 4]:
        return 'слова'
    else:
        return 'слов'


try:
    with open("text_1_2.txt") as file:
        data = file.readlines()

except FileNotFoundError:
    print('Файл не найден')

print(f'Всего строк: {len(data)}')
for i in range(len(data)):
    words_count = len(data[i].split())
    words_str = words(words_count)
    print(f'В строке {i + 1} - {words_count} {words_str}')
