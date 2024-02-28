from project.supply.supply import Supply


class Food(Supply):

    def __init__(self, name, energy=25):
        super().__init__(name, energy)

    @property
    def type(self):
        return "Food"

    def details(self):
        return f"{self.type}: {self.name}, {self.energy}"
