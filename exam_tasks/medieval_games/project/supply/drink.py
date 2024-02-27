from project.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name):
        super().__init__(name, energy=15)

    @property
    def type(self):
        return "Drink"

    def details(self):
        return f"{self.type}: {self.name}, {self.energy}"
