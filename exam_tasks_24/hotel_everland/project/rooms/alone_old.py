from project.rooms.room import Room


class AloneOld(Room):
    room_members_count = 1
    room_cost = 10

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, self.room_members_count)
        self.default_room_cost = self.room_cost
