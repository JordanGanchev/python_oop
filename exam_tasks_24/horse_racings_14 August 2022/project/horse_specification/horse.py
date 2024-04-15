from abc import ABC, abstractmethod


class Horse(ABC):
    MAX_SPEED_HORSE = None

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self._name = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value > self.MAX_SPEED_HORSE:
            raise ValueError("Horse speed is too high!")
        self._speed = value

    @abstractmethod
    def train(self):
        pass
