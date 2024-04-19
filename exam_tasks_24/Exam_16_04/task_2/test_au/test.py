import unittest

from project.restaurant import Restaurant


class RestaurantTest(unittest.TestCase):
    name = 'Test'
    capacity = 5

    def setUp(self):
        self.restaurant = Restaurant(self.name, self.capacity)

    def test_init_attributes(self):
        self.assertEqual('Test', self.restaurant.name)
        self.assertEqual(5, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_name__expect_to_raise_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.restaurant.name = ''
        expect = 'Invalid name!'
        actual = str(ex.exception)
        self.assertEqual(expect, actual)

    def test_name__expect_to_raise_space(self):
        with self.assertRaises(ValueError) as ex:
            self.restaurant.name = ' '
        expect = 'Invalid name!'
        actual = str(ex.exception)
        self.assertEqual(expect, actual)

    def test_capacity__expect_to_raise_(self):
        with self.assertRaises(ValueError) as ex:
            self.restaurant.capacity = -5
        expect = 'Invalid capacity!'
        actual = str(ex.exception)
        self.assertEqual(expect, actual)

    def test_get_waiters__expect_empty(self):
        expect = []
        actual = self.restaurant.get_waiters()
        self.assertEqual(expect, actual)

    def test_get_waiters__expect_waiter(self):
        self.restaurant.add_waiter('Pesho')
        expect = [{'name': 'Pesho'}]
        actual = self.restaurant.get_waiters()
        self.assertEqual(expect, actual)

    def test_get_waiters__expect_waiter_min_earnings(self):
        self.restaurant.add_waiter('Pesho')
        self.restaurant.add_waiter('Gosho')
        self.restaurant.waiters[0]['total_earnings'] = 1
        self.restaurant.waiters[1]['total_earnings'] = 5
        expect = [{'name': 'Gosho', 'total_earnings': 5}]
        actual = self.restaurant.get_waiters(min_earnings=2)
        self.assertEqual(expect, actual)

    def test_get_waiters__expect_waiter_max_earnings(self):
        self.restaurant.add_waiter('Pesho')
        self.restaurant.add_waiter('Gosho')
        self.restaurant.waiters[0]['total_earnings'] = 1
        self.restaurant.waiters[1]['total_earnings'] = 5
        expect = [{'name': 'Pesho', 'total_earnings': 1}]
        actual = self.restaurant.get_waiters(max_earnings=2)
        self.assertEqual(expect, actual)

    def test_get_waiters__expect_waiter_min_max_earnings(self):
        self.restaurant.add_waiter('Pesho')
        self.restaurant.add_waiter('Gosho')
        self.restaurant.add_waiter('Minka')
        self.restaurant.waiters[0]['total_earnings'] = 1
        self.restaurant.waiters[1]['total_earnings'] = 5
        self.restaurant.waiters[2]['total_earnings'] = 7
        expect = [{'name': 'Gosho', 'total_earnings': 5}]
        actual = self.restaurant.get_waiters(min_earnings=2, max_earnings=6)
        self.assertEqual(expect, actual)

    def test_add_waiter__expect_to_add(self):
        expect = 'The waiter Pesho has been added.'
        actual = self.restaurant.add_waiter('Pesho')
        self.assertEqual(expect, actual)

    def test_add_waiter__expect_duplicate(self):
        self.restaurant.add_waiter('Pesho')
        expect = 'The waiter Pesho already exists!'
        actual = self.restaurant.add_waiter('Pesho')
        self.assertEqual(expect, actual)

    def test_add_waiter__expect_capacity(self):
        self.restaurant.capacity = 1
        self.restaurant.add_waiter('Pesho')
        expect = 'No more places!'
        actual = self.restaurant.add_waiter('Gosho')
        self.assertEqual(expect, actual)

    def test_remove_waiter__expect_to_remove(self):
        self.restaurant.add_waiter('Pesho')
        expect = 'The waiter Pesho has been removed.'
        actual = self.restaurant.remove_waiter('Pesho')
        self.assertEqual(expect, actual)

    def test_remove_waiter__expect_to_not_remove(self):
        expect = 'No waiter found with the name Pesho.'
        actual = self.restaurant.remove_waiter('Pesho')
        self.assertEqual(expect, actual)

    def test_get_total_earnings__expect_no_waiter(self):
        expect = 0
        actual = self.restaurant.get_total_earnings()
        self.assertEqual(expect, actual)

    def test_get_total_earnings__expect_one_waiter(self):
        self.restaurant.add_waiter('Pesho')
        self.restaurant.waiters[0]['total_earnings'] = 10
        expect = 10
        actual = self.restaurant.get_total_earnings()
        self.assertEqual(expect, actual)

    def test_get_total_earnings__expect_one_plus_waiters(self):
        self.restaurant.add_waiter('Pesho')
        self.restaurant.waiters[0]['total_earnings'] = 10
        self.restaurant.add_waiter('Gosho')
        self.restaurant.waiters[1]['total_earnings'] = 10
        expect = 20
        actual = self.restaurant.get_total_earnings()
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
