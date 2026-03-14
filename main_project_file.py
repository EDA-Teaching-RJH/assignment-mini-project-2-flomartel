# Film rating, filtering, and watchlist system project main file

from film import Film #import Film class from film.py file
from watchlist import Watchlist #import Watchlist class from watchlist.py file
import re #import REGEX for validating the year and the rating
import csv #imports my recommendations csv file

watchlist = Watchlist()

while True: #sets up while loop
    
    print()
    print("---Welcome to your film organisation system!---")
    print()
    print("--Menu Options--")
    print("1. List Films In Watchlist")
    print("2. List Watched Films")
    print("3. Add Film To Watchlist")
    print("4. Mark Film As Watched")
    print("5. Rate Film")
    print("6. Recommend Me Some Films")
    print("7. Exit Application") #all options for the user to select from

    user_choice = input("Please choose an option: ") #user selects an option

    if user_choice == "1": #if user inputs option 1
        watchlist.list_films() #runs this named function inside the watchlist file

    elif user_choice == "2":
        watchlist.list_of_watched_films() #runs this named function inside the watchlist file


    elif user_choice == "3": #if user inputs option 2

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

    elif user_choice == "4":
        watched_title = input("Please enter a previous film title to mark as watched: ") #promts user for film input
        watchlist.mark_as_watched(watched_title) #searches for film and if found sets film as watched = true



    elif user_choice == "6":
        genre_choice = input("Please choose a genre for some recommendations: ") #asks user for input
        with open("recommendations.csv", "r") as file: #"r" means reading data from the recommendations.csv file
            reader = csv.DictReader(file) #converts a csv file to a python dictionary
            found = False

            count = 0 #count starts at zero
            print("Try these:")
            for row in reader:
                if row["Genre"].lower() == genre_choice.lower(): #using .lower() so it can be entered upper or lowercase
                    print(f"{row['Title']} | {row['Year']}") #prints the Title row and the Year row from the csv file

                    count += 1 #count up by 1
                    if count == 3: #when count gets to 3 break. it will recommend only three films
                        break
            else: #if user enters a not found genre instead of breaking it will print this
                    print("Sorry, no films found under that genre.")



    elif user_choice == "7": #if user chooses 6
        break #stop the code, exit