from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        if not self.robots:
            return f"{self.name} Main Service:\n" \
                   f"Robots: none"
        result = []
        for el in self.robots:
            result.append(el)

        return f"{self.name} Main Service:\n" \
               f"Robots: {' '.join([e for e in result])}"