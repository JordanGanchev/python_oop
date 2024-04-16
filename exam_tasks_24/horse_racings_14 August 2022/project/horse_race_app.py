from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_TYPE_HORSE = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):

        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.VALID_TYPE_HORSE:
            return None
        if self._find_horses_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")
        new_hors = self.VALID_TYPE_HORSE[horse_type](horse_name, horse_speed)
        self.horses.append(new_hors)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self._find_jockey_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type not in ["Winter", "Spring", "Autumn", "Summer"]:
            raise Exception(f"Race {race_type} has been already created!")
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        pass

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        pass

    def start_horse_race(self, race_type: str):
        pass

    def _find_horses_name(self, name):
        return next((n for n in self.horses if n.name == name), None)

    def _find_jockey_name(self, name):
        return next((j for j in self.jockeys if j.name == name), None)
