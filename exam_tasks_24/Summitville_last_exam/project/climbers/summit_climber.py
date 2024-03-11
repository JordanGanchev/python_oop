from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    STRENGTH = 150

    def __init__(self, name: str):
        super().__init__(name, self.STRENGTH)

    def can_climb(self):
        if self.strength >= 75:
            return True

    def climb(self, peak : BasePeak):
        self.conquered_peaks.append(peak)
        if peak.__class__.__name__ == "Advanced":
            return (self.strength - 30) * 1.3
        else:
            return (self.strength - 30) * 2,5
