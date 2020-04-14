# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_sec = int(input('Введите количество секунд: '))

hrs = time_in_sec // 3600
mins_in_sec = time_in_sec % 3600
mins = mins_in_sec // 60
secs = mins_in_sec % 60

hrs_string = hrs if hrs > 9 else f'0{hrs}'
mins_string = mins if mins > 9 else f'0{mins}'
secs_string = secs if secs > 9 else f'0{secs}'

print(f'{hrs_string}:{mins_string}:{secs_string}')
