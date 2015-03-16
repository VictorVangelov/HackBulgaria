import sqlite3
from movies import Movies
from projections import Projections


class Reservations():

    all_reservations = [("RadoRado", 1, 2, 1),
                        ("RadoRado", 1, 3, 5),
                        ("RadoRado", 1, 7, 8),
                        ("Ivo", 3, 1, 1),
                        ("Ivo", 3, 1, 2),
                        ("Mysterious", 5, 2, 3),
                        ("Mysterious", 5, 2, 4)]

    def create_database(connection, cursor):
        cursor.execute('''CREATE TABLE IF NOT EXISTS reservations(id INTEGER PRIMARY KEY,
        username TEXT,
        projections_id INTEGER,
        row INTEGER,
        col INTEGER,
        FOREIGN KEY(projections_id) REFERENCES projections(id))
        ''')
        connection.commit()

    def add(cursor, connection, username, projections_id, row, col):
        cursor.execute('''INSERT INTO reservations(username, projections_id, row, col) VALUES(?,?,?,?)''',
                       (username, projections_id, row, col))
        connection.commit()

    def get_all_for(cursor, id_movie):
        result = cursor.execute(
            '''SELECT * FROM reservations WHERE id = ?''', (id_movie))

    def get_all(cursor, connection):
        cursor.execute('''SELECT reservations.username, reservations.col, reservations.row ,  projections.data , projections.time, projections.type
        FROM reservations
        INNER JOIN projections
        ON reservations.projections_id = projections.id''')
        for reseravion in cursor.fetchall():
            print("Username : {}\nSeat {}{}\nDate and Time: {} - {}\nType of the projections : {} \n\n".format(reseravion["username"],
                                                                                                               reseravion["col"], reseravion["row"], reseravion["data"], reseravion["time"], reseravion["type"]))

    def add_old(connection, cursor):
        cursor.executemany(
            ''' INSERT INTO reservations(username, projections_id, row, col) VALUES(?,?,?,?)''', (Reservations.all_reservations))
        connection.commit()

    def init_new_seats():
        dict_of_projec = {}
        for row in range(1, 11):
            dict_of_projec[row] = [
                ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
        return dict_of_projec

    def reserv_seat(cursor, connection, projection_id, row, col):
        if Reservations.validate_row_and_col_input(row, col):
            current_projection = Projections.dict_of_projections[projection_id]
            current_row = current_projection[row]
            if current_row[int(col) - 1] != Projections.TAKEN_SEAT:
                current_row[int(col) - 1] = Projections.TAKEN_SEAT
                print("You take the seat {}-{}".format(row, col))
                Reservations.reduce_available_seats(cursor, connection, projection_id)
            else:
                print("This seat is already taken!")
                return Reservations.choose_seats(cursor, connection, projection_id)
        else:
            print("Lol...NO!")
            return Reservations.choose_seats(cursor, connection, projection_id)

    def reduce_available_seats(cursor, connection, projection):
        proj = int(projection)
        cursor.execute(
            '''UPDATE projections SET available_spots = available_spots -1 WHERE movie_id = ?''', (proj,))
        connection.commit()

    def validate_row_and_col_input(row, col):
        if not (int(row) > Projections.NUMBER_OF_ROWS or int(row) < 1):
            if (int(col) > Projections.NUMBER_OF_COLS or Projections.NUMBER_OF_COLS < 1):
                return False
            else:
                return True
        else:
            return False

    def make_a_reservation(cursor, connection):
        seats = []
        username = input("Enter username > ")
        number_of_tickets = input("Enter the number of tickets > ")
        Movies.get_all(cursor, connection)
        movie_id = input("Choose a projection >")
        Projections.get_all_for(cursor, movie_id)
        projection_id = input("Enter the wanted projection")
        for x in range(1, int(number_of_tickets)+1):
            seats.append(Reservations.choose_seats(cursor, connection, projection_id))
        Reservations.print_reservation(cursor, username, movie_id, projection_id, seats)
        Reservations.confirm(cursor, connection, username, projection_id, seats)

    def print_reservation(cursor, username, movie_id, projection_id, seats):
            cursor.execute('''SELECT movies.name, movies.rating, projections.data, projections.time, projections.type
                FROM movies
                INNER JOIN projections
                ON movies.id = projections.movie_id''')
            reservation = cursor.fetchone()
            reserved_seats = ""
            for seat in seats:
                reserved_seats += str(seats)+"\n"
            print("Movie : {} ({})\n Date And Time : {} {} ({})\n{}".format(reservation["name"],
            reservation["rating"], reservation["data"],
            reservation["time"], reservation["time"], reserved_seats))

    def confirm(cursor, connection, username, projection_id, seats):
        confirm = input("To confirm the reservation - type 'finalize' > ")
        if confirm.lower() == 'finalize':
            for seat in seats:
                Reservations.add(cursor, connection, username, projection_id, seat[0], seat[1])
        elif confirm.lower() == "quit":
            print("You canceld the order, bye bye")
        else:
            print("Lol , u cant type 1 word correctly, try again or type 'Quit'")
            Reservations.confirm(cursor, connection, username, projection_id, row, col)

    def choose_seats(cursor, connection, projection_id):
        Projections.print_projection_seats(projection_id)
        row_and_col = input("Enter the row and the collum separated with \" , \" >")
        row_and_col = (row_and_col.split(","))
        Reservations.reserv_seat(cursor, connection, projection_id, row_and_col[0], row_and_col[1])
        return (row_and_col)
