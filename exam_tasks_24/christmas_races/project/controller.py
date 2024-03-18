from typing import List

from project import race
from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver


class Controller:
    VALID_CAR_TYPE = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: list[race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.VALID_CAR_TYPE:
            return None
        car = next((c for c in self.cars if c.model == model), None)
        if car:
            raise Exception(f"Car {model} is already created!")
        new_car = self.VALID_CAR_TYPE[car_type](model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        pass

    def create_race(self, race_name: str):
        pass

    def add_car_to_driver(self, driver_name: str, car_type: str):
        pass

    def add_driver_to_race(self, race_name: str, driver_name: str):
        pass

    def start_race(self, race_name: str):
        pass
