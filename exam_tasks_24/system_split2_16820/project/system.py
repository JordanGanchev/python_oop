from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    hardware = []
    software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        heavy = HeavyHardware(name, capacity, memory)
        System.hardware.append(heavy)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        pover = PowerHardware(name, capacity, memory)
        System.software.append(pover)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System.hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System.software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System.hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System.software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = next((h for h in System.hardware if h.name == hardware_name), None)
        software = next((s for s in System.hardware if s.name == software_name), None)
        if hardware is None or software is None:
            return "Some of the components do not exist"
        hardware.uninstall(software)
        System.software.remove(software)


    @staticmethod
    def analyze():
        total_memory = [sum(mc) for mc in System.software.memory_consumption]
        return "System Analysis\n" \
               f"Hardware Components: {len(System.hardware)}\n" \
               f"Software Components: {len(System.software)}\n" \
               f"Total Operational Memory: {total memory consumption for all registered software components} / {total memory for all registered hardware components}\n" \
               f"Total Capacity Taken: {total capacity consumption for all registered software components} / {total capacity of all registered hardware components}"    @staticmethod
    def system_split():
        pass

    # @staticmethod
    # def __find_name_software(name):
    # return next((n for n in System.software if n.name == name), None)

