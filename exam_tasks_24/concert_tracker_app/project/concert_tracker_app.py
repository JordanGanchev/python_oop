from typing import List

from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer


class ConcertTrackerApp:
    VALID_MUSICIAN = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List = []
        self.musicians: List = []
        self.concerts: List = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN:
            raise ValueError("Invalid musician type!")
        if self._find_musician(name):
            raise Exception(f"{name} is already a musician!")
        new_musician = self.VALID_MUSICIAN[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        pass

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        pass

    def add_musician_to_band(self, musician_name: str, band_name: str):
        pass

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        pass

    def start_concert(self, concert_place: str, band_name: str):
        pass

    def _find_musician(self, name):
        name = [n for n in self.musicians if n.name == name]
        return name[0] if name else None

