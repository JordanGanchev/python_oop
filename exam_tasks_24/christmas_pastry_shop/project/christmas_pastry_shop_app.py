from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    VALID_TYPE_DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_TYPE_BOOTH = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List = []
        self.delicacies: List = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.VALID_TYPE_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        name_delicacy = self._find_name_delicacy(name)
        if name_delicacy:
            raise Exception(f"{name} already exists!")
        new_delicacy = self.VALID_TYPE_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in self.VALID_TYPE_BOOTH:
            raise Exception(f"{type_booth} is not a valid booth!")
        booth_num = next((num for num in self.booths if num == booth_number), None)
        if booth_num:
            raise Exception(f"Booth number {booth_number} already exists!")
        new_booth = self.VALID_TYPE_BOOTH[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = next((b for b in self.booths if b.is_reserved == False and b.capacity <= number_of_people), None)
        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        delicacy_obj = booth.delicacy_orders
        sum_of_delicacy = 0
        for p in delicacy_obj:
            sum_of_delicacy += p.price
        sum_of_delicacy += booth.price_for_reservation
        self.income += sum_of_delicacy
        result = f"Booth {booth_number}:\n"
        result += f"Bill: {sum_of_delicacy:.2f}lv."
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0.0

        return result

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def _find_name_delicacy(self, name):
        return next((n for n in self.delicacies if n == name), None)
