from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    STRENGTH = 200

    def __init__(self, name: str):
        super().__init__(name, self.STRENGTH)

    def can_climb(self):
        if self.strength >= 100:
            self.is_prepared = False

    def climb(self, peak: BasePeak):
        self.conquered_peaks.append(peak)
        if peak.difficulty_level == "Extreme":
            return (self.strength - 20) * 2
        else:
            return (self.strength - 20) * 1.5




