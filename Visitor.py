from Person import Person
class Visitor(Person):
    """
    Class representing a visitor inheriting from the Person class
    This class has an aggregation relationship with the Ticket class
    """
    def __init__(self, f_name, l_name, gender, phone_num, age, nationality, visitorId, email):
        super().__init__(f_name, l_name, gender,phone_num)  # Initializing the parent class with common person attributes
        # Initializing attributes of the visitor
        self.__nationality = nationality
        self.__visitorId = visitorId
        self.__email = email
        self._tickets = []  # Stores the Ticket objects since there is an aggregation relationship

    # Setter and getter for visitor attributes
    def setNationality(self, nationality):
        self.__nationality = nationality
    def getNationality(self):
        return self.__nationality

    def setVisitorId(self, visitorId):
        self.__visitorId = visitorId
    def getVisitorId(self):
        return self.__visitorId

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
        print("Visitor ID:", self.getVisitorId())
        print("Email:", self.getEmail())
        print()

    def addTicket(self, ticket):  # Add ticket to visitor's list of tickets
        self._tickets.append(ticket)

    def getTicket(self):  # Returns copy of visitor's list of tickets
        return self._ticket[:]
