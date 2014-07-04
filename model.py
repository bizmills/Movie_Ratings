from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

engine = create_engine("sqlite:///ratings.db", echo=False)
db_session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))

Base = declarative_base()
Base.query = db_session.query_property()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

    # ratings = relationship("Ratings")

class Movie(Base):
    __tablename__= "movies"

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = True)
    released_at = Column(DateTime, nullable = True)
    imdb_url = Column(String(100), nullable = True)

    # ratings = relationship("Ratings")

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable = True)
    #ForeignKey says it references another column in another table
    user_id = Column(Integer, ForeignKey('users.id'), nullable = True)
    rating = Column(Integer, nullable = True)

    #This establish relationship between Rating and User objects with 'backref'
    #These are actually objects, entire user objects and movie objects
    # user and movie objects are accessed through Rating objects
    user = relationship("User", backref=backref("ratings", order_by=id))

    movie = relationship("Movie", backref=backref("ratings", order_by=id))

# ## End class declarations
# def connect():
#     global ENGINE 
#     global Session

#     ENGINE = create_engine("sqlite:///ratings.db", echo=False)
#     Session = sessionmaker(bind=ENGINE)

#     return Session()

def main():
    """In case we need this for something"""

if __name__ == "__main__":
    main()
