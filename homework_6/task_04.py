# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула на{direction}')

    def show_speed(self):
        print(f'{self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        speed_limit = 60
        if self.speed > speed_limit:
            print(f'Превышение скорости на {self.speed - speed_limit} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        speed_limit = 40
        if self.speed > speed_limit:
            print(f'Превышение скорости на {self.speed - speed_limit} км/ч')


class PoliceCar(Car):
    pass


car_0 = SportCar(80, 'красная', 'Машина 0', False)
print(car_0.color)
car_0.show_speed()

car_1 = TownCar(80, 'синяя', 'Машина 1', False)
print(car_1.color)
car_1.show_speed()

car_2 = WorkCar(120, 'красная', 'Машина 2', False)
print(car_2.name)
car_2.show_speed()

car_3 = PoliceCar(120, 'полосатая', 'Полиция', True)
print(car_3.name)
car_3.show_speed()
