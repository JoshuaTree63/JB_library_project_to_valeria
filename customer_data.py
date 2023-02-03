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
        if Email.check(your_email) is True:
            self._email = your_email


if __name__ == '__main__':
    my_address = Address("israel", "Ramat Gan", "shimouni", 52214, 3, 1, 0)
    this_is_my_email_test = Email("Joshua.Levi63@gmail.com")
    try_me = Customer("038773321", "Joshua", my_address, this_is_my_email_test, 1983)

    print(try_me, this_is_my_email_test)