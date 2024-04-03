from enum import Enum
from datetime import datetime


class Artwork:
    """
    Class representing the artwork at the museum.
    """

    def __init__(self, title, artist, date_of_creation, historical_significance,
                 exhibition_location):  # Initialize Artwork object
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

    def __init__(self, name, exhibition_location, exhibition_duration, is_special_event=False,
                 special_event_ticket_price=None):  # Initialize Exhibition object
        self.name = name
        self.exhibition_location = exhibition_location
        self.exhibition_duration = exhibition_duration
        self.is_special_event = is_special_event
        self.special_event_ticket_price = special_event_ticket_price
        self.artworks = []  # Empty list of artworks

    def addArtwork(self, artwork):  # Add artwork to the exhibition
        if artwork not in self.artworks:
            self.artworks.append(artwork)
        else:
            raise ValueError(f"The artwork '{artwork.title}' is already in the exhibition.")

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
            print(
                f"Artwork: {self.artworks.index(artwork) + 1}. {artwork._title}, Artist: {artwork.__artist}, Date: {artwork.__creation_date}")


class Person:
    """
    Class to represent a person
    (This class is the parent class for Management and Visitor classes)
    """

    def __init__(self, f_name, l_name, age, gender, phone_num):
        # Initialization of person attributes
        self._f_name = f_name
        self._l_name = l_name
        self._age = age
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

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

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

    def __init__(self, f_name, l_name, age, gender, phone_num, nationality, visitorID, email):
        super().__init__(f_name, l_name, age, gender,
                         phone_num)  # Initializing the parent class with common person attributes
        # Initializing attributes of the visitor
        self.__nationality = nationality
        self.__visitorID = visitorID
        self.__email = email
        self._tickets = []  # Stores the Ticket objects since there is an aggregation relationship

    def purchaseTicket(self, numTickets, ticketType, isGroup=False,
                       isSpecialEvent=False):  # Method for online ticket purchase
        ticket = TicketandPricing(numTickets, ticketType, isGroup, isSpecialEvent)  # Create a new Ticket object
        self.addTicket(ticket)  # Add the ticket to the visitor's list of tickets

    def displayVisitorInfo(self):  # Display data about the visitor
        print("Visitor Information:")
        print("Name:", self.get_f_name(), self.get_l_name())
        print("Age:", self.get_age())
        print("Gender:", self.get_gender())
        print("Phone Number:", self.get_phone_num())
        print("Nationality:", self.__nationality)
        print("Visitor ID:", self.__visitorID)
        print("Email:", self.__email)
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

    def __init__(self, f_name, l_name, age, gender, phone_num, employee_id, department, position):
        super().__init__(f_name, l_name, age, gender,
                         phone_num)  # Initializing the parent class with common person attributes
        # Initializing attributes of the management employee
        self.__employee_id = employee_id
        self.__department = department
        self.__position = position

    def displayManagementInfo(self):  # Display data about the management employee
        print("Employee Information:")
        print("Name:", self.get_f_name(), self.get_l_name())
        print("Age:", self.get_age())
        print("Gender:", self.get_gender())
        print("Phone Number:", self.get_phone_num())
        print("Employee ID:", self.__employee_id)
        print("Department:", self.__department)
        print("Position:", self.__position)
        print()


class VisitorsClassification(Enum):
    """
    This class represents the Visitors Classification enumeration
    """
    A = "Adults"
    C = "Children"
    STUDENT = "Students"
    T = "Teachers"
    SENIOR = "Seniors"


class TicketandPricing:
    """
    This class represents the type of ticket purchased by the visitor
    This class is an aggregation relation with the Visitor class
    """

    def __init__(self, numTickets, ticketType, isGroup=False,
                 isSpecialEvent=False):  # Initialize attributes of the ticket
        self.numTickets = numTickets  # Stores the number of tickets
        self.ticketType = ticketType  # Stores the visitor classification for the ticket
        self.isGroup = isGroup  # Indicates if ticket is purchased as a group
        self.isSpecialEvent = isSpecialEvent  # Indicates if ticket is for a special event

    def calculatePrice(self):  # Calculate total price of tickets based on visitor classification and number of tickets
        ticketPrice = 63.0  # Base price
        if self.ticketType in [VisitorsClassification.C, VisitorsClassification.STUDENT, VisitorsClassification.T,
                               VisitorsClassification.SENIOR]:  # Check certain categories eligible for free tickets
            return 0.0  # Free ticket for certain visitor types
        totalPrice = self.numTickets * ticketPrice  # Normal price calculation
        if self.isGroup:
            totalPrice *= 0.5  # 50% discount for groups
        totalPrice += totalPrice * 0.05  # 5% VAT
        return totalPrice

    def isFree(self):  # Check if ticket is free
        return self.calculatePrice() == 0.0
