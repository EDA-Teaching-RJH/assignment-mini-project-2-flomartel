**Developer Journal for Film Watchlist Project**
For this assignment I decided to make a film organisation and rating system, as this is of high interest for me because I love watching and reviewing films. 


**Object-Oriented Programming**
My two classes are Watchlist and Film. The Film class I created first within the film.py file. This class represents a singular film when it is added by the user through the main menu when the main_project_file.py is run. When a new film object is created at this point, the init constructor method “ __init__”  is used to initialise the attributes Title, Year, and Genre. I also added two other attributes which were watched = False and rating = None. The main project file will create this film object through option 3.Add Film to Watchlist, this is done through "from film import Film" and " from watchlist import Watchlist". After the main file creates the film object this is then sent to my Watchlist class under a new file called watchlist.py (through the code watchlist.add_film(film)).This demonstrates the use of Object-Oriented Programming by organising the program into clearly defined classes under different files. The Film object represents individual films, and the Watchlist class manages the whole collection of these objects. This was introduced in lecture 9, specifically slide 16 where it is shown how to set up a class. I then slightly expanded on this and changed my film class to use inheritance, which is covered in the same lecture, and slide 24 was the most helpful to my work. I created the "Cinema" superclass with the attributes of title and year. I then made the original "Film" class from before inherit these two attributes from the superclass, but added genre, watched status and rating.

**File I/O**
The first time I implemented file I/O into this assignment was when I created the recommendations.csv file. Here I created a menu option that 





