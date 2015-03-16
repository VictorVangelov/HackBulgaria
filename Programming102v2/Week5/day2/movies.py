import sqlite3


class Movies():

    all_movies = [("The Hunger Games: Catching Fire", 7.9),
                  ("Wreck-It Ralph", 7.8), ("Her", 8.3)]

    def create_database(connection, cursor):
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY,
             name TEXT unique,
             rating REAL,
             FOREIGN KEY(id) REFERENCES projections(movie_id))''')
        connection.commit()

    def add(connection, cursor, name, rating):
        cursor.execute(
            '''INSERT INTO movies(name, rating) VALUES(?, ?)''', (name, rating))
        connection.commit()

    def get_all(cursor, connection):
        result = cursor.execute(
            '''SELECT * FROM movies ORDER BY rating desc''')
        for movie in result:
            print("[{}] - {} ({})".format(movie["id"], movie["name"], movie["rating"]))

    def add_old(connection, cursor):
        cursor.executemany(''' INSERT INTO movies(name, rating) VALUES(?,?)''', (Movies.all_movies))
        connection.commit()
