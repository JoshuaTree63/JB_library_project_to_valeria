from datetime import datetime, timedelta

from customer_data import Customer
from book_data import Book
from loan_data import Loan
from side_calc import Address


class Library:

    def __init__(self, the_library_name: str, address: Address):

        self._address = address
        self._the_library_name = the_library_name
        self._customer: dict[int, Customer] = {}
        self._book: dict[int, Book] = {}
        self._loan: dict[int, Loan] = {}

    def get_library_name(self):
        return self._the_library_name

    def get_library_address(self):
        return self._address

    def set_library_name(self, new_library_name: str):
        self._the_library_name = new_library_name

    def set_new_address_for_library(self, address: Address):
        self._address = address

    def add_new_customer(self, customer_id, customer_name, my_email, address: Address, customer_birth_year: str):

        if customer_id in self._customer:
            return False
        else:
            new_customer = Customer(customer_id, customer_name, address, my_email, customer_birth_year)
            self._customer[customer_id] = new_customer
            return True

    def add_new_book(self, book_id: int, book_name: str, author_name: str, year_published: str, book_type: int):

        if book_id in self._book:
            return False
        else:
            new_book = Book(book_id, book_name, author_name, year_published, book_type)
            self._book[book_id] = new_book
            return True

    def loan_a_book(self, book_id, customer_id):

        if book_id in self._loan and customer_id not in self._customer:
            return False
        else:
            make_a_book_loan = Loan(customer_id, book_id, datetime.today())
            self._loan[customer_id] = make_a_book_loan
            return True








