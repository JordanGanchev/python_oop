from typing import List


class Band:

    def __init__(self, name: str):
        self.name = name
        self.members: List = []

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
