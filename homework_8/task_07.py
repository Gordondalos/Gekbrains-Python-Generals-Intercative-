# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'Число {self.real} + {self.imag}i'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)


num_1 = Complex(1, 2)
num_2 = Complex(3, 4)
print(num_1 + num_2)
print(num_1 * num_2)
