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

    def displayInfo(self):  # Display data about exhibition and the artworks
        print(f"Exhibition: {self.name}")
        for artwork in self.artworks:
            print(f"Artwork: {self.artworks.index(artwork) + 1}. {artwork._title}, Artist: {artwork.__artist}, Date: {artwork.__creation_date}")




class Person:
    """
    Class to represent a person
    (This class is the parent class for Management and Visitor classes)
    """
    def __init__(self, f_name, l_name, gender, phone_num):
        # Initialization of person attributes
        self._f_name = f_name
        self._l_name = l_name
        self._gender = gender
        self._phone_num = phone_num

    # Setter and getter for person attributes
    def set_f_name(self, f_name):
        self._f_name = f_name
    def get_f_name(self):
        return self._f_name

    def set_l_name(self, l_name):
        self._l_name = l_name
    def get_l_name(self):
        return self._l_name

    def set_gender(self, gender):
        self._gender = gender
    def get_gender(self):
        return self._gender

    def set_phone_num(self, phone_num):
        self._phone_num = phone_num
    def get_phone_num(self):
        return self._phone_num



class Visitor(Person):
    """
    Class representing a visitor inheriting from the Person class
    This class has an aggregation relationship with the Ticket class
    """
    def __init__(self, f_name, l_name, gender, phone_num, age, nationality, visitorID, email):
        super().__init__(f_name, l_name, gender,phone_num)  # Initializing the parent class with common person attributes
        # Initializing attributes of the visitor
        self.__nationality = nationality
        self.__visitorID = visitorID
        self.__email = email
        self._tickets = []  # Stores the Ticket objects since there is an aggregation relationship

    # Setter and getter for visitor attributes
    def setNationality(self, nationality):
        self.__nationality = nationality
    def getNationality(self):
        return self.__nationality

    def setVisitorID(self, visitorID):
        self.__visitorID = visitorID
    def getVisitorID(self):
        return self.__visitorID

    def setEmail(self, email):
        self.__email = email
    def getEmail(self):
        return self.__email

    def displayVisitorInfo(self):  # Display data about the visitor
        print("Visitor Information:")
        print("Name:", self.get_f_name(), self.get_l_name())
        print("Age:", self.getAge())
        print("Gender:", self.get_gender())
        print("Phone Number:", self.get_phone_num())
        print("Nationality:", self.getNationality())
        print("Visitor ID:", self.getVisitorID())
        print("Email:", self.getEmail())
        print()

    def addTicket(self, ticket):  # Add ticket to visitor's list of tickets
        self._tickets.append(ticket)

    def getTicket(self):  # Returns copy of visitor's list of tickets
        return self._ticket[:]





class Management(Person):
    """
    Class representing an employee in the management team of the museum inheriting attributes from Person class
    (This is a child class of the Person class)
    """
    def __init__(self, f_name, l_name, gender, phone_num, employee_id, department, position):
        super().__init__(f_name, l_name, gender, phone_num)  # Initializing the parent class with common person attributes
        # Initializing attributes of the management employee
        self.__employee_id = employee_id
        self.__department = department
        self.__position = position

        # Setter and getter for management employee attributes
    def setEmployeeID(self, employee_id):
        self.__employee_id = employee_id
    def getEmployeeID(self):
        return self.__employee_id

    def setDepartment(self, department):
        self.__department = department
    def getDepartment(self):
        return self.__department

    def setPosition(self, position):
        self.__position = position
    def getPosition(self):
        return self.__position

    def displayManagementInfo(self):  # Display data about the management employee
        print("Employee Information:")
        print("Name:", self.get_f_name(), self.get_l_name())
        print("Age:", self.getAge())
        print("Gender:", self.get_gender())
        print("Phone Number:", self.get_phone_num())
        print("Employee ID:", self.getEmployeeID())
        print("Department:", self.getDepartment())
        print("Position:", self.getPosition())
        print()



class TicketandPricing:
