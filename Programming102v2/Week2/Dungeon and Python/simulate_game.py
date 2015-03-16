from dungeon import Dungeon
from weapon import Weapon
from orc import Orc
from hero import Hero
from potion import Potion


class SimulateGame():

    def __init__(self, map_name):
        self.dugneon = Dungeon(map_name)
        self.command1 = ""
        self.command2 = ""
        self.command3 = ""
        self.command4 = ""

    def main():
        game = SimulateGame("map.txt")
        game.execute_necessary_inits()
        while game.dungeon.EXIT is False:
            game.dungeon.show_map()
            game.dungeon.input_comand()
            game.recognize_commands()
            game.execute_command()

    def execute_necessary_inits(self):
        thanes_hummer = Weapon("Thanes hummer", 15, 0.4)
        yurnero_blade = Weapon("Yurneros blade", 10, 0.35)
        the_hero = Hero("Thanes", 150, 150, "Mountain King")
        the_orc = Orc("Yurnero the Blademaster", 150, 150, 1.3)
        small_potion = Potion("Small potion", 15)
        midium_potion = Potion("Midium potion", 25)
        the_hero.equip_weapon(thanes_hummer)
        the_orc.equip_weapon(yurnero_blade)
        self.dungeon.dict_of_items[yurnero_blade] = []
        self.dungeon.dict_of_items[thanes_hummer] = []
        self.dungeon.dict_of_items[small_potion] = []
        self.dungeon.dict_of_items[midium_potion] = []
        self.dungeon.dict_of_herous[the_orc] = []
        self.dungeon.dict_of_herous[the_hero] = []

    def recognize_commands(self):
        if len(self.dungeon.list_of_commands) == 1:
            self.command1 = self.dungeon.list_of_commands[0]
        elif len(self.dungeon.list_of_commands) == 2:
            self.command1 = self.dungeon.list_of_commands[0]
            self.command2 = self.dungeon.list_of_commands[1]
        elif len(self.dungeon.list_of_commands) == 3:
            self.command1 = self.dungeon.list_of_commands[0]
            self.command2 = self.dungeon.list_of_commands[1]
            self.command3 = self.dungeon.list_of_commands[2]
        elif len(self.dungeon.list_of_commands) == 4:
            self.command1 = self.dungeon.list_of_commands[0]
            self.command2 = self.dungeon.list_of_commands[1]
            self.command3 = self.dungeon.list_of_commands[2]
            self.command4 = self.dungeon.list_of_commands[3]
        else:
            print("wrong command")
            self.dungeon.input_comand()

    def execute_command(self):
        if self.dungeon.list_of_commands[0] == "load_map":
            self.dugneon.load_map(self.dungeon.list_of_commands[1])
        elif self.dungeon.list_of_commands[0] == "spawn_weapons":
            self.dungeon.spawn_all_items()
        elif self.dungeon.list_of_commands[0] == "make_ner_hero":
            self.dungeon.make_new_hero(self.command2, self.command3, self.command3, self.command4)
        elif self.dungeon.list_of_commands[0] == "make_ner_orc":
            self.dungeon.make_new_hero(self.command2, self.command3, self.command3, self.command4)
        elif self.dungeon.list_of_commands[0] == "move":
            self.dungeon.move(self.command2, self.command3)
        elif self.dungeon.list_of_commands[0] == "exit":
            self.dungeon.ask_to_quit()
        else:
            print("wrong command")
            self.dungeon.input_comand()
