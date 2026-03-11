
#watchlist class of films added, stored and managed here

class Watchlist:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)