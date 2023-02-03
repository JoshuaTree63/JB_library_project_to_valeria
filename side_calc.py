import re


class Email:

    def __init__(self, my_email):
        self._my_email = my_email

    def check(self, my_email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.fullmatch(regex, my_email):
            return True
        else:
            return False


class Address:
    def __init__(self, country, city, street,
                 zip_code, building_num, entrance=None, floor=None):
        self._floor = floor
        self._entrance = entrance
        self._building_num = building_num
        self._zip_code = zip_code
        self._street = street
        self._city = city

    def get_city(self):
        return self._city

    def get_floor(self):
        return self._floor

    def get_entrance(self):
        return self._entrance

    def get_building_num(self):
        return self._building_num

    def get_zip_code(self):
        return self._zip_code

    def get_street(self):
        return self._street

    def set_city(self, your_city):
        self._city = your_city

    def set_floor(self, your_floor):
        self._floor = your_floor

    def set_entrance(self, your_entrance):
        self._entrance = your_entrance

    def set_building_num(self, your_building_num):
        self._building_num = your_building_num

    def set_zip_code(self, your_zip_code):
        self._zip_code = your_zip_code

    def set_street(self, your_street):
        self._street = your_street


