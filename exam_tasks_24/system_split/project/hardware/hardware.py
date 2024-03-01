from typing import List

from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List = []

    def install(self, software: Software):
        soft_comp = [soft for soft in self.software_components if soft.software == software]
        if soft_comp:
            capacity = soft_comp[2]
            memory = soft_comp[3]
            if self.capacity > capacity and self.memory > memory:
                self.software_components.append(software)
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        soft_comp = [soft for soft in self.software_components if soft.software == software]
        if soft_comp:
            self.software_components.remove(software)
