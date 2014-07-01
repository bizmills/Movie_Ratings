import model
import csv

# from sqlalchemy.orm import sessionmaker


def load_users(session):
    # use u.user
    with open("seed_data/u.user") as f:
        reader = csv.reader(f, delimiter = '|')
        for line in reader:
            # debug counter
            # i = 1
            # if i % 10 == 0:
            #     print i
            user_age = line[1]
            zipcode = line[4]
            user = model.User(age=user_age, zipcode=zipcode)
            session.add(user)
    print session

    

def load_movies(session):
    # use u.item
    pass

def load_ratings(session):
    # use u.data
    pass

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    session.commit()

if __name__ == "__main__":
    s= model.connect()
    main(s)
