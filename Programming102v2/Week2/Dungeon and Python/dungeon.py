from hero import Hero
from fighting import Fighting
from weapon import Weapon
from random import shuffle
from potion import Potion

#script, text_file = argv


class Dungeon():

    def __init__(self, maps_file):
        self.maps_file = maps_file
        self.current_user = object
        self.mark = ""
        self.dict_of_herous = {}
        self.number_of_rows = 0
        self.number_of_chars = 0
        self.current_x = 0
        self.current_y = 0
        self.wanted_x = 0
        self.wanted_y = 0
        self.EXIT = False
        self.refreshed_map = [[]]
        self.dict_of_items = {}
        self.dict_champion_name = {}
        self.player_names_list = []
        self.list_of_commands = []
        self.available_commands = "load_map <map_name.txt>\nshow_map\nspawn_weapons\nmake_new_hero <name> <max_health> <nickname>\n",
        "make_new_orc <name> <max_health> <berserk_factor>\nmove <name> <way>",
        "\nspawn_player <name> <entity>\nprint_available_entitys"

    def load_map(self, map_file):
        self.map_file = map_file
        file = open(self.maps_file, "r")
        map_file = file.read()
        my_map = map_file.split("\n")
        my_map.reverse()
        self.number_of_rows = len(my_map)
        self.number_of_chars = len(my_map[0])
        loaded_map = [
            [0] * self.number_of_chars for i in range(self.number_of_rows,)]

        for row_num, context in enumerate(list(my_map)):
            # print(context)
            for num_ch, ch in enumerate(list(context)):
                loaded_map[row_num][num_ch] = (ch)
        # print(loaded_map)
        loaded_map.reverse()
        file.close()
        self.refreshed_map = loaded_map
        # print(self.refreshed_map[0])
        # print(self.refreshed_map[0])

    def show_map(self):
        for row in self.refreshed_map:
            print ("".join(row))

    def spawn_player(self, player_name, entity):
        if isinstance(entity, Hero):
            self.mark = "H"
        else:
            self.mark = "O"
            self.dict_champion_name[entity] = player_name
        for row_num, row in enumerate(self.refreshed_map):
            the_row = list(row)
            if 'S' in the_row:
                self.dict_of_herous[entity] = [row_num, row.index("S")]
                the_row[the_row.index("S")] = self.mark
                stringed_row = "".join(the_row)
                self.refreshed_map[row_num] = stringed_row
                print("True")
                return True
        print("False")
        return False

    def take_random_item(self, mark):
        if mark == "W":
            list_of_weapons = []
            for weapon in self.dict_of_items:
                if isinstance(self.dict_of_items[weapon], Weapon):
                    list_of_weapons.append(weapon)
            shuffle(list_of_weapons)
            return list_of_weapons[0]
        elif mark == "P":
            list_of_potions = []
            for potion in self.dict_of_items:
                if isinstance(self.dict_of_items[potion], Potion):
                    list_of_potions.append(potion)
            shuffle(list_of_potions)
            return list_of_potions[0]

    def spawn_item(self, item, x_coord, y_coord):
        if x_coord < self.number_of_rows and y_coord < self.number_of_chars:
            if isinstance(item, Potion):
                self.refreshed_map[x_coord, y_coord] = "P"
                self.dict_of_items[item] = [x_coord, y_coord]
            elif isinstance(item, Weapon):
                self.refreshed_map[x_coord, y_coord] = "W"
                self.dict_of_items[item] = [x_coord, y_coord]
        else:
            print(
                "coordinates must be [0-{}, 0-{}".format(self.number_of_rows - 1, self.number_of_chars - 1))

    def spawn_all_items(self):
        for row_num, row in enumerate(self.refreshed_map):
            if 'W' in list(row):
                self.dict_of_items[
                    take_random_item('W')] = [row_num, row.index("W")]
                print("True")
            elif "P" in list(row):
                self.dict_of_items[
                    take_random_item('P')] = [row_num, row.index("P")]
                print("True")

    def find_fighter(self):
        for fighter in self.dict_of_herous:
            if self.dict_of_herous[fighter] == [self.wanted_x, self.wanted_y]:
                return fighter
            else:
                print("there is no fighter there")
                return False

    def move(self, player_name, direction):
        self.validate_player_name(player_name)
        if direction == "up":
            if self.can_move_up():
                self.execute_move(-1, 0)
                print("True")
            else:
                print("False")
        elif direction == "down":
            if self.can_move_down():
                self.execute_move(1, 0)
                print("True")
            else:
                print("False")
        elif direction == "left":
            if self.can_move_left():
                self.execute_move(0, -1)
                print("True")
            else:
                print("False")
        elif direction == "right":
            if self.can_move_right():
                self.execute_move(0, 1)
                print("True")
            else:
                print("False")
        else:
            print("wrong direction, please use up, down, left or right")

    def begin_fight(self):
        defender = self.find_fighter()
        new_fight = Fighting(self.current_user, defender)
        if new_fight.winner == self.current_user:
            return True
        else:
            return False

    def print_potion_info(self):
        potion = self.dict_of_items(self.wanted_x, self.wanted_y)
        print ("{}\nHealing point:{}".format(
            potion.name, potion.healing_points))

    def print_weapon_info(self):
        item = self.dict_of_items(self.wanted_x, self.wanted_y)
        print("{}\nDamage:{}\nCritical chance:{}\n".format(
            item.type, item.damage, item.critical_strike_percent))

    def ask_question(self, mark):
        if mark == "O" or mark == "H":
            print(
                "There is a enemy , do you wanna attack him ?\n type yes or no")
            if input("> ") == "yes":
                return 1
            else:
                return 0
        elif mark == "W":
            print("You found a weapon")
            self.print_weapon_info()
            print ("Do you wanna equip it ?")
            if input("> ") == "yes":
                return 2
            else:
                return 3
        elif mark == "P":
            print(
                "You found a potion, do u wanna heal your self?\ntype yes or no")
            if input("> ") == "yes":
                return 4
            else:
                return 3

    def change_coordinates(self):
        self.refreshed_map[self.current_x, self.current_y] = '.'
        self.refreshed_map[self.wanted_x, self.wanted_y] = self.mark
        self.dict_of_herous[self.current_user] = [self.wanted_x, self.wanted_y]

    def execute_move(self, x, y):
        self.current_x = self.dict_of_herous[self.current_user[0]]
        self.current_y = self.dict_of_herous[self.current_user[1]]

        wanted_position = self.refreshed_map[self.wanted_x, self.wanted_y]
        if self.ask_question(wanted_position) == 0:
            print("False")
        elif self.ask_question(wanted_position) == 1:
            if self.begin_fight():
                self.change_coordinates()
                print("True")
            else:
                print("Screw you mada faka, you are dead")
                print("False")  # to retrun main_menU()
        elif self.ask_question(wanted_position) == 2:
            self.current_user.equip_weapon(
                self.dict_of_items(self.wanted_x, self.wanted_y))

            self.change_coordinates()
            print("True")
        elif self.ask_question(wanted_position) == 3:
            self.change_coordinates()
            print("True")
        elif self.ask_question(wanted_position) == 4:
            self.current_user.take_healing(
                self.dict_of_items([self.wanted_x, self.wanted_y]).healing_points)
            self.change_coordinates()
            print("True")

    def can_move_up(self, x, y):
        try:
            self.wanted_x = self.current_x + x
            self.wanted_y = self.current_y + y
        except (IndexError, TypeError):
            return False
        if self.current_x > 0 and self.refreshed_map[self.wanted_x][self.wanted_y] != '#':
            return True
        else:
            return False

    def can_move_left(self, x, y):
        try:
            self.wanted_x = self.current_x + x
            self.wanted_y = self.current_y + y

        except (IndexError, TypeError):
            return False
        if self.current_y > 0 and self.refreshed_map[self.wanted_x][self.wanted_y] != '#':
            return True
        else:
            return False

    def can_move_down(self, x, y):
        try:
            self.wanted_x = self.current_x + x
            self.wanted_y = self.current_y + y
        except (IndexError, TypeError):
            return False
        if self.current_x < self.number_of_rows - 1 and self.refreshed_map[self.wanted_x][self.wanted_y] != '#':
            return True
        else:
            return False

    def can_move_right(self, x, y):
        try:
            self.wanted_x = self.current_x + x
            self.wanted_y = self.current_y + y
        except (IndexError, TypeError):
            return False
        if self.current_y < self.number_of_chars - 1 and self.refreshed_map[self.wanted_x][self.wanted_y] != '#':
            return True
        else:
            return False

    def validate_player_name(self, player_name):
        for champion in self.dict_champion_name:
            self.player_names_list.append(self.dict_champion_name[champion])
            if player_name == self.dict_champion_name[champion]:

                print(self.dict_of_herous[champion])
                print(self.current_x)
                #self.current_y = self.dict_of_herous[champion][1]
                #print(self.current_y)
                return champion
        print("There is no Entity with this name, please use some of this:\n")
        names = ("\n".join(self.player_names_list))
        print(names)

    def input_comand(self):
        the_input = input("Enter a command: ")
        self.list_of_commands = the_input.split()

    def make_new_hero(self, name, max_health, nickname):
        the_hero = Hero(name, max_health, max_health, nickname)
        self.dict_of_herous["hero"].add(the_hero)

    def make_new_orc(self, name, max_health, berserk_factor):
        the_orc = Orc(name, max_health, max_health, berserk_factor)
        self.dict_of_herous["orc"].add(the_orc)

    def ask_to_quit(self):
        exit_answer = input("are you shure m that u wanna quit ?(type yes or no)")
        if exit_answer == "yes":
            self.EXIT = True

    def print_available_entitys(self):
        content = ""
        for entity in self.dict_of_herous:
            content += "{}:\n".format(entity)
            for name in self.dict_of_herous[entity]:
                content += "{}\n".format(name)
        print(content)

def main():
    pass
if __name__ == '__main__':
    a = Dungeon("map.txt")
    a.read_map()
    # print(a.refreshed_map)
    # print(self.number_of_chars)
