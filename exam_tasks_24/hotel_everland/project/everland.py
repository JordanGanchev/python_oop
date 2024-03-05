from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum(num.cost for num in self.rooms)
        return f"Monthly consumption: {total_consumption}$."

    def pay(self):
        pass

    def status(self):
        pass