from abc import ABC, abstractmethod


class BaseClient(ABC):
    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points: int = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Client name should be determined!")
        self._name = value

    @property
    def membership_type(self):
        return self._membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in ["Regular", "VIP"]:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self._membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        percent = 0
        if self.points >= 100:
            percent = 10
            self.points -= 100

        elif 50 <= self.points < 100:
            percent = 5
            self.points -= 50

        elif self.points > 50:
            percent = 0

        return f"{self.name} received a {percent}% discount. Remaining points {self.points}"

