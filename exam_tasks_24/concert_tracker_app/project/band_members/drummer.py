from project.band_members.musician import Musician


class Drummer(Musician):
    SKILL = ["play the drums with drumsticks", "play the drums with drum brushes"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)