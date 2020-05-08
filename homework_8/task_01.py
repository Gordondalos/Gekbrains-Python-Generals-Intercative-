# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:

    def __init__(self, input):
        self.input = input

    @classmethod
    def to_number(cls, string):
        # Приведение строки к списку чисел
        day = int(string.split('-')[0])
        month = int(string.split('-')[1])
        year = int(string.split('-')[2])
        return day, month, year

    @staticmethod
    def validate(lst):
        # Проверка списка чисел на валидность
        day = lst[0]
        month = lst[1]
        year = lst[2]
        if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 2050:
            print(f'Хорошая дата: {day} {month} {year}')
        else:
            print('Ошибка в дате')

    def check_date(self):
        # Итоговая проверка даты с использованием методов, описанных выше
        Date.validate(Date.to_number(self.input))


date = Date('1-1-2020')
date.check_date()
