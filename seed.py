import model
import csv
import datetime


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


def load_movies(session):
    # use u.item
    with open("seed_data/u.item") as f:
        reader = csv.reader(f, delimiter = '|')
        for line in reader:
            if line[2]:
                release_date = datetime.datetime.strptime(line[2], "%d-%b-%Y")
            else:
                release_date = None 
            title_list = line[1].split()
            del title_list[-1]
            title = ' '.join(title_list)
            title = title.decode("latin-1")
            movie = model.Movie(name=title, released_at=release_date, imdb_url=line[4])
            session.add(movie)
           

def load_ratings(session):
    # use u.data
    with open("seed_data/u.data") as f:
        reader = csv.reader(f, delimiter="\t")
        for line in reader:
            rating = model.Rating(movie_id = line[0], user_id = line[1], rating = line[2])
            session.add(rating)

# def release_date(str_date): 
#     date_obj = datetime.datetime.strptime(str_date, "%d-%b-%Y")
#     return date_obj

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    load_movies(session)
    load_ratings(session)
    session.commit()

if __name__ == "__main__":
    s= model.connect()
    main(s)
