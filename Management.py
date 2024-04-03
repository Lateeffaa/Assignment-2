class Management:
    """
    Class representing an employee in the management team of the museum
    """

    def __init__(self, fName, lName, age, gender, phoneNum, employeeID, department, position):
        # Initialization of attributes
        self._fName = fName
        self._lName = lName
        self._age = age
        self._gender = gender
        self._phoneNum = phoneNum
        self.__employeeID = employeeID
        self.__department = department
        self.__position = position

    # Setter and getter methods for attributes
    def setFName(self, fName):
        self._fName = fName
    def getFName(self):
        return self._fName

    def setLName(self, lName):
        self._lName = lName
    def getLName(self):
        return self._lName

    def setAge(self, age):
        self._age = age
    def getAge(self):
        return self._age

    def setGender(self, gender):
        self._gender = gender
    def getGender(self):
        return self._gender

    def setPhoneNum(self, phoneNum):
        self._phoneNum = phoneNum
    def getPhoneNum(self):
        return self._phoneNum

    def setEmployeeID(self, employeeID):
        self.__employeeID = employeeID
    def getEmployeeID(self):
        return self.__employeeID

    def setDepartment(self, department):
        self.__department = department
    def getDepartment(self):
        return self.__department

    def setPosition(self, position):
        self.__position = position
    def getPosition(self):
        return self.__position

    def displayManagementInfo(self): # Display data about the management employee
        print("Employee Details:")
        print("Name:", self.getFName(), self.getLName())
        print("Gender:", self.getGender())
        print("Phone Number:", self.getPhoneNum())
        print("Employee ID:", self.getEmployeeID())
        print("Department:", self.getDepartment())
        print("Position:", self.getPosition())
        print()
