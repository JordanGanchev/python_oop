from typing import List

from project import race
from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPE = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: list[race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.VALID_CAR_TYPE:
            return None
        if self.__get_name_car(model):
            raise Exception(f"Car {model} is already created!")
        new_car = self.VALID_CAR_TYPE[car_type](model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.__get_name_driver(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.__get_name_race(race_name):
            raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if self.__get_name_driver(driver_name) is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = next((c for c in self.cars if c.__class__.__name__ == car_type or c.is_taken is True), None)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if self.__get_name_race(race_name) is None:
            raise Exception(f"Race {race_name} could not be found!")
        if self.__get_name_driver(driver_name) is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if self.__get_name_driver(driver_name).car is None:
            raise f"Driver {driver_name} could not participate in the race!"

    def start_race(self, race_name: str):
        if self.__get_name_race(race_name) is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(self.races) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

    def __get_name_driver(self, name):
        driver = [n for n in self.drivers if n.name == name]
        return driver[0] if driver else None

    def __get_name_car(self, model):
        car = [n for n in self.cars if n.model == model]
        return car[0] if car else None

    def __get_name_race(self, name):
        race_first = [n for n in self.races if n.name == name]
        return race_first[0] if race_first else None



