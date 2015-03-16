import json
#from reservations import Reservations
import datetime
from movies import Movies
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Projections():

    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("Movies.id", nullable=False))
    type = Column(String)
    data = Column(datetime.date)
    time = Column(datetime.time)
    available_spots = Column(Integer, default=Projections.spots)

    movie = relationship("Movies", backref="projections")

    spots = Projections.NUMBER_OF_COLS * Projections.NUMBER_OF_ROWS
    TAKEN_SEAT = "X"
    NUMBER_OF_COLS = 10
    NUMBER_OF_ROWS = 10
    filename = "all_reseravtions.txt"
    dict_of_projections = {}

    def __str__(self):
        return "{} - {}".format(self.movie_id, self.type, self.data,
                                self.time, self.available_spots)

    def __repr__(self):
        return self.__str__()

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
        Projections.dict_of_projections[
            the_len + 1] = (Projections.init_new_seats())

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

    def add(session, movie_id, projection_type, data, time):
        session.add(Projections(movie_id, projection_type, data, time))
        Projections.init_free_hall()
        session.commit()

    def get_all_for(session, id_movie):
        projections = session.query(Projections).filter(
            Projections.movie_id == id_movie)
        for projection in projections:
            print(projection)

    def get_all(session, ):
        projections = session.query(Projections)
        for projection in projections:
            print(projection)

    def add_old(session):
        session.add_all([Projections(movie_id=1, type="3D", data="2014-04-01", time="19:10"),
                         Projections(movie_id=1, type="2D", data="2014-04-01", time="19:00"),
                         Projections(movie_id=1, type="4DX", data="2014-04-02", time="21:00"),
                         Projections(movie_id=3, type="2D", data="2014-04-05", time="20:20"),
                         Projections(movie_id=2, type="3D", data="2014-04-02", time="22:00"),
                         Projections(movie_id=2, type="2D", data="2014-04-02", time="19:30")])
        session.commit()
