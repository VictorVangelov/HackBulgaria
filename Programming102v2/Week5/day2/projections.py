import sqlite3
import json
import reservations
from movies import Movies


class Projections():

    all_projections = [(1, "3D", "2014-04-01", "19:10"),
                       (1, "2D", "2014-04-01", "19:00"),
                       (1, "4DX", "2014-04-02", "21:00"),
                       (3, "2D", "2014-04-05", "20:20"),
                       (2, "3D", "2014-04-02", "22:00"),
                       (2, "2D", "2014-04-02", "19:30")]
    TAKEN_SEAT = "X"
    NUMBER_OF_COLS = 10
    NUMBER_OF_ROWS = 10
    filename = "all_reseravtions.txt"
    dict_of_projections = {}

    def print_projection_seats(projection):
        projection = Projections.dict_of_projections[str(projection)]
        colums = "   "
        for x in range(1, Projections.NUMBER_OF_COLS + 1):
            colums += "{} ".format(str(x))
        print ("".join(colums))
        for col in range(1, Projections.NUMBER_OF_ROWS + 1):
            if col < 10:
                print("{}  {}".format(col, " ".join(projection[str(col)])))
            else:
                print("{} {}".format(col, " ".join(projection[str(col)])))

    def init_free_hall():
        the_len = len(Projections.dict_of_projections)
        Projections.dict_of_projections[the_len + 1] = (Projections.init_new_seats())

    def load_reservations():
        file = open(Projections.filename, "r")
        content = json.load(file)
        for item in content:
            dict_for_reservation = content[item]
            # print(dict_for_reservation)
            Projections.dict_of_projections[item] = dict_for_reservation
            secound_dict = {}
            for row in dict_for_reservation:
                secound_dict[row] = (dict_for_reservation[row])
            Projections.dict_of_projections[item] = secound_dict

    def update_the_json_file():
        file = open(Projections.filename, "w")
        file.write(json.dumps(Projections.dict_of_projections))
        file.close()

    def create_database(connection, cursor):
        spots = Projections.NUMBER_OF_COLS * Projections.NUMBER_OF_ROWS
        cursor.execute('''CREATE TABLE IF NOT EXISTS projections(id INTEGER PRIMARY KEY,
        movie_id INTEGER,
        type TEXT,
        data TEXT,
        time TEXT,
        available_spots INTEGER DEFAULT spots,
        FOREIGN KEY (movie_id) REFERENCES movies(id))''')
        connection.commit()

    def add(cursor, movie_id, projection_type, data, time):
        cursor.execute('''INSERT INTO projections(movie_id, type, data, time) VALUES(?,?,?,?)''',
                       (movie_id, projection_type, data, time))
        Projections.init_free_hall()

    def get_all_for(cursor, id_movie):
        cursor.execute(
            '''SELECT *  FROM projections WHERE movie_id = {}'''.format(id_movie))
        for projections in cursor.fetchall():
            print("[{}] - {}  {}  ({})".format(projections["id"],
                                               projections["data"], projections["time"], projections["type"]))

    def get_all(cursor, connection):
        cursor.execute('''SELECT projections.id, movies.name, projections.data ,projections.time, projections.type
        FROM projections
        INNER JOIN movies
        ON projections.movie_id = movies.id''')
        for projection in cursor.fetchall():
            print("[{}] {} - type : {} - at {} on {}".format(projection["id"],
                                                             projection["name"], projection["type"], projection["time"], projection["data"]))

    def add_old(connection, cursor):
        cursor.executemany(
            ''' INSERT INTO projections(movie_id, type, data, time) VALUES(?,?,?,?)''', (Projections.all_projections))
        connection.commit()
