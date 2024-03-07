from typing import List

from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class Controller:

    VALID_TYPE_AQUARIUM = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
    VALID_TYPE_DECORATION = {"Ornament": Ornament, "Plant": Plant}

    def __init__(self):
        self.decorations_repository = []
        self.aquariums: List = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.VALID_TYPE_AQUARIUM:
            return "Invalid aquarium type."
        aquarium = self.VALID_TYPE_AQUARIUM[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.VALID_TYPE_DECORATION:
            return "Invalid decoration type."
        decoration = self.VALID_TYPE_DECORATION[decoration_type]()
        self.decorations_repository.append(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = next((d for d in self.decorations_repository if decoration_type == d.__class__.__name__), None)
        aquarium = next((a for a in self.aquariums if aquarium_name == a.name))
        if decoration and aquarium:
            self.aquariums.append(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.VALID_TYPE_AQUARIUM:
            return "There isn't a fish of type {fish_type}."
        

    def feed_fish(self, aquarium_name: str):
        pass

    def calculate_value(self, aquarium_name: str):
        pass

    def report(self):
        pass
