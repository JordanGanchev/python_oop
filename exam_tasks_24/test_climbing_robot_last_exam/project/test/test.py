import unittest
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(unittest.TestCase):

    def setUp(self) -> None:
        self.climb = ClimbingRobot('Mountain', 'mobil', 100, 1000)

    def test_init_method(self):
        self.assertEqual('Mountain', self.climb.category)
        self.assertEqual('mobil', self.climb.part_type)
        self.assertEqual(100, self.climb.capacity)
        self.assertEqual(1000, self.climb.memory)
        self.assertEqual([], self.climb.installed_software)
        self.assertEqual(['Mountain', 'Alpine', 'Indoor', 'Bouldering'], ClimbingRobot.ALLOWED_CATEGORIES)

    def test_setter_category(self):
        with self.assertRaises(ValueError) as context:
            self.climb.category = 'robot'
        self.assertEqual(f"Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']", str(context.exception))

    def test_get_used_capacity(self):
        self.climb.installed_software.append({'capacity_consumption': 10, 'memory_consumption': 20})
        self.assertEqual(10, self.climb.get_used_capacity())

    def test_get_used_memory(self):
        self.climb.installed_software.append({'capacity_consumption': 10, 'memory_consumption': 20})
        self.assertEqual(20, self.climb.get_used_memory())