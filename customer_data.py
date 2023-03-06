import datetime

import side_calc
from side_calc import *


class Customer:

    def __init__(self, customer_id: str, customer_first_name: str, customer_last_name: str, address: Address, email,
                 birth_date: datetime):

        self._birth_date = birth_date
        self._email = email
        self._address: Address = address
        self._customer_first_name= customer_first_name
        self._customer_last_name = customer_last_name
        self._customer_id = customer_id

    def __str__(self):
        print_me = f'customer first name: {self._customer_first_name},customer first name: {self._customer_last_name}, ' \
                   f'customer ID: {self._customer_id}, customer address ' \
                   f'{self._address}, customer email: {self._email} ' \
               f'customer year of birth: {self._birth_date}'
        return print_me

    def get_birth_date(self):
        return self._birth_date

    def get_email(self):
        return self._email

    def get_address(self):
        return self._address

    def get_customer_first_name(self):
        return self._customer_first_name

    def get_customer_last_name(self):
        return self._customer_last_name

    def get_customer_id(self):
        return self._customer_id

    def set_birth_date(self, your_bday):
        self._birth_date = your_bday

    def set_address(self, address: Address):
        self._address = address

    def set_email(self, your_email):
        if side_calc.check_email(your_email):
            self._email = your_email



