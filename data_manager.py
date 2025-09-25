from models.models import FavouriteMovies, Movies, Users

# alle METHODEN die CRUD operationen durchführen, hier zum Wiederverwenden erstellen
# !! Klassen ohne klammer sind ohne vererbung!
class DataManager:
    def __init__(self, db):
        self.db = db  # merken, welche DB wir verwenden


    def create_user(self, name):
        new_user = Users(name=name)
        self.db.session.add(new_user)
        self.db.session.commit()


    def get_users(self):
        users = (self.db.session.query(Users).all())
        return users


    def get_movies(self, user_id):  # user_id wird übergeben
        movies = (self.db.session.query(Movies)   #movies ist die haupttabelle, von da fange ich an
                  .join(FavouriteMovies, Movies.id == FavouriteMovies.movie_id)  # hier habe ich gejoined!
                  .filter(FavouriteMovies.user_id == user_id)  #user_id wird als parameter übergeben
                  .all())
        return movies


    def add_movie(self, title, director, year, poster_url, user_id):  # was ist movie, was wird her übergeben?
        # 1. Movie-Objekt bauen und speichern
        new_movie = Movies(title=title, director=director, year=year,poster_url=poster_url)
        self.db.session.add(new_movie)
        self.db.session.commit()

        # 2. Favoriten-Verknüpfung speichern
        fav = FavouriteMovies(user_id=user_id, movie_id=new_movie.id)
        self.db.session.add(fav)
        self.db.session.commit()


    def update_movie(self, movie_id, new_title, new_director, new_year, new_poster_url):
        movie_to_update = (
            self.db.session.query(Movies)
            .filter(Movies.id == movie_id)
            .one()
        )
        movie_to_update.title = new_title
        movie_to_update.director = new_director
        movie_to_update.year = new_year
        movie_to_update.poster_url = new_poster_url
        self.db.session.commit()


    def delete_movie(self, movie_id):
        self.db.session.query(Movies).filter(Movies.id == movie_id).delete()
        self.db.session.commit()