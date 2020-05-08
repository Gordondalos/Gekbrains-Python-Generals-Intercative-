# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyZeroException(Exception):
    def __init__(self, text):
        self.text = text


inp_data = input("Введите делитель: ")

try:
    inp_data = int(inp_data)
    if inp_data == 0:
        raise MyZeroException("На ноль не поделим")
except ValueError:
    print("Вы ввели не число")
except MyZeroException as err:
    print(err)
else:
    print(f"Все хорошо. Результат: {100 / inp_data}")
