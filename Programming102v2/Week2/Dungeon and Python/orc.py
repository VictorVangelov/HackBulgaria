from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, max_health, berserk_factor):
        super().__init__(name, health, max_health)
        self._set_berserk_factor(berserk_factor)

    def _set_berserk_factor(self, berserk_factor):
        if berserk_factor < 2 and berserk_factor > 1:
            self.berserk_factor = berserk_factor
        elif berserk_factor > 2:
            self.berserk_factor = 2
        else:
            self.berserk_factor = 1

    def attack(self):
        return super().attack() * self.berserk_factor




        # else:
        #     raise ValueError
