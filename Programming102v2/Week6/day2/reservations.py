from movies import Movies
from projection import Projections
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Reservations():

    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    projection_id = Column(Integer, ForeignKey("Projections.id", nullable=False))
    row = Column(Integer, nullable=False)
    col = Column(Integer, nullable=False)
    projection = relationship("Projections", backref="reservations")


    def __str__(self):
        return "{} - {} - {} - {}".format(self.username, self.projection_id, self.row, self.col)

    def __repr__(self):
        return self.__str__()

    def add(session, user_name, projections_id, the_row, the_col):
        session.execute(Projections(username=user_name,
                                    projection_id=projections_id, row=the_row, col=the_col))
        session.commit()

    def get_all_for(session, movie_id):
        reservations = session.query(Reservations).filter(
            Reservations.projection_id == movie_id)
        return reservations

    def get_all(session):
        reservations = session.query(Reservations)
        return reservations
        # for reseravion in reservations:
        #     print(reseravion)

    def add_old(session):
        session.add_all([Reservations("RadoRado", 1, 2, 1),
                         Reservations("RadoRado", 1, 3, 5),
                         Reservations("RadoRado", 1, 7, 8),
                         Reservations("Ivo", 3, 1, 1),
                         Reservations("Ivo", 3, 1, 2),
                         Reservations("Mysterious", 5, 2, 3),
                         Reservations("Mysterious", 5, 2, 4)])
        session.commit()

    def init_new_seats():
        dict_of_projec = {}
        for row in range(1, 11):
            dict_of_projec[row] = [
                ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
        return dict_of_projec

    def reserv_seat(session, projection_id, row, col):
        if Reservations.validate_row_and_col_input(row, col):
            current_projection = Projections.dict_of_projections[projection_id]
            current_row = current_projection[row]
            if current_row[int(col) - 1] != Projections.TAKEN_SEAT:
                current_row[int(col) - 1] = Projections.TAKEN_SEAT
                print("You take the seat {}-{}".format(row, col))
                Reservations.reduce_available_seats(
                    session, projection_id)
            else:
                print("This seat is already taken!")
                return Reservations.choose_seats(session, projection_id)
        else:
            print("Lol...NO!")
            return Reservations.choose_seats(session, projection_id)

    def reduce_available_seats(session, projection):
        proj = int(projection)
        projection = session.query(Projections).filter(
            Projections.movie_id == proj)
        projection.available_spots -= 1
        session.commit()

    def validate_row_and_col_input(row, col):
        if not (int(row) > Projections.NUMBER_OF_ROWS or int(row) < 1):
            if (int(col) > Projections.NUMBER_OF_COLS or Projections.NUMBER_OF_COLS < 1):
                return False
            else:
                return True
        else:
            return False

    def make_a_reservation(session):
        seats = []
        username = input("Enter username > ")
        number_of_tickets = input("Enter the number of tickets > ")
        Movies.get_all(session)
        movie_id = input("Choose a projection >")
        Projections.get_all_for(session, movie_id)
        projection_id = input("Enter the wanted projection")
        for x in range(1, int(number_of_tickets) + 1):
            seats.append(
                Reservations.choose_seats(session, projection_id))
        Reservations.print_reservation(
            session, username, movie_id, projection_id, seats)
        Reservations.confirm(session, username, projection_id, seats)

    def print_reservation(session, username, movie_id, projection_id, seats):
        result = session.query(Projections, Movies).filter(
            Movies.id == movie_id, Projections.id == projection_id)
        reserved_seats = ""
        for seat in seats:
            reserved_seats += str(seats) + "\n"
        print("Movie : {} ({})\n Date And Time : {} {} ({})\n{}".format(result.name,
            result.rating, result.data, result.time, reserved_seats))

    def confirm(session, username, projection_id, seats):
        confirm = input("To confirm the reservation - type 'finalize' > ")
        if confirm.lower() == 'finalize':
            for seat in seats:
                Reservations.add(
                    session, username, projection_id, seat[0], seat[1])
        elif confirm.lower() == "quit":
            print("You canceld the order, bye bye")
        else:
            print(
                "Lol , u cant type 1 word correctly, try again or type 'Quit'")
            Reservations.confirm(
                session, username, projection_id, row, col)

    def choose_seats(session, projection_id):
        Projections.print_projection_seats(projection_id)
        row_and_col = input(
            "Enter the row and the collum separated with \" , \" >")
        row_and_col = (row_and_col.split(","))
        Reservations.reserv_seat(
            session, projection_id, row_and_col[0], row_and_col[1])
        return (row_and_col)
