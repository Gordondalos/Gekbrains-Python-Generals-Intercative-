# Необходимо написать программу, открывающую файл text_4.txt на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translates = {
    "One": "Один",
    "Three": "Три",
    "Two": "Два",
    "Four": "Четыре"
}

# Чтение данных
try:
    with open("text_4.txt") as file:
        data = file.readlines()

except FileNotFoundError:
    print('Файл не найден')

# Создание базы для работы на основе словаря
eng = {}
for i in range(len(data)):
    eng.update({data[i].split(' - ')[0]: int((data[i].split(' - ')[1]))})

# Создание нового словаря на русском
rus = {}
for k in eng.keys():
    rus.update({translates.get(k): eng.get(k)})

# Запись результата
with open("text_4_rus.txt", "w") as file:
    to_write = []
    for k, v in rus.items():
        to_write.append(f'{k} - {v}' + '\n')
    file.writelines(to_write)
