#stores data here from each film i put in, title,year,genre,rating


class Film: #creates a new class that films added in main project file go into here
    def __init__(self, Title, Year, Genre):
        self.Title = Title
        self.Year = Year
        self.Genre = Genre
