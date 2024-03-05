from typing import List

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.software import Software



class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        comp_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(comp_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        comp_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(comp_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for name_hard in System._hardware:
            if not name_hard.name == name:
                return "Hardware does not exist"
        # comp_software = ExpressSoftware(hardware_name, capacity_consumption, memory_consumption)
        # System._software.append(comp_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        comp_software = LightSoftware(hardware_name, capacity_consumption, memory_consumption)
        System._software.append(comp_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        pass

    @staticmethod
    def analyze():
        pass

    @staticmethod
    def system_split():
        pass

