class Artwork:
  def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
    self._title = title
    self.__artist = artist
    self.__date_of_creation = date_of_creation
    self.__historical_significance = historical_significance
    self.__exhibition_location = exhibition_location


class Exhibition:
  def __init__(self, name, exhibition_location, exhibition_duration):
    self.name = name
    self.exhibition_location = exhibition_location
    self.exhibition_duration = exhibition_duration
    self.artworks = []

  def addArtwork(self, artwork):
    self.artworks.append(artwork)

  def removeArtwork(self, artwork):
    self.artworks.remove(artwork)
    
