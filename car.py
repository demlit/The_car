from engine import Engine
from transmission import Transmission
from wheels import Wheels
import time


class Car:
    engine = Engine()  # подключаем двигатель
    transmission = Transmission()  # подключаем КП
    wheels = Wheels()  # подключаем колёса

    def __init__(self):
        self.path = 0
        self.power = False
        self.gasoline = 0.0
        self.oil = 0.0
        self.speed = 0.0
        self.__time_start = 0

    def __repr__(self):
        self.transforms()
        return "Данные автомобиля и поездки:\n" \
               "\tзапущен = %s\n" \
               "\tуровень топлива = %s л.\n" \
               "\tуровень масла = %s %%\n" \
               "\tскорость = %s км/ч\n" \
               "\tпройденый путь = %s км" % (self.power, self.gasoline, self.oil, self.speed, self.path)

    def transforms(self):  # соединение классов, получение данных для вывода
            self.engine.time = self.power * (time.time() - self.__time_start)
            self.transmission.turns_engine = self.engine.turns_engine()
            self.wheels.turns_wheels = self.transmission.clutch_pedal()
            self.power = self.engine.power
            self.gasoline = self.engine.gasoline
            self.oil = self.transmission.oil * 100
            self.get_speed()
            self.path = self.wheels.transform_path()

    def turn_on(self):  # включить двигатель, начинаем отсчёт времени
        try:
            self.engine.start_engine()
        except Exception as e:
            print("Авто не поедет, пока есть проблемы:\n %s" % e)
        else:
            self.__time_start = time.time()
            print("Вжжжжжжжж-чух-чух-чух-чух")

    def turn_off(self):  # выключить двигатель
        self.engine.stop_engine()
        print("Двигатель выключен")

    def add_gasoline(self, litres):  # добавить топлива
        self.engine.add_gasoline(litres)
        print("Машина заправлена. Всего в баке %s литров бензина" % self.engine.gasoline)

    def add_oil(self):  # восстановить масло
        self.transmission.add_oil()
        print("Ты зашёл на ближайшую СТО и поменял масло. Какой молодец ^_^ ")

    def change_speed(self, gas=engine.gas, gear=transmission.gear):  # изменить скорость
        self.transmission.gear = gear
        self.engine.gas = gas
        print("Теперь ты едешь на %s передаче и нажал газ на %s градусов. Какой молодец ^_^ " %
              (self.transmission.gear, self.engine.gas))

    def get_speed(self):  # расчитать скорость
        try:
            self.speed = self.engine.rpm * self.transmission.gear * self.wheels.wheel * 60
        except Exception:
            self.speed = 0
        return self.speed


if __name__ == "__main__":
    pass
