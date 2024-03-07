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
        self.train.passengers.append('lubo', 'emo', 'boris')
        self.train.add('lubo')
        if len(self.train.passengers) == 2:
            self.assertEqual("Train is full", )




