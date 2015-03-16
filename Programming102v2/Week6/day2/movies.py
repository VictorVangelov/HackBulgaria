from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from projections import Projections


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, ForeignKey("Projections.movie_id", primary_key=True))
    name = Column(String, nullable=False, unique=True)
    rating = Column(Float, default=0)

    def __str__(self):
        return "{} - {} - {}".format(self.id, self.name, self.rating)

    def __repr__(self):
        return self.__str__()

    def add(session, name, rating):
        session.add(Movie(name, rating))
        session.commit()

    def get_all(session):
        movies = session.query(Movies)
        for movie in movies:
            print(movie)

    def add_old(session):
        session.add_all([
            Movie("The Hunger Games: Catching Fire", 7.9),
            Movie("Wreck-It Ralph", 7.8),
            Movie("Her", 8.3)
            ])
        session.commit()
