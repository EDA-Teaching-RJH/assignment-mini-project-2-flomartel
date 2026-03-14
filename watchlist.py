
#watchlist class of films added, stored and managed here

class Watchlist: #creates a new watchlist class, for managing the film objects
    def __init__(self):
        self.films = [] #the list is made initially empty before films are added

#for option 2 adding film
    def add_film(self, film): #defines add film function
        self.films.append(film) #.append adds an item to the end of a list

#for option 1 listing watchlist
    def list_films(self): #defines list films function

        if len(self.films) == 0: #checks to see if the list is equal to 0, if it is it prints below
            print("There are no entries in your watchlist!") #if there are 0 entries in the list it prints this
        else:
            for film in self.films: #if self.films =/= 0 it goes back to the empty list i made at the top and prints the entries
                if not film.watched: #now displays either watched or unwatched next to movie in list
                    print(f"| {film.Title} | {film.Genre} | {film.Year} |") #prints the added film from option 2 in a nice table layout, with title,genre,year,watched/unwatched
                    
#lists watched films
    def list_of_watched_films(self):
        watched_found = False
        for film in self.films:
            if film.watched:
                print(f"| {film.Title} | {film.Genre} | {film.Year} |")
                watched_found = True

        if not watched_found:
            print("You haven't watched any films yet. Try adding one")




#for option 3 mark as watched
    def mark_as_watched(self, film_watched):
        for film in self.films:
            if film.Title.lower() == film_watched.lower(): #if film title entered is in film list(also lets film be added in lowercase)
                film.watched = True #then mark the film as watched = true
                print(f"Great choice! {film.Title} has been added to watched films!") #confirms film has been watched to user
                return #exits function and saves value if film is in watchlist
        else: #if film title is not in list
                print(f"Sorry, {film_watched} is not in your list. Try adding it in option 2.") #prompts user to add film to list if not already entered

    #should add something that takes you straight to option 2 if the film isnt already added in the list maybe