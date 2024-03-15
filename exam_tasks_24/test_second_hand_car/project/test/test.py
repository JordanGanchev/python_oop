import unittest
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(unittest.TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar('volvo', 'xc90', 10000, 100000)

    def test_init_method(self):
        self.assertEqual('volvo', self.car.model)
        self.assertEqual('xc90', self.car.car_type)
        self.assertEqual(10000, self.car.mileage)
        self.assertEqual(100000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_setter_price(self):
        with self.assertRaises(ValueError) as container:
            self.car.price = 0.0
        self.assertEqual('Price should be greater than 1.0!', str(container.exception))

    def test_setter_mileage(self):
        with self.assertRaises(ValueError) as context:
            self.car.mileage = 90
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(context.exception))

    def test_set_promotional_price_if_price_bigger_from_price(self):
        self.car.price = 110
        with self.assertRaises(ValueError) as content:
            self.car.set_promotional_price(120)
        self.assertEqual('You are supposed to decrease the price!', str(content.exception))

    def test_set_promotional_price_if_price_less_from_price(self):
        self.car.price = 120
        self.assertEqual('The promotional price has been successfully set.', self.car.set_promotional_price(110))
        self.assertEqual(110, self.car.price)

    def test_need_repair_if_repair_prise_is_bigger(self):
        self.car.price = 10
        self.assertEqual('Repair is impossible!', self.car.need_repair(10, 's80'))

    def test_need_repair_if_repair_prise_is_less(self):
        self.car.price = 20
        self.assertEqual(f'Price has been increased due to repair charges.', self.car.need_repair(10, 's80'))
        self.assertEqual(30, self.car.price)
        self.assertEqual(['s80'], self.car.repairs)

    def test_gt_if_car_type_not_equal_value(self):
        car1 = SecondHandCar('volvo', 'xc90', 10000, 100000)
        car2 = SecondHandCar('volvo', 's80', 10000, 100000)
        result = car1 > car2
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_gt_if_car_type_equal_value(self):
        car1 = SecondHandCar('volvo', 'xc90', 10000, 100000)
        car2 = SecondHandCar('volvo', 's80', 10000, 100000)
        result = car1 > car2
        self.assertTrue(self.__gt__, result)

    def test_str_method(self):
        self.assertEqual(f"Model volvo | Type xc90 | Milage 10000km\n"
                         f"Current price: 100000.00 | Number of Repairs: 0", self.car.__str__())
