from engine import Engine
from transmission import Transmission
from wheels import Wheels


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
        self.time = 0
        self.transmission_health = 0

    def __repr__(self):
        return "Данные автомобиля и поездки:\n" \
               "\t запущен = %s\n" \
               "\t уровень топлива = %s л.\n" \
               "\t уровень масла = %s %%\n" \
               "\t состояние КП = %s %%\n" \
               "\t скорость = %s км/ч\n" \
               "\t пройденый путь = %s км" % (self.power, self.gasoline, self.oil,
                                              self.transmission_health, self.speed, self.path)

    def get_car_data(self):  # соединение классов, получение данных для вывода
        self.engine.time = self.time
        self.transmission.turns_engine = self.engine.launch_engine()
        self.wheels.turns_wheels = self.transmission.clutch_pedal()
        self.power = self.engine.power
        self.gasoline = self.engine.gasoline
        self.oil = self.transmission.oil * 100
        self.transmission_health = self.transmission.transmission_health * 100
        self.get_speed()
        self.path += self.wheels.transform_path()
        self.time = 0

    def turn_on(self):  # включить двигатель
        try:
            self.engine.start_engine()
        except Exception as e:
            print("Авто не поедет, пока есть проблемы:\n %s" % e)
        else:
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

    def repair_transmission(self):  # починить КП
        self.transmission.repair_transmission()
        print("Ты зашёл на ближайшую СТО и поменял КП. Какой молодец ^_^ ")

    def change_speed(self, gas=engine.gas, gear=transmission.gear):  # изменить скорость
        self.transmission.set_gear(gear)
        self.engine.gas_pedal(gas)
        print("Теперь ты едешь на %s передаче и нажал газ на %s градусов. Какой молодец ^_^ " %
              (self.transmission.gear, self.engine.gas))

    def get_speed(self):  # расчитать скорость
        self.speed = self.engine.rpm * self.transmission.gear * self.wheels.wheel * 60
        return self.speed

    def brake_pedal(self):  # остановить автомобиль
        self.change_speed(1, 0)


if __name__ == "__main__":
    pass
