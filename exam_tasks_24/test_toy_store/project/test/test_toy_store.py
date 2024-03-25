import unittest
from project.toy_store import ToyStore


class TestToyStore(unittest.TestCase):
    def setUp(self) -> None:
        self.toy = ToyStore()

    def test_init_dictionaries(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)
