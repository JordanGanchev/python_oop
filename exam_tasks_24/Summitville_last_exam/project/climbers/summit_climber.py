from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    initial_strength = 150

    def __init__(self, name: str):
        super().__init__(name, self.initial_strength)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Advanced":
            self.strength -= 30 * 1.3
        else:
            self.strength -= 30 * 2.5
        self.conquered_peaks.append(peak.name)

    # def climb(self, peak: BasePeak):
    #     difficulty_multiplier = 1.3 if peak.difficulty_level == "Advanced" else 2.5
    #     self.strength -= 30.0 * difficulty_multiplier
    #     self.conquered_peaks.append(peak.name)
