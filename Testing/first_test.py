import unittest
from random import random
from unittest import TestCase


class FirstTests(TestCase):
    x = None

    @classmethod
    def setUpClass(cls) -> None:
        '''
        Runs once before all tests
        :return:
        '''
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        '''
        Runs **before** each test
        :return:
        '''
        pass

    def tearDown(self) -> None:
        '''
        Runs **after** each test
        :return:
        '''
        pass

    def setUp(self) -> None:
        '''
        Runs before each test
        :return:
        '''
        self.x = random()

    def test_expect_1_to_equal_1(self):
        self.assertEqual(1, 1)

    def test_expect_1_to_equal_2(self):
        self.assertEqual(1, 2)

    def test_assertTrue(self):
        self.assertTrue(True)
        self.assertTrue(1 == 2)

    def test_assertListEqual(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3])
        self.assertListEqual([1, 2, 3], [1, 1, 3])


if __name__ == '__main__':
    unittest.main()
