from entity import Entity


class Hero(Entity):
    def __init__(self, name, health, max_health, nickname):
        super().__init__(name, health, max_health)
        self.nickname = nickname

    def known_as(self):
        return (self.name + " the " + self.nickname)
