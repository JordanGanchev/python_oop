from project.booths.booth import Booth


class PrivateBooth(Booth):

    def __init__(self, booth_number: int,  capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        return number_of_people*3.5
