from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name: str, software_type: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, software_type, capacity_consumption, memory_consumption)
        self.software_type = 'Express'
        self.memory_consumption = int(memory_consumption * 2)
