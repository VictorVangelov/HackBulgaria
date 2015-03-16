from weapon import Weapon


class Entity:

    def __init__(self, name, health, max_health):
        without_weapon = Weapon("Without weapon", 0, 0)
        self.name = name
        self.health = health
        self.max_health = max_health
        self.has_weapon = False
        self.equipped_weapon = without_weapon

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def take_healing(self, heal):
        if self.health == 0:
            return False
        else:
            self.health += heal
            if self.health > 100:
                self.health = 100
            return True

    def equip_weapon(self, weapon):
        if weapon is None:
            self.has_weapon = False
        else:
            self.equipped_weapon = weapon
            self.has_weapon = True
            print("Weapon equipped")
            return True

    def has_weapons(self):
        if self.has_weapon is True:
            return True
        else:
            return False

    def attack(self):
        if not self.has_weapons():
            return 0
            print("You dont have any weapon equipped")
        elif self.equipped_weapon.critical_hit():
            return self.equipped_weapon.damage * 2
        else:
            return self.equipped_weapon.damage
