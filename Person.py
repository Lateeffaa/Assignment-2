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
