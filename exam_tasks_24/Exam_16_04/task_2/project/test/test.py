import unittest

from project.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):
    def setUp(self) -> None:
        self.rest = Restaurant('tara', 10)

    def test_init_method(self):
        self.assertEqual('tara', self.rest.name)
        self.assertEqual(10, self.rest.capacity)
        self.assertEqual([], self.rest.waiters)

    def test_setter_valid_name(self):
        with self.assertRaises(ValueError) as content:
            self.rest.name = '   '
        self.assertEqual("Invalid name!", str(content.exception))

    def test_setter_capacity(self):
        with self.assertRaises(ValueError) as content:
            self.rest.capacity = -1
        self.assertEqual("Invalid capacity!", str(content.exception))

    def test_add_waiter_if_len_waiters(self):
        self.rest.waiters.append('w')
        self.rest.capacity = 1
        self.assertEqual("No more places!", self.rest.add_waiter('tara'))

    def test_add_waiter_if_len_waiters_name(self):
        self.rest.capacity = 1
        self.assertEqual(f"The waiter tara has been added.", self.rest.add_waiter('tara'))

    def test_remove_waiter_not_in_list(self):
        self.assertEqual(f"No waiter found with the name wer.", self.rest.remove_waiter('wer'))

    def test_remove_waiter_if_list(self):
        self.rest.waiters.append({'name': 'wer'})
        self.assertEqual(f"The waiter wer has been removed.", self.rest.remove_waiter('wer'))

    def test_get_total_earnings(self):
        self.assertEqual(0, self.rest.get_total_earnings())

