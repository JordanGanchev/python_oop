import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.paint = PaintFactory('house', 100)

    def test_init_factory(self):
        valid_ingredients = 5
        ingredients = ["white", "yellow", "blue", "green", "red"]
        self.assertEqual('house', self.paint.name)
        self.assertEqual(100, self.paint.capacity)
        self.assertEqual(valid_ingredients, len(self.paint.valid_ingredients))
        self.assertEqual(ingredients, self.paint.valid_ingredients)

    def test_add_ingredient(self):
        self.paint.add_ingredient("white", 10)
        self.assertEqual({'white': 10}, self.paint.ingredients)

    def test_add_not_ingredient(self):
        self.paint.capacity = 0
        with self.assertRaises(ValueError) as content:
            self.paint.add_ingredient("white", 10)
            self.paint.can_add(-10)
        self.assertEqual("Not enough space in factory", str(content.exception))

    def test_add_negative_case(self):
        with self.assertRaises(TypeError) as content:
            self.paint.add_ingredient("black", 10)
        self.assertEqual(f"Ingredient of type black not allowed in PaintFactory", str(content.exception))

    def test_remove_ingredient(self):
        self.paint.ingredients['white'] = 10
        self.paint.remove_ingredient('white', 10)
        self.assertEqual({'white': 0}, self.paint.ingredients)

    def test_remove_not_ingredient(self):
        with self.assertRaises(ValueError) as context:
            self.paint.ingredients['white'] = 0
            self.paint.remove_ingredient('white', 10)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test_remove_when_ingredient_not_exist(self):
        self.paint.ingredients['white'] = 10
        with self.assertRaises(KeyError) as content:
            self.paint.remove_ingredient('black', 20)
        self.assertEqual("'No such ingredient in the factory'", str(content.exception))

    # def test_products(self):
    #     result = self.paint.ingredients['white'] = 10
    #     expect = self.paint.products()
    #     self.assertEqual(result, expect)

    def test_products(self):
        self.paint.ingredients['white'] = 10
        expected = {'white': 10}
        result = self.paint.products
        self.assertEqual(expected, result)
