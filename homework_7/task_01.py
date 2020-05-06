# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):

        new = ''
        for string in self.matrix:
            for item in string:
                new += str(item)
                new += '  '
            new += '\n'

        return new

    def __add__(self, other):

        new = [[0] * len(self.matrix[0]) for i in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                new[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return Matrix(new)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[11, 12], [13, 14], [15, 16]])
print(matrix_1 + matrix_2)
