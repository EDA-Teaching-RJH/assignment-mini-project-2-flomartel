
#watchlist class of films added, stored and managed here. then changed into just every option being controlled from here
import csv
import random #imports random external library
from film import Film

class Watchlist: #creates a new watchlist class, for managing the film objects
    def __init__(self):
        self.films = [] #the list is made initially empty before films are added

    def save_to_csv(self):
        with open ("watchlist.csv", "w", newline="") as file: #open watchlist.csv in write mode on newline
            writer = csv.writer(file) #writes data to watchlist.csv
            writer.writerow(["Title", "Year", "Genre", "Watched", "Rating"]) #write the header
            #struggled here header kept getting deleted but fixed eventualy
            for film in self.films:
                writer.writerow([ #used to write the row of data into the csv file
                    film.Title,
                    film.Year,
                    film.Genre,
                    film.watched,
                    film.rating


            ])

    def load_from_csv(self): 
        with open("watchlist.csv", "r", newline="") as file: #open watchlist.csv as a read file, newline=starts new line
            reader = csv.DictReader(file) #reads data from the csv file
            for row in reader:
                watched = row["Watched"] == "True"
                rating = float(row["Rating"]) if row["Rating"] not in ("", "None") else None #if number then convert to float(decimal) if no then set as None

                film = Film(
                    row["Title"],row["Year"],row["Genre"] #creates new film object
                )
                film.watched = watched
                film.rating = rating
                self.films.append(film) #append data


#for option 3 adding film to watchlist
    def add_film(self, film): #defines add film function
        for existing in self.films:
            if existing.Title.lower() == film.Title.lower():
                print(f"{film.Title} is already in your watchlist!") #if the user adds a film already in watchlist dont add again
                return
        
        self.films.append(film) #.append adds an item to the end of a list

        with open("watchlist.csv", "a", newline="") as file: #appending new data on a new line using "a" and newline
            writer = csv.writer(file) #writes data to the csv file watchlist.csv
            writer.writerow([ #used to write a row of data into these catagories in the csv file
                film.Title,
                film.Year,
                film.Genre,
                film.watched,
                film.rating
            ])
        self.save_to_csv() ####saves film to csv file watchlist.csv
        print(f"{film.Title} has been added to watchlist!") #if film not already in watchlist print this
#for option 1 listing watchlist
    def list_films(self): #defines list films function

        if len(self.films) == 0: #checks to see if the list is equal to 0, if it is it prints below
            print("There are no entries in your watchlist!") #if there are 0 entries in the list it prints this
        else:
            for film in self.films: #if self.films =/= 0 it goes back to the empty list i made at the top and prints the entries
                if not film.watched: #now displays either watched or unwatched next to movie in list
                    print(f"| {film.Title} | {film.Genre} | {film.Year} |") #prints the added film from option 2 in a nice table layout, with title,genre,year,watched/unwatched
                    
#for option 2 lists watched films
    def list_of_watched_films(self):
        watched_found = False
        for film in self.films:
            if film.watched:
                print(f"| {film.Title} | {film.Genre} | {film.Year} | ☆ {film.rating}/5☆ |")
                watched_found = True

        if not watched_found:
            print("You haven't watched any films yet. Try adding one!")

#for option 3 mark as watched
    def mark_as_watched(self, film_watched):
        for film in self.films:
            if film.Title.lower() == film_watched.lower(): #if film title entered is in film list(also lets film be added in lowercase)
                film.watched = True #then mark the film as watched = true
                print(f"Great choice! {film.Title} has been added to watched films!") #confirms film has been watched to user
                self.save_to_csv() #####
                return #exits function and saves value if film is in watchlist
        else: #if film title is not in list
                print(f"Sorry, {film_watched} is not in your list. Try adding it in option 3.") #prompts user to add film to list if not already entered

    #should add something that takes you straight to option 2 if the film isnt already added in the list maybe


# for option 5 rate film
    def rating_film(self,user_title,user_rating):
        for film in self.films: #calls back up to watchlist made
            if film.Title.lower() == user_title.lower(): #finds user input title from film list. can also be input in lowercase
            
                if not film.watched:
                    print("Sorry, this film is not in your watched list. Please watch the film before rating it.")
                    return #if film is in watchlist but not watched films, promt user to watch before rating
            
                film.rating = user_rating
                print(f"Awesome! {film.Title} has been rated at {user_rating}!") #lets user know film has been rated
                self.save_to_csv()####
                return
        else:
            print(f"Sorry, {user_title} is not in any list.")#if user input is not in any list it prints this


#using the "random" external library to choose a random film from my watchlist
    def random_film(self):
        if len(self.films) == 0: #if no films in watchlist print no films
            print("There are no films to choose from in your watchlist")
            return #return data
        
        film = random.choice(self.films) #choose random film from film watchlist
        print(f"Try watching: {film.Title} | {film.Year}") #print the film in this layout


