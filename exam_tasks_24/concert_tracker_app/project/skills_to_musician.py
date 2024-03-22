
class Find_somewhere:

    def __init__(self):
        self.valid_skills = {
            'Drummer': [
                "play the drums with drumsticks",
                "play the drums with drum brushes"],
            'Guitarist': [
                "play metal",
                "play rock",
                "play jazz"],
            'Singer': [
                "sing high pitch notes",
                "sing low pitch notes"],
            }

    def find_type(self, skill):
        for key, value in self.valid_skills:
            if skill == value:
                return key
            return None
