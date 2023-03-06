import datetime
from time import strptime

from book_data import Book


class Loan:

    def __init__(self, customer_id: str, book: Book, loan_date: datetime):

        self._loan_date = loan_date
        self._book_id = book.get_book_type()
        self._customer_id = customer_id
        self._book_type = book.get_book_type()
        self._return_date = None

    def __repr__(self):
        my_print = f'customer ID: {self._customer_id} book ID: {self._book_id} book type: {self._book_type} ' \
                   f'loan date: {self._loan_date} return date: {self._return_date}'
        return my_print

    def max_to_of_book_loan(self, date_of_loan: datetime):

        type_time = None

        if self._book_type == 1:
            type_time = datetime.timedelta(days=10)
        elif self._book_type == 2:
            type_time = datetime.timedelta(days=5)
        elif self._book_type == 3:
            type_time = datetime.timedelta(days=2)

        temp_date_of_return = date_of_loan + type_time

        if temp_date_of_return.weekday() == 4:
            temp = temp_date_of_return + datetime.timedelta(days=2)
            self._return_date = temp
            return self._return_date
        elif temp_date_of_return.weekday() == 5:
            temp = temp_date_of_return + datetime.timedelta(days=1)
            self._return_date = temp
            return self._return_date
        else:
            self._return_date = temp_date_of_return
            return self._return_date

    def check_if_over_due(self, date_of_return: datetime):

        if self._return_date < date_of_return.date():
            return True
        else:
            return False

    def get_loan_date(self):
        return self._loan_date

    def get_book_id(self):
        return self._book_id

    def get_customer_id(self):
        return self._customer_id

    def get_book_type(self):
        return self._book_type

    def get_return_date(self):
        return self._return_date












