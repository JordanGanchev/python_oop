class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        pass

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        pass

    def add_robot_to_service(self, robot_name: str, service_name: str):
        pass

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        pass

    def feed_all_robots_from_service(self, service_name: str):
        pass

    def service_price(self, service_name: str):
        pass

    def __str__(self):
        pass