# class Player:
#
#     def __init__(self, name: str, age: int, stamina=100):
#         self.name = name
#         self.age = age
#         self.stamina: int = stamina
#         self.need_sustenance = None
#         self.set_name = set()
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if not value:
#             raise Exception("Name not valid!")
#         if value in self.set_name:
#             raise ValueError(f"Name {value} is already used!")
#         self.set_name.add(value)
#         self.__name = value
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value < 12:
#             raise ValueError("The player cannot be under 12 years old!")
#         self.__age = value
#
#     @property
#     def stamina(self):
#         return self.__stamina
#
#     @stamina.setter
#     def stamina(self, value):
#         if value < 0 or value > 100:
#             raise ValueError("Stamina not valid!")
#         self.__stamina = value
#
#     @property
#     def need_sustenance(self):
#         return self.__need_sustenance
#
#     @need_sustenance.setter
#     def need_sustenance(self, value):
#         if self.stamina < 100:
#             self.stamina = True
#         self.__need_sustenance = value

from project.supply.supply import Supply


class Player:
    players_names = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name not valid!")
        elif value in Player.players_names:
            raise Exception(f"Name {value} is already used!")
        Player.players_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.__stamina < 100

    def _sustain_player(self, supply: Supply):
        if self.stamina + supply.energy > 100:
            self.stamina = 100
        else:
            self.stamina += supply.energy

    def __lt__(self, other):
        return self.stamina < other.stamina

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"




