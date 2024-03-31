
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOT = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE:
            raise Exception("Invalid service type!")
        new_service = self.VALID_SERVICE[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT:
            raise Exception("Invalid robot type!")
        new_robot = self.VALID_ROBOT[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._find_robot_obj(robot_name)
        service = self._find_services_obj(service_name)
        type_robot = robot.__class__.__name__
        type_service = service.__class__.__name__
        if not (type_robot == "FemaleRobot" and type_service == "SecondaryService") or \
               (type_robot == "MaleRobot" and type_service == "MainService"):
            return "Unsuitable service."
        if service.capacity <= robot.weight:
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._find_services_obj(service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)
        if not robot:
            raise Exception("No such robot in this service!")
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self._find_services_obj(service_name)
        count = 0
        for r in service.robots:
            r.eating()
            count += 1
        return f"Robots fed: {count}."

    def service_price(self, service_name: str):
        service = self._find_services_obj(service_name)
        total_price = 0
        for r in service.robots:
            total_price += r.price
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        for r in self.services:
            return r.details()

    def _find_robot_obj(self, name):
        name = next((n for n in self.robots if n.name == name), None)
        return name

    def _find_services_obj(self, name):
        name = next((n for n in self.services if n.name == name), None)
        return name