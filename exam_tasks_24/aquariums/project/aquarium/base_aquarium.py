from abc import ABC, abstractmethod
from typing import List


class BaseAquarium(ABC):
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

    def calculate_comfort(self):
        pass

    def add_fish(self, fish):
        pass

    def remove_fish(self, fish):
        pass

    def add_decoration(self, decoration):
        pass

    def feed(self):
        pass
    
    def __str__(self):
        pass







