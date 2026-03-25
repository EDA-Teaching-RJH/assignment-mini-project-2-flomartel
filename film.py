#stores data here from each film i put in, title,year,genre,rating

class Cinema: #makes superclass
    def __init__(self,Title,Year):
        self.Title = Title
        self.Year = Year


class Film(Cinema): #creates a new subclass that films added in main project file go into here. later changed to inherit the cinema class
    def __init__(self, Title, Year, Genre):
        super().__init__(Title,Year) #inheriting these values from superclass
        self.Genre = Genre
        self.watched = False #film is added as unwatched
        self.rating = None #film is added as unrated
