# Film rating, filtering, and watchlist system project main file
from film import Film
from watchlist import Watchlist

watchlist = Watchlist()

while True:

    print("Welcome to your film organisation system!")
    print("1. List Films")
    print("2. Add Film")
    print("3. Mark As Watched")
    print("4. Rate Film")
    print("5. Exit")

    user_choice = input("Please choose an option: ")


    if user_choice == "5":
        break