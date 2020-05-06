# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.


class Cell:

    def __init__(self, num):
        self.num = num

    def __str__(self):
        if self.num >= 1:
            return f'Клетка размером {self.num}'
        else:
            return f'Клетки не существует'

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num > other.num:
            return Cell(self.num - other.num)
        else:
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(round(self.num / other.num))

    def make_order(self, count):

        whole_strs = self.num // count

        lst = ['*' * count for i in range(whole_strs)]
        lst.append('*' * (self.num % count))

        result_str = ''
        for i in lst:
            result_str += i
            result_str += '\n'

        return result_str


cell_1 = Cell(34)
cell_2 = Cell(114)

cell_sum = cell_1 + cell_2
print(cell_sum)

cell_sub = cell_1 - cell_2
print(cell_sub)

cell_mul = cell_1 * cell_2
print(cell_mul)

cell_div = cell_1 / cell_2
print(cell_div)

print(cell_1.make_order(10))
