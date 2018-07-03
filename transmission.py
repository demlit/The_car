class Transmission:
    gears = [-1, 0, 1, 2, 3, 4, 5]
    oil_per_turns = 0.05
    turns_per_oil = 100000

    def __init__(self):
        self.gear = 0
        self.oil = 1
        self.turns_engine = 0
        self.turns_wheels = 0

    def __repr__(self):
        return "Transmission status:\n" \
               "gear = %s\n" \
               "oil = %s\n" \
               "turns_engine = %s\n" \
               "turns_wheels = %s\n" % (self.gear, self.oil, self.turns_engine, self.turns_wheels)

    def set_gear(self, gear):
        if gear in self.gears:
            self.gear = gear
        else:
            raise Exception("Такой передачи не существует. Только от -1 до 5")

    def transform_turns(self):
        self.turns_wheels = self.turns_engine * abs(self.gear)

    def clutch_pedal(self):
        self.oil = 1.0 - (self.turns_engine // self.turns_per_oil * self.oil_per_turns)
        if self.oil <= 0:
            self.oil = 0
            self.set_gear(0)
            self.turns_engine = 1.0/self.oil_per_turns*self.turns_per_oil
            raise Exception("Масло кончилось, коробка передач работать не будет")
        self.transform_turns()


if __name__ == "__main__":
    b = Transmission()
    b.set_gear(-1)
    b.turns_engine = 350000
    b.clutch_pedal()
    print(b)
    b.turns_engine = 10550000
    b.clutch_pedal()
    print(b)