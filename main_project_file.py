# Film rating, filtering, and watchlist system project main file

from film import Film #import Film class from film.py file
from watchlist import Watchlist #import Watchlist class from watchlist.py file
import re #import REGEX for validating the year and the rating

watchlist = Watchlist()

while True:

    print("Welcome to your film organisation system!")
    print("1. List Films")
    print("2. Add Film")
    print("3. Mark As Watched")
    print("4. Rate Film")
    print("5. Exit") #all options for the user to select from

    user_choice = input("Please choose an option: ") #user selects an option




    if user_choice == "2": #if user chooses option 2

        Title = input("Please enter film title: ")
        Year = input("Please enter film year: ")
        Genre = input("Please enter film genre: ") #asks user for the film title, year, and genre

        film = Film(Title, Year, Genre)
        watchlist.add_film(film) # adds film to watchlist list

        print("Film added to list")

        ######working here - use regex to validate the film year
        

    elif user_choice == "5": #if user chooses 5
        break #stop the code, exit