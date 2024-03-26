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

    def test_add_toy_if_not_key(self):
        with self.assertRaises(Exception) as content:
            self.toy.add_toy("J", 'lemon')
        self.assertEqual("Shelf doesn't exist!", str(content.exception))

    def test_add_toy_if_not_value(self):
        with self.assertRaises(Exception) as ex:
            self.toy.toy_shelf["J"] = "T"
            self.toy.add_toy("J", 'T')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_if_is_not_none(self):
        with self.assertRaises(Exception) as ex:
            self.toy.toy_shelf["J"] = "T"
            self.toy.add_toy("J", 'R')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_end_position(self):
        self.assertEqual(f"Toy:T placed successfully!", self.toy.add_toy('A', "T"))
        self.assertEqual(
            {
                "A": "T",
                "B": None,
                "C": None,
                "D": None,
                "E": None,
                "F": None,
                "G": None,
            }, self.toy.toy_shelf
        )

    def test_remove_toy_if_not_in_dictionaries(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy('J', "T")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_if_name_difference(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy('A', 'T')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_end_position(self):
        self.toy.toy_shelf['A'] = 'B'
        result = self.toy.remove_toy("A", 'B')
        self.assertEqual(f"Remove toy:B successfully!", result)
        self.assertEqual(
            {
                "A": None,
                "B": None,
                "C": None,
                "D": None,
                "E": None,
                "F": None,
                "G": None,
            }, self.toy.toy_shelf
        )
