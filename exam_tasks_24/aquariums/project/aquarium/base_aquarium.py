from abc import ABC, abstractmethod
from typing import List

from project.decoration.decoration_repository import DecorationRepository


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List = []
        self.fish: List = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    @staticmethod
    def calculate_comfort():
        decor = next((sum(d.comfort) for d in DecorationRepository.DECOR), None)
        return decor[0]

    def add_fish(self, fish):
        if len(self.fish) > self.capacity:
            return "Not enough capacity."
        self.decorations.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {fish.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        pass

    def __str__(self):
        result = ([n for n in self.fish], None)

        return f"{self.name}:\n"\
               f"Fish: {result}\n"\
               f"Decorations: {len(self.decorations)}\n"\
               f"Comfort: {self.calculate_comfort()}"







