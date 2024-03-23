from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


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
        if self._find_bands(name):
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if self._find_concerts(place):
            raise Exception(f"{place} is already registered for {genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if not self._find_musician(musician_name):
            raise Exception(f"{musician_name} isn't a musician!")
        if not self._find_bands(band_name):
            raise Exception(f"{band_name} isn't a band!")
        group = self._find_bands(band_name)
        group.members.append(musician_name)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        pass

    def start_concert(self, concert_place: str, band_name: str):
        pass

    def _find_bands(self, name):
        name = [n for n in self.musicians if n.name == name]
        return name[0] if name else None

    def _find_musician(self, name):
        name = [n for n in self.bands if n.name == name]
        return name[0] if name else None

    def _find_concerts(self, name):
        place = [p for p in self.concerts if p.place == name]
        return place[0] if place else None

