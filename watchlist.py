
#watchlist class of films added, stored and managed here

class Watchlist:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film) #.append adds an item to the end of a list


    def list_films(self):
        if len(self.films) == 0: #checks to see if the list is equal to 0, if it is it prints below
            print("There are no entries in your watchlist!") #if there are 0 entries in the list it prints this
        else:
            for film in self.films: #if self.films =/= 0 it goes back to the empty list i made at the top and prints the entries
                print(f"{film.Title} | {film.Genre} | {film.Year}") #prints the added film from option 2 in a nice table layout, with title, genre, and year

