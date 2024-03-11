from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak



class SummitQuestManagerApp:
    VALID_PEAK = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}
    VALID_CLIMBER = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}

    def __init__(self):
        self.climbers: List = []
        self.peaks: list = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBER:
            return f"{climber_type} doesn't exist in our register."
        name = next((n for n in self.climbers if n.name == climber_name), None)
        if name is not None:
            return f"{climber_name} has been already registered."
        new_climber = self.VALID_CLIMBER[climber_type](climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAK:
            return f"{peak_type} is an unknown type of peak."
        new_peak = self.VALID_PEAK[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f'{peak_name} is successfully added to the wish list as a {peak_type}.'

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        pass

    def perform_climbing(self, climber_name: str, peak_name: str):
        pass

    def get_statistics(self):
        pass
