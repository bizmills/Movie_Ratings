from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker 
from datetime import datetime

ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

class Movie(Base):
    __tablename__= "movies"

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = True)
    released_at = Column(DateTime, nullable = True)
    imdb_url = Column(String(100), nullable = True)

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    movie_id = Column(Integer, nullable = True)
    user_id = Column(Integer, nullable = True)
    rating = Column(Integer, nullable = True)

### End class declarations
def connect():
    global ENGINE 
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=False)
    Session = sessionmaker(bind=ENGINE)

    return Session()

# NON FUNCTIONING STRING PARSING FOR RELEASED_AT
# def datetime(str_date): 
#     date_obj = datetime.datetime.strptime(str_date, "%d-%b-%Y")
#     return date_obj

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
