from car import Car
from time import sleep

car = Car()
car.add_gasoline(50)
car.turn_on()
car.change_speed(33,5)
while True:
    sleep(1)
    car.time = 1
    car.get_car_data()
    print(car)
