import unittest
from hero import Hero
from orc import Orc
from fighting import Fighting
from weapon import Weapon


class TestFighting(unittest.TestCase):

    def setUp(self):
        self.the_hero = Hero("Thanes", 150, 150, "Mountain King")
        self.the_orc = Orc("Yurnero the Blademaster", 150, 150, 1.3)
        self.thanes_hummer = Weapon("Thanes hummer", 15, 0.4)
        self.yurnero_blade = Weapon("Yurneros blade", 10, 0.35)
        self.the_hero.equip_weapon(self.thanes_hummer)
        self.the_orc.equip_weapon(self.yurnero_blade)
        self.some_fight = Fighting(self.the_hero, self.the_orc)

    def test_init(self):
        self.assertEqual(self.some_fight.attacker, self.the_hero)
        self.assertEqual(self.some_fight.defender, self.the_orc)
        self.some_fight.simulate_fight()
        self.assertTrue(
            self.some_fight.attacker or self.some_fight.defender, self.some_fight.winner)

    def test_return_fighters_names(self):
        pass

if __name__ == '__main__':
    unittest.main()
