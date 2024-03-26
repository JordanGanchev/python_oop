from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, 250, price)

    def details(self):
        return f"Gingerbread {self.name}: 250g - {self.price:.2f}lv."