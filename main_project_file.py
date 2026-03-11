# Film rating, filtering, and watchlist system project main file

from film import Film #import Film class from film.py file
from watchlist import Watchlist #import Watchlist class from watchlist.py file

watchlist = Watchlist()

while True:

    print("Welcome to your film organisation system!")
    print("1. List Films")
    print("2. Add Film")
    print("3. Mark As Watched")
    print("4. Rate Film")
    print("5. Exit") #all options for the user to select from

    user_choice = input("Please choose an option: ") #user selects an option

    if user_choice == "2":
        Title = input("Please enter film title: ")
        film = Film(Title)
        watchlist.add_film(film)
        print("Film added to list")

        
        

    elif user_choice == "5":
        break