import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):

    def setUp(self) -> None:
        self.train = Train('dan', 100)

    def test_class_value(self):
        self.assertEqual("Train is full", Train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", Train.PASSENGER_EXISTS )
        self.assertEqual("Passenger Not Found", Train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", Train.PASSENGER_ADD)
        self.assertEqual("Removed {}", Train.PASSENGER_REMOVED)
        self.assertEqual(0, Train.ZERO_CAPACITY)

    def test_init_element(self):
        self.assertEqual('dan', self.train.name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger(self):
        self.train.passengers.append('boris')
        self.train.capacity = 1
        with self.assertRaises(ValueError) as content:
            self.train.add('monk')
        self.assertEqual("Train is full", str(content.exception))

    def test_add_name_if_name_in_passenger(self):
        self.train.passengers.append('boris')
        with self.assertRaises(ValueError) as content:
            self.train.add('boris')
        self.assertEqual(Train.PASSENGER_EXISTS.format('boris'), str(content.exception))

    def test_add_name_if_not_in_passenger(self):
        self.train.passengers.append('boris')
        self.train.add('monk')
        self.assertEqual(self.train.passengers, ['boris', 'monk'])

    def test_remove_if_not_in_passenger(self):
        with self.assertRaises(ValueError) as content:
            self.train.remove('monk')
        self.assertEqual(Train.PASSENGER_NOT_FOUND.format('monk'), str(content.exception))

    def test_remove_if_have_passenger(self):
        self.train.passengers.append('boris')
        self.train.remove('boris')
        self.assertEqual(self.train.passengers, [])
