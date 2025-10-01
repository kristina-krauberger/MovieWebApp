from models.models import FavouriteMovies, Movies, Users

class DataManager:
    def __init__(self, db):
        self.db = db


    def create_user(self, name):
        if not name or name.strip() == "":  #1. None, .strip() leerzeichen raus, nur "Enter" gedrückt
            return "Invalid input - please type in username."  # Nachricht im

        try:
            new_user = Users(name=name)
            self.db.session.add(new_user)
            self.db.session.commit()
        except ValueError as e:
            return f"{e}"


    def get_users(self):
        users = (self.db.session.query(Users).all())
        return users


    def get_user(self, user_id):
        return self.db.session.query(Users).get(user_id)


    def get_favourite_movies(self, user_id):
        movies = (self.db.session.query(Movies)
                  .join(FavouriteMovies, Movies.id == FavouriteMovies.movie_id)
                  .filter(FavouriteMovies.user_id == user_id)
                  .all())
        return movies


    def add_movie(self, title, director, year, poster_url, user_id):
        # Creates and saves movie-object
        new_movie = Movies(title=title, director=director, year=year,poster_url=poster_url)
        self.db.session.add(new_movie)
        self.db.session.commit()

        # Saves movie to users favourites
        fav = FavouriteMovies(user_id=user_id, movie_id=new_movie.id)
        self.db.session.add(fav)
        self.db.session.commit()


    def update_movie(self, movie_id, new_title):
        movie_to_update = (
            self.db.session.query(Movies)
            .filter(Movies.id == movie_id)
            .one()
        )
        movie_to_update.title = new_title
        self.db.session.commit()


    def delete_movie(self, movie_id):
        self.db.session.query(FavouriteMovies).filter(FavouriteMovies.movie_id == movie_id).delete()
        self.db.session.query(Movies).filter(Movies.id == movie_id).delete()
        self.db.session.commit()