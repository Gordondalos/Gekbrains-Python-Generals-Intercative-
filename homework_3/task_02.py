# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_data(**kwargs):
    # Функция возвращает значения аргументов одной строкой

    result = ''
    for item in kwargs.values():
        result += item + ' '
    return result


print(user_data(name='Taras', sirname='Kvitko', year='1986', city='Saint-Petersburg', email='tkvitko@gmail.com',
                phone='79110231144'))
