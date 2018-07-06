class Transmission:
    gears = [-1, 0, 1, 2, 3, 4, 5]  # массив передач
    oil_per_turns = 0.05  # трата масла ->
    turns_per_oil = 100000  # за такое количество оборотов

    def __init__(self):
        self.gear = 0
        self.oil = 1
        self.turns_engine = 0
        self.turns_wheels = 0
        self.__turns_rotate = 0

    def __repr__(self):
        return "Transmission status:\n" \
               "gear = %s\n" \
               "oil = %s\n" \
               "turns_engine = %s\n" \
               "turns_wheels = %s\n" % (self.gear, self.oil, self.turns_engine, self.turns_wheels)

    def set_gear(self, gear):   # задать передачу
        if gear in self.gears:
            self.gear = gear
        else:
            raise Exception("Такой передачи не существует. Только от -1 до 5")

    def transform_turns(self):  # преобразовать обороты двигателя в обороты колёс
        self.turns_wheels = self.turns_engine * abs(self.gear)

    def clutch_pedal(self):  # расчёты при работе коробки передач, как-бы "нажали педаль сцепления"
        self.oil = 1.0 - ((self.turns_engine - self.__turns_rotate) // self.turns_per_oil * self.oil_per_turns)
        if self.oil <= 0:
            self.oil = 0
            self.set_gear(0)
#            self.turns_engine = 1.0/self.oil_per_turns*self.turns_per_oil
            raise Exception("Масло кончилось, коробка передач работать не будет")
        self.transform_turns()
        return self.turns_wheels

    def add_oil(self):  # восстановить масло
        self.oil = 1.0
        self.__turns_rotate = self.turns_engine


if __name__ == "__main__":
    pass
