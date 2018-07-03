time = 100


class Engine:
    max_gasoline = 50  # объем бака
    max_gas = 33  # максимальный угол нажатия педали газа
    gas_rpm_default = 400  # обороты на холостом ходу
    rpm_per_gas = 200  # изменение оборотов за 1 градус педали газа
    gasoline_per_turns = 0.0001  # убыток бензина за 1 оборот двигателя

    def __init__(self):
        self.gasoline = 0.0
        self.power = False
        self.gas = 1.0
        self.rpm = 0
        self.turns = 0

    def __repr__(self):
        return "Engine status:\n" \
               "gasoline = %s\n" \
               "power = %s\n" \
               "gas = %s\n" \
               "rpm = %s\n" \
               "turns = %s\n" % (self.gasoline, self.power, self.gas, self.rpm, self.turns)

    def add_gasoline(self):  # заправить полный бак
        self.gasoline = 50.0

    def start_engine(self):  # запустить двигатель
        if self.gasoline:
            self.power = True
            self.rpm_engine()
        else:
            raise Exception("Топливный бак пуст. Очень жаль")

    def stop_engine(self):  # вручную остановить двигатель
        self.power = False
        self.rpm = 0

    def rpm_engine(self):  # расчёт оборотов в минуту
        self.rpm = self.power * (self.gas_rpm_default + self.gas * self.rpm_per_gas)

    def gas_pedal(self, set_gas=1.0):  # изменить положение педали газа
        if 1 <= set_gas <= 33:
            self.gas = set_gas * 1.0
        else:
            raise Exception("Газ может быть только в диапазоне 1-33")
        self.rpm_engine()

    def turns_engine(self):  # расчёт общего количества оборотов
        self.turns = self.turns + self.rpm * time
        self.gasoline_engine()

    def gasoline_engine(self):  # расчёт потраченого бензина
        remainder = self.gasoline
        self.gasoline = self.gasoline - self.turns * self.gasoline_per_turns
        if self.gasoline <= 0:
            self.gasoline = 0
            self.power = False
            self.turns = remainder/self.gasoline_per_turns
            raise Exception("Топливный бак пуст. Очень жаль")


if __name__ == "__main__":
    pass
