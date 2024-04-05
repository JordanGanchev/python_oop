from typing import List


class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List = []
        self.bill: float = 0.0

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if len(value) != 10 or value[0] != '0' or not value.isdigit():
            raise ValueError("Invalid phone number!")
        self._phone_number = value

