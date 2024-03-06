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
        total_sum_memory_soft = 0
        for obj in System._software:
            total_sum_memory_soft += obj.memory_consumption

        total_sum_memory_hard = 0
        for obj in System._hardware:
            total_sum_memory_hard += obj.memory

        total_sum_capacity_soft = 0
        for obj in System._software:
            total_sum_capacity_soft += obj.capacity_consumption

        total_sum_capacity_hard = 0
        for obj in System._hardware:
            total_sum_capacity_hard += obj.capacity
        return f"System Analysis" '\n' \
               f"Hardware Components: {len(System._hardware)}" '\n' \
               f"Software Components: {len(System._software)}"  '\n' \
               f"Total Operational Memory: {total_sum_memory_soft} / {total_sum_memory_hard}" '\n' \
               f"Total Capacity Taken: {total_sum_capacity_soft} / {total_sum_capacity_hard}" \

    @staticmethod
    def system_split():
        list_components = []
        for components in System._hardware:
            list_components.append(components.name)
        return f"Hardware Component - {', '.join(list_components)}" '\n' \
               # f"Express Software Components: {number of the installed express software components}" '\n' \
               # f"Light Software Components: {number of the installed light software components}" '\n' \
               # f"Memory Usage: {total memory used of all installed software components} / {total memory of the hardware}" '\n' \
               # f"Capacity Usage: {total capacity used of all installed software components } / {total capacity of the hardware}" '\n' \
               # f"Type: {hardware_type}" '\n' \
               # f"Software Components: {names of all software components separated by ', '} (or 'None' if no software components)"


