import unittest
from entity import Entity
from weapon import Weapon


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.new_entity = Entity("Chen", 100, 100)
        self.new_weapon = Weapon("Some Sword", 1, 0)
        self.some_weapon = Weapon("Some Sword", 1, 1)

    def test_init_entity(self):
        self.assertEqual("Chen", self.new_entity.name)
        self.assertEqual(100, self.new_entity.health)
        self.assertEqual(100, self.new_entity.max_health)

    def test_get_health(self):
        self.assertEqual(100, self.new_entity.get_health())

    def test_is_alive(self):
        self.assertTrue(self.new_entity.is_alive())

    def test_take_damage(self):
        self.new_entity.take_damage(5.5)
        self.assertEqual(self.new_entity.health, 94.5)
        self.new_entity.take_damage(95)
        self.assertEqual(self.new_entity.health, 0)

    def test_take_healing(self):
        self.new_entity.take_healing(11)
        self.assertEqual(100, self.new_entity.health)
        self.new_entity.take_damage(15)
        self.new_entity.take_healing(16)
        self.assertEqual(100, self.new_entity.health)
        self.new_entity.take_damage(111)
        self.assertFalse(self.new_entity.take_healing(1))
        self.new_entity.health = 10
        self.assertTrue(self.new_entity.take_healing(1))

    def test_has_weapon(self):
        self.assertFalse(self.new_entity.has_weapon)
        self.assertEqual(0, self.new_entity.attack())
        self.new_entity.equip_weapon(self.new_weapon)
        self.assertEqual(1, self.new_entity.attack())
        self.assertTrue(self.new_entity.has_weapon)
        self.new_entity.equip_weapon(self.some_weapon)
        self.assertEqual(2, self.new_entity.attack())

if __name__ == '__main__':
    unittest.main()
