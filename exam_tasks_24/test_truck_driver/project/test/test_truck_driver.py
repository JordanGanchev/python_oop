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