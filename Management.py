class Management(Person):
    """
    Class representing an employee in the management team of the museum inheriting attributes from Person class
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

    def displayManagementInfo(self): # Display data about the management employee
        print("Employee Details:")
        print("Name:", self.get_f_name(), self.get_l_name())
        print("Gender:", self.get_gender())
        print("Phone Number:", self.get_phone_num())
        print("Employee ID:", self.getEmployeeID())
        print("Department:", self.getDepartment())
        print("Position:", self.getPosition())
        print()
