from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        super().__init__(name, hardware_type, capacity, memory)
        self.hardware_type = 'Power'
        self.capacity = int(capacity * 0.25)
        self.memory = int(memory * 1.75)