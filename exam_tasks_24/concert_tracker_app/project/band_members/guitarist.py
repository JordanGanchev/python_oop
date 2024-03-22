from project.band_members.musician import Musician


class Guitarist(Musician):
    SKILL = ["play metal", "play rock", "play jazz"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)