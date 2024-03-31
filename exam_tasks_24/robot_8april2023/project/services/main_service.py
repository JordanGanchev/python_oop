from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        if not self.robots.__class__.__name__:
            return f"{self.name} Main Service:\n" \
                   f"Robots: none"
        result = []
        for el in self.robots:
            result.append(el.name)

        total_exit = ""
        total_exit += f"{self.name} Main Service:\n" \
                      f"Robots: {' '.join([e for e in result])}"
        return total_exit