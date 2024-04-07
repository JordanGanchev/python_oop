from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        tel_num = next((num for num in self.clients_list if num.phone_number == client_phone_number), None)
        if tel_num:
            raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        for meal in self.menu:
            return meal.details()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        pass

    def cancel_order(self, client_phone_number: str):
        pass

    def finish_order(self, client_phone_number: str):
        pass

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
