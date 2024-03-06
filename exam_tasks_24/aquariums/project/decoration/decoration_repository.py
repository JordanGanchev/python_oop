from typing import List


class DecorationRepository:
    DECOR = []

    def __init__(self):
        self.decorations: List = []

    def add(self, decoration):
        self.decorations.append(decoration)
        self.DECOR.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        decoration = next((d for d in self.decorations if d.__class__.__name__ == decoration_type), None)
        return decoration

