import unittest
from hero import Hero
from orc import Orc
from fighting import Fighting
from weapon import Weapon
from potion import Potion
from dungeon import Dungeon
from fighting import Fighting
from entity import Entity



class TestDungeon(unittest.TestCase):

    def setUp(self):

        self.without_weapon = Weapon("With bare hands", 0, 0)
        self.thanes_hummer = Weapon("Thanes hummer", 15, 0.4)
        self.yurnero_blade = Weapon("Yurneros blade", 10, 0.35)
        self.the_hero = Hero("Thanes", 150, 150, "Mountain King")
        self.the_orc = Orc("Yurnero the Blademaster", 150, 150, 1.3)
        self.the_chen = Orc("Chen", 150, 150, 1.3)
        self.small_potion = Potion("Small potion", 15)
        self.midium_potion = Potion("Midium potion", 25)
        self.the_hero.equip_weapon(self.thanes_hummer)
        self.the_orc.equip_weapon(self.yurnero_blade)
        self.map = Dungeon("map.txt")
        self.map.read_map()
        self.map.dict_of_items[self.yurnero_blade] = []
        self.map.dict_of_items[self.thanes_hummer] = []
        self.map.dict_of_items[self.small_potion] = []
        self.map.dict_of_items[self.midium_potion] = []
        self.map.dict_of_herous[self.the_orc] = []
        self.map.dict_of_herous[self.the_hero] = []
        self.map.spawn_player("shosho", self.the_hero)
        #self.map.spawn_player("kosho", self.the_orc)
        #self.map.dict_champion_name[self.the_hero] = "shosho"
        self.map.dict_champion_name[self.the_orc] = "kosho"



    #def test_validate_player(self):
    #    self.assertEqual(self.the_hero, self.map.validate_player_name("hero"))
    def test_spawn_player(self):
        #self.assertFalse(self.map.spawn_player("shosho", self.the_hero))
        self.assertTrue(self.map.spawn_player("kosho", self.the_orc))
        self.assertFalse(self.map.spawn_player("kosho", self.the_chen))

    def test_can_move(self):
        #print("{}\n{}".format(self.map.number_of_rows, self.map.number_of_chars))
        #print((self.map.number_of_rows))
        self.current_user = self.the_orc
        self.map.print_map()

        self.assertFalse(self.map.can_move_up(-1, 0))
        self.assertFalse(self.map.can_move_down(1, 0))
        self.assertTrue(self.map.can_move_right(0, 1))
        self.map.validate_player_name("orc")
        print("{}     {}".format(self.map.current_x, self.map.current_y))
        self.assertFalse(self.map.can_move_up(-1, 0))
        self.assertFalse(self.map.can_move_down(1, 0))
        self.assertTrue(self.map.can_move_right(0, 1))
        self.assertFalse(self.map.can_move_left(0, -1))

    def test_validate_player_name(self):

        self.map.spawn_player("kosho", self.the_orc)
        self.assertEqual(self.map.validate_player_name("kosho"), self.the_orc)
        self.map.print_map()

if __name__ == '__main__':
    unittest.main()
