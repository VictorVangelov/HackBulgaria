import unittest
from orc import Orc
from weapon import Weapon


class TestOrc(unittest.TestCase):

    def setUp(self):
        self.new_orc = Orc("Yurnero", 100, 100, 1.23)
        self.new_weapon = Weapon("Some Sword", 1, 0)
        self.without_weapon = Weapon("With bare hands", 0, 0)

    def test_init(self):
        self.assertEqual(1.23, self.new_orc.berserk_factor)

    def test_berserk_factor(self):
        self.new_orc._set_berserk_factor(2.5)
        self.assertEqual(2, self.new_orc.berserk_factor)
        self.new_orc._set_berserk_factor(0.5)
        self.assertEqual(1, self.new_orc.berserk_factor)

    def test_berserk_atack(self):
        self.new_orc.equip_weapon(self.new_weapon)
        self.assertEqual(1.23, self.new_orc.attack())
        self.new_orc.equip_weapon(self.without_weapon)
        self.assertEqual(0, self.new_orc.attack())

    # def test_value_error(self):
    #     with self.assertRaises(ValueError):
    #         Orc("Yurnero", 100, 100, 5)

if __name__ == '__main__':
    unittest.main()
