import unittest
from weapon import Weapon


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.short_sword = Weapon("Short Sword", 10, 0.1)

    def test_init(self):
        self.assertEqual("Short Sword", self.short_sword.name)
        self.assertEqual(10, self.short_sword.damage)
        self.assertEqual(0.1, self.short_sword.critical_strike_percent)

    def test_critical_hit(self):
        list_of_booleans = []
        for i in range(0, 1000):
            list_of_booleans.append(self.short_sword.critical_hit())
        self.assertIn(True, list_of_booleans)
        self.assertIn(False, list_of_booleans)

if __name__ == '__main__':
    unittest.main()
