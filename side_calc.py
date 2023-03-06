import re


def check_email(my_email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(regex, my_email):
        return True
    else:
        return False


def is_valid_name(name):
    if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name):
        return True
    else:
        return False


def is_valid_bday(birthday):
    if re.search('^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$', birthday):
        return True
    else:
        return False


def is_digit(nums):
    if re.fullmatch('[0-9]*', nums):
        return True
    else:
        return False


def is_str_valid(letters):
    if re.fullmatch('[A-Za-z]*', letters):
        return True
    else:
        return False


class Address:
    def __init__(self, country, city, street,
                 zip_code, building_num, entrance=None, floor=None):
        self._country = country
        self._floor = floor
        self._entrance = entrance
        self._building_num = building_num
        self._zip_code = zip_code
        self._street = street
        self._city = city

    def __str__(self):
        my_print = f' city: {self._city} street: {self._street} entrance: {self._entrance}' \
                   f' building number: {self._building_num} floor {self._floor} zip: {self._zip_code}'
        return my_print

    def get_country(self):
        return self._country

    def set_country(self, new_country: str):
        self._country = new_country

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
