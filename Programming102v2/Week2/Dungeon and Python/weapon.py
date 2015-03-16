import random



class Weapon():

    def __init__(self, name, damage, critical_strike_percent):
        self.name = name
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        some_int = random.random()
        if self.critical_strike_percent > some_int and self.critical_strike_percent != 0:
            return True
        else:
            return False
