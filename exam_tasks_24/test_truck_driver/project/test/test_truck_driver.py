import unittest
from project.truck_driver import TruckDriver


class TestTruckDriver(unittest.TestCase):

    def setUp(self) -> None:
        self.truck = TruckDriver('dan', 10.0)

    def test_init_method(self):
        self.assertEqual('dan', self.truck.name)
        self.assertEqual(10.0, self.truck.money_per_mile)
        self.assertEqual({}, self.truck.available_cargos)
        self.assertEqual(0, self.truck.earned_money)
        self.assertEqual(0, self.truck.miles)

    def test_setter_earned_money(self):
        with self.assertRaises(ValueError) as content:
            self.truck.earned_money = -1
        self.assertEqual(f"dan went bankrupt.", str(content.exception))
        self.truck.earned_money = 10
        self.assertEqual(10, self.truck.earned_money)

    def test_add_cargo_offer_raise_error(self):
        self.truck.available_cargos['kiro'] = 100
        with self.assertRaises(Exception) as content:
            self.truck.add_cargo_offer('kiro', 100)
        self.assertEqual("Cargo offer is already added.", str(content.exception))

    def test_add_cargo_offer_write(self):
        self.truck.available_cargos['kiro'] = 100
        self.assertEqual(f"Cargo for 200 to asen was added as an offer.", self.truck.add_cargo_offer('asen', 200))
        self.assertEqual({'asen': 200, 'kiro': 100}, self.truck.available_cargos)

    def test_drive_best_cargo_offer_is_empty_dictionaries(self):
        self.assertEqual("There are no offers available.", self.truck.drive_best_cargo_offer())

    def test_drive_best_cargo_offer_is_not_empty_dictionaries(self):
        self.truck.available_cargos['pesho'] = 20
        self.assertEqual('dan is driving 20 to pesho.', self.truck.drive_best_cargo_offer())
        self.assertEqual(200.0, self.truck.earned_money)
        self.assertEqual(20, self.truck.miles)

    def test_check_for_activities_eat(self):
        self.truck.earned_money = 100
        self.truck.check_for_activities(250)
        self.assertEqual(80, self.truck.earned_money)

    def test_check_for_activities_sleep(self):
        self.truck.earned_money = 1000
        self.truck.check_for_activities(1000)
        self.assertEqual(875, self.truck.earned_money)

    def test_check_for_activities_pump(self):
        self.truck.earned_money = 1500
        self.truck.check_for_activities(1500)
        self.assertEqual(835, self.truck.earned_money)

    def test_check_for_activities_repair_truck(self):
        self.truck.earned_money = 15000
        self.truck.check_for_activities(15000)
        self.assertEqual(625, self.truck.earned_money)

    def test_repr(self):
        self.truck.miles = 10
        self.assertEqual(f"dan has 10 miles behind his back.", self.truck.__repr__())

#---author---

from unittest import TestCase
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver("Kostadin", 1.40)

    def test_init(self):
        self.assertEqual(self.driver.name, "Kostadin")
        self.assertEqual(self.driver.money_per_mile, 1.40)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_add_cargo_valid(self):
        result = self.driver.add_cargo_offer("California", 2000)

        self.assertEqual(result, f"Cargo for 2000 to California was added as an offer.")
        self.assertEqual(self.driver.available_cargos, {"California": 2000})

    def test_add_cargo_invalid(self):
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("California", 2000)

        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_drive_best_cargo_offer_valid(self):
        self.driver.add_cargo_offer("California", 2000)
        self.driver.add_cargo_offer("Los Angeles", 20000)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(result, f"{self.driver.name} is driving 20000 to Los Angeles.")
        self.assertEqual(self.driver.earned_money, 4000)
        self.assertEqual(self.driver.miles, 20000)

    def test_drive_best_cargo_invalid(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_eat(self):
        self.driver.earned_money = 100

        self.driver.eat(250)
        self.driver.eat(500)

        self.assertEqual(self.driver.earned_money, 60)

    def test_sleep(self):
        self.driver.earned_money = 100

        self.driver.sleep(1000)
        self.driver.sleep(2000)

        self.assertEqual(self.driver.earned_money, 10)

    def test_pump_gas(self):
        self.driver.earned_money = 2000

        self.driver.pump_gas(1500)
        self.driver.pump_gas(3000)

        self.assertEqual(self.driver.earned_money, 1000)

    def repair_truck(self):
        self.driver.earned_money = 16000

        self.driver.repair_truck(10000)
        self.driver.repair_truck(20000)

        self.assertEqual(self.driver.earned_money, 1000)

    def test_repr(self):
        self.assertEqual(str(self.driver), "Kostadin has 0 miles behind his back.")
