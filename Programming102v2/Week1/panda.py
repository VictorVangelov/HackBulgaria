class Panda:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def _get_buff(self):
        if self.weight < 1000:
            self.weight += 1

    def eat_bamboo(self):
        self._get_buff()
        return "Nomm nomm nomm!"


dimcho = Panda("Dimcho", 10, 1500)
print(dimcho.age)  # 10
print(dimcho.eat_bamboo())  # "Nomm nomm nomm!"
