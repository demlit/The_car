class Transmission:
    gears = [-1, 0, 1, 2, 3, 4, 5]  # массив передач
    oil_per_turns = 0.05  # трата масла ->
    turns_per_oil = 100000  # за такое количество оборотов
    health_per_turns = 0.05  # разрушение КП ->
    turns_per_health = 1000000  # за такое количество оборотов

    def __init__(self):
        self.gear = 0
        self.oil = 1.0
        self.turns_engine = 0
        self.turns_wheels = 0
        self.__turns_mileage = 0
        self.transmission_health = 1.0
        self.__health_mileage = 0

    def __repr__(self):
        return "Transmission status:\n" \
               "gear = %s\n" \
               "oil = %s\n" \
               "transmission health = %s %%\n" \
               "turns_engine = %s\n" \
               "turns_wheels = %s\n" % (self.gear, self.oil, self.transmission_health * 100,
                                        self.turns_engine, self.turns_wheels)

    def set_gear(self, gear):   # задать передачу
        if gear in self.gears:
            self.gear = gear
        else:
            raise Exception("Такой передачи не существует. Только от -1 до 5")

    def transform_turns(self):  # преобразовать обороты двигателя в обороты колёс
        self.turns_wheels = self.turns_engine * abs(self.gear) * self.transmission_health
        self.__mileage_for_oil()
        self.__mileage_for_health()

    def __mileage_for_oil(self):  # Счётчик пробега для масла
        self.__turns_mileage += self.turns_engine

    def __mileage_for_health(self):  # Счётчик пробега для КП
        self.__health_mileage += self.turns_engine

    def clutch_pedal(self):  # расчёты при работе коробки передач, как-бы "педаль сцепления"
        if self.oil == 0:
            raise Exception("Коробка передач работать не работает. Очень жаль.")
        self.transform_turns()
        self.oil = (1.0 - self.__turns_mileage // self.turns_per_oil * self.oil_per_turns) / self.transmission_health
        self.transmission_health = 1.0 - self.__health_mileage // self.turns_per_health * self.health_per_turns
        if self.oil <= 0:
            self.oil = 0
            self.set_gear(0)
        if self.transmission_health <= 0:
            self.transmission_health = 0
            self.oil = 0
            self.set_gear(0)
        return self.turns_wheels

    def add_oil(self):  # восстановить масло
        self.oil = 1.0
        self.__turns_mileage = 0

    def repair_transmission(self):  # починить КП
        self.transmission_health = 1.0
        self.__health_mileage = 0


if __name__ == "__main__":
    pass
