from abc import ABC, abstractmethod


class BaseWaiter(ABC):
    def __init__(self, name: str, hours_worked: int):
        self.name = name
        self.hours_worked = hours_worked

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (3 < len(value) < 30):
            raise ValueError("Waiter name must be between 3 and 50 characters in length!")
        self._name = value

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if value < 0:
            raise ValueError("Cannot have negative hours worked!")
        self._hours_worked = value

    @abstractmethod
    def calculate_earnings(self):
        pass

    @abstractmethod
    def report_shift(self):
        pass

    def __str__(self):
        return f"Name: {self.name}, Total earnings: ${self.calculate_earnings()}"
