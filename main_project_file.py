# Film rating, filtering, and watchlist system project main file

from film import Film #import Film class from film.py file
from watchlist import Watchlist #import Watchlist class from watchlist.py file
import re #import REGEX for validating the year and the rating

watchlist = Watchlist()

while True:
    
    print()
    print("---Welcome to your film organisation system!---")
    print()
    print("--Menu Options--")
    print("1. List Films")
    print("2. Add Film")
    print("3. Mark As Watched")
    print("4. Rate Film")
    print("5. Exit") #all options for the user to select from

    user_choice = input("Please choose an option: ") #user selects an option

    if user_choice == "1": #if user inputs option 1
        watchlist.list_films()

    elif user_choice == "2": #if user inputs option 2

        Title = input("Please enter film title: ") #asks user for film title input
        Year = input("Please enter film year: ") #asks user for film year input

        while True:
            if re.match(r"^(19|20)\d{2}$", Year): #uses regex here to validate the year
            #(19|20) meaning that the first two digits are one of these, and \d{2} meaning its followed by two decimal digits
                break #if correct then goes onto the next input, asking for genre
            else:
                Year = input("Please enter a valid year: ") #if year is invalid, asks user for input again

        Genre = input("Please enter film genre: ") #asks user for the genre input

        film = Film(Title, Year, Genre)
        watchlist.add_film(film) # adds film to watchlist list

        print("Film added to list!")

    elif user_choice == "3":
        watched_title = input("Please enter a film title to mark as watched: ")
        watchlist.mark_as_watched(watched_title)

        

    elif user_choice == "5": #if user chooses 5
        break #stop the code, exit