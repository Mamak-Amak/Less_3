from random import choice
class Car:

    direction = ["Север", "Северозапад", "Восток", "Юговосток",
                 "Юг", "Югозапад", "Запад", "Северозапад"]

    def __init__(self, name, color, speed, ispolice = False):
        self.name = name
        self.color = color
        self.speed = speed
        self.ispolice = ispolice
        print(f'Новая машина: {name} имеет цвет {color}.\n Это полицейкая машина? {ispolice}')

    def go(self):
        print(f'{self.name}:машина поехала ')

    def stop(self):
        print(f'{self.name}:машина стоит ')

    def turn(self):
        print(f'{self.name}:машина поворачивает {choice(self.direction)}. ')

    def show_speed(self):
        print(f'{self.name}:скорость машины: {self.speed}. ')

class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: скорость машины: {self.speed}. разгоняется!' if self.speed > 60 else super().show_speed()

class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: скорость машины: {self.speed}. разгоняется!' if self.speed > 40 else super().show_speed()

class SportCar(Car):
    pass

class PoliceCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, ispolice = True)

police_car = PoliceCar('"Полиция"', 'белый', 87)
work_car = WorkCar('"Грузовая"', 'белый', 41)
sport_car = SportCar('"Спортивная"', 'белый', 120)
town_car = TownCar('"Семейная"', 'белый', 60)

cars_list = [police_car, work_car, sport_car, town_car]

for i in cars_list:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()



