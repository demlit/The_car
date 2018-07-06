from math import pi


class Wheels:
    wheel = 0.0006 * pi  # длина окружности колеса

    def __init__(self):
        self.turns_wheels = 0
        self.path = 0

    def __repr__(self):
        return "Wheels status:\n" \
               "turns_wheels = %s\n" \
               "path = %s\n" % (self.turns_wheels, self.path)

    def transform_path(self):  # преобразовать обороты колёс в пройденый путь
        self.path = self.turns_wheels * self.wheel
        return self.path


if __name__ == "__main__":
    pass
