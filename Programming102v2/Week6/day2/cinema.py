from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from reservations import Reservations
from movies import Movies
from projections import Projections
from session import Base

engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)
# Session is our Data Mapper
session = Session(bind=engine)


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

    def main_menu(self, session):
        self.print_commands()
        while self.QUIT is False:
            input_command = input("enter your command >")
            if not input_command == "help" and not input_command == "quit":
                self.dict_of_commands[input_command](session)
            elif input_command == "help":
                self.print_commands()
            elif input_command == "quit":
                print("bye bye")
                session.commit()
                self.QUIT = True


def main(session):
    cinema = Cinema()
    cinema.main_menu(session)

if __name__ == '__main__':
    main()
