
#watchlist class of films added, stored and managed here

class Watchlist:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)


    def list_films(self):
        if len(self.films) == 0:
            print("There are no entries in your watchlist!")
        else:
            for film in self.films:
                print(film.Title)

