import sqlite3
from reservations import Reservations
from movies import Movies
from projections import Projections


class Cinema:

    def __init__(self):
        self.QUIT = False
        self.dict_of_commands= {"help": Cinema.print_commands,
         "show_projections": Projections.get_all,
        "asd": Reservations.make_a_reservation,
        "show_reservations":Reservations.get_all,
        "show_movies": Movies.get_all}

    def help(self):
        return self.dict_of_commands.keys()

    def print_commands(self):
        for command in sorted(self.help()):
            print(command)

    def main_menu(self, cursor, connection):
        self.print_commands()
        while self.QUIT is False:
            input_command = input("enter your command >")
            if not input_command == "help" and not input_command == "quit":
                self.dict_of_commands[input_command](cursor, connection)
            elif input_command == "help":
                self.print_commands()
            elif input_command == "quit":
                print("bye bye")
                connection.commit()
                self.QUIT = True




def main():
    connection = sqlite3.connect('cinema')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cinema(id INTEGER PRIMARY KEY,
    name TEXT)''')
    Projections.load_reservations()
    connection.commit()
    Reservations.create_database(connection, cursor)
    Projections.create_database(connection, cursor)
    Movies.create_database(connection, cursor)
    cinema = Cinema()
    cinema.main_menu(cursor, connection)
    #cinema.print_commands()
    # # projections.init_free_hall()
    # # projections.reserv_seat(1,1,10)
    # Projections.load_reservations()
    # Projections.print_projection_seats(1)
    # # projections.update_the_json_file()
    # # projections.add_old(connection, cursor)
    # reservation.add_old(connection, cursor)
    # movies.add_old(connection, cursor)
    #movies.get_all(cursor)
    #reservation.get_all(cursor)
    #projections.get_all_for(cursor,2)
    #projections.get_all(cursor)
    # db_is_closed = False

if __name__ == '__main__':
    main()
