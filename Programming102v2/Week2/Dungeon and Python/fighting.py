from random import random
from orc import Orc
from hero import Hero


class Fighting():

    def __init__(self, attacker, deffender):
        self.attacker = attacker
        self.deffender = deffender
        self.winner = object

    def flip_the_coint(self):
        if random() < 0.5:
            return 1
        else:
            return 0

    def change_the_atacker(self):
        # temp = self.attacker
        # self.attacker = self.deffender
        # self.deffender = temp
        self.attacker, self.deffender = self.deffender, self.attacker


    def return_attacker_name(self, attacker):
        if isinstance(attacker, Orc):
            return attacker.name
        else:
            return attacker.known_as()

    def return_deffender_name(self, deffender):
        if isinstance(deffender, Orc):
            return deffender.name
        else:
            return deffender.known_as()

    def heal_the_fighters(self):
        self.attacker.health = self.attacker.max_health
        self.deffender.health = self.deffender.max_health

    def simulate_fight(self):
        if self.flip_the_coint() == 0:
            self.change_the_atacker()
        while(self.attacker.health == 0):
            the_attack_damage = self.attacker.atack()
            self.deffender.take_damage(the_attack_damage)
            print("{} atacked the {} and reduce his life points by {}").format(
                self.return_attacker_name(self.attacker), self.return_deffender_name(self.deffender), the_attack_damage)
            self.change_the_atacker()
        print("The winner is {}".format(self.return_deffender_name(self.deffender)))
        self.winner = self.deffender
        self.heal_the_fighters()
