from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, "Regular")

    def earning_points(self, order_amount: float):
        point = int(order_amount / 10)
        self.points += point
        return point