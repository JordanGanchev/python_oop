from typing import List

from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_TYPE_WAITER = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    VALID_TYPE_CLIENT = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __init__(self):
        self.clients: List = []
        self.waiters: List = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.VALID_TYPE_WAITER:
            return f"{waiter_type} is not a recognized waiter type."
        if self._find_waiter_name(waiter_name):
            return f"{waiter_name} is already on the staff."
        new_waiter = self.VALID_TYPE_WAITER[waiter_type](waiter_name, hours_worked)
        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.VALID_TYPE_CLIENT:
            return f"{client_type} is not a recognized client type."
        if self._find_client_name(client_name):
            return f"{client_name} is already a client."
        new_client = self.VALID_TYPE_CLIENT[client_type](client_name)
        self.clients.append(new_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = self._find_waiter_name(waiter_name)
        if waiter is None:
            return f"No waiter found with the name {waiter_name}."
        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = self._find_client_name(client_name)
        if client is None:
            return f"{client_name} is not a registered client."
        point = client.earning_points(order_amount)
        return f"{client_name} earned {point} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = self._find_client_name(client_name)
        if client is None:
            return f"{client_name} cannot get a discount because this client is not admitted!"
        return client.apply_discount()

    def generate_report(self):
        # return f"$$ Monthly Report $$\n" \
        #        f"Total Earnings: ${total_earnings}\n" \
        #        f"Total Clients Unused Points: {total_client_points}\n" \
        #        f"Total Clients Count: {clients_count}\n" \
        #        f"** Waiter Details **\n" \
        #        f"Name: {name1}, Total earnings: ${waiter1_total_earnings}" \
        #        f"Name: {name2}, Total earnings: ${waiter2_total_earnings}"
        pass

    def _find_waiter_name(self, name):
        return next((n for n in self.waiters if n.name == name), None)

    def _find_client_name(self, name):
        return next((n for n in self.clients if n.name == name), None)
