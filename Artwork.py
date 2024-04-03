class Artwork:
    """
    Class representing the artwork at the museum.
    """
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):  # Initialize Artwork object
        self._title = title
        self.__artist = artist
        self.__date_of_creation = date_of_creation
        self.__historical_significance = historical_significance
        self.__exhibition_location = exhibition_location


class Exhibition:
    """
    Class representing an exhibition at the museum.
    Aggregation relation with Artwork class.
    """
    def __init__(self, name, exhibition_location, exhibition_duration):  # Initialize Exhibition object
        self.name = name
        self.exhibition_location = exhibition_location
        self.exhibition_duration = exhibition_duration
        self.artworks = []  # Empty list of artworks

    def addArtwork(self, artwork):  # Add artwork to the exhibition
        if artwork not in self.artworks:
            self.artworks.append(artwork)
        else:
            print(f"The artwork '{artwork}' is already in the exhibition.")

    def removeArtwork(self, artwork):  # Remove artwork from the exhibition
        try:
            self.artworks.remove(artwork)
        except ValueError:
            print(f"The artwork '{artwork}' is not in the exhibition.")

    def getArtworks(self):  # Gets and returns the list of artworks in the exhibition
        return self.artworks

    def getTotalArtworks(self):  # Gets and returns the total number of artworks in the exhibition
        return len(self.artworks)
      
