import datetime
from side_calc import Address, Email


class Customer:

    def __init__(self, customer_id: str, customer_name: str, address: Address, email, birth_date: datetime):
        self._birth_date = birth_date
        self._email = email
        self._address: Address = address
        self._customer_name = customer_name
        self._customer_id = customer_id

    def get_birth_date(self):
        return self._birth_date

    def get_email(self):
        return self._email

    def get_address(self):
        return self._address

    def get_customer_name(self):
        return self._customer_name

    def get_customer_id(self):
        return self._customer_id

    def set_birth_date(self, your_bday):
        self._birth_date = your_bday

    def set_address(self, address: Address):
        self._address = address

    def set_email(self, your_email: Email):
        if Email.check(your_email):
            self._email = your_email



