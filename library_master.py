import os.path
from datetime import datetime, timedelta

from customer_data import Customer
from book_data import Book
from loan_data import Loan
from side_calc import Address


class Library:
    class BookNotFoundError(Exception):
        pass

    class CustomerNotFoundError(Exception):
        pass

    class LoanNotFoundError(Exception):
        pass

    class BookAlreadyExistsError(Exception):
        pass

    class CustomerAlreadyExistsError(Exception):
        pass

    def __init__(self, the_library_name: str, address: Address):

        self._address = address
        self._the_library_name = the_library_name
        self._customer: dict[str, Customer] = {}
        self._books: dict[str, Book] = {}
        self._loans: dict[str, Loan] = {}
        self._returned_loans: dict[str, list[Loan]] = {}
        self._returned_loans: dict[str, list[Loan]] = {}
        self._late_returned_loan: dict[str, list[Loan]] = {}
        self._book: dict[str, str] = {}

    def __str__(self):
        my_print = f' library name: {self._the_library_name}'
        return my_print

    def get_library_name(self):
        return self._the_library_name

    def get_library_address(self):
        return self._address

    def set_library_name(self, new_library_name):
        self._the_library_name = new_library_name

    def set_new_address_for_library(self, address: Address):
        self._address = address

    def add_new_customer(self, customer_id: str, customer_first_name: str, customer_last_name: str, address: Address,
                         email,
                         birth_date: datetime):

        if customer_id in self._customer:
            raise Library.CustomerAlreadyExistsError(f"Customer with ID {customer_id} already exists")
        else:
            new_customer = Customer(customer_id, customer_first_name, customer_last_name, address, email, birth_date)
            self._customer[customer_id] = new_customer
            return True

    def add_new_book(self, book_id: str, book_name: str, author_first_name: str, author_last_name: str,
                     year_published: str, book_type: int):
        if book_id in self._books:
            raise Library.BookAlreadyExistsError(f"The book you enter {book_id}, is already in our Database")
        else:
            new_book = Book(book_id, book_name, author_first_name, author_last_name, year_published, book_type)
            self._books[book_id] = new_book
            return True

    def loan_a_book(self, book, customer_id):
        if book not in self._books:
            raise Library.BookNotFoundError(f"Book with ID {book} not found")
        if customer_id not in self._customer:
            raise Library.CustomerNotFoundError(f"Customer with ID {customer_id} not found")
        else:
            make_a_book_loan = Loan(customer_id, book, datetime)
            self._loans[customer_id] = make_a_book_loan
            return True

    def return_a_book(self, book):
        if book in self._loans:
            self._loans.pop(book)
            return True
        else:
            return False

    def display_all_books(self):
        retrieve_curr_book_list = []
        for book in self._books.values():
            retrieve_curr_book_list.append(str(book))
        return retrieve_curr_book_list

    def display_all_customers(self):
        loans_list = {'date of loan': [],
                      'late returned': [],
                      'date of returned': []
                      }

        for loan in self._loans.values():
            loans_list['date of loan'].append(loan)
        for returned in self._returned_loans.values():
            loans_list['date of returned'].append(returned)
        for late in self._late_returned_loan.values():
            loans_list['late returned'].append(late)
        return loans_list

    def display_all_loans(self):

        retrieve_curr_loans_list = []
        for loan in self._loans.keys():
            retrieve_curr_loans_list.append(loan)
            return retrieve_curr_loans_list
        else:
            return False

    def display_all_late_loans(self):
        retrieve_late_loans_list = []
        for loan in self._loans.keys():
            retrieve_late_loans_list.append(loan)
            return retrieve_late_loans_list
        else:
            return False

    def get_book_by_name(self, book_name):

        if book_name in self._books.keys():
            return self._books[book_name]
        else:
            return False

    def remove_book_from_library(self, book_id: str) -> bool:
        if book_id not in self._books:
            raise Library.BookNotFoundError(f"Book with ID {book_id} not found")
        else:
            self._books.pop(book_id)
            for book in self._loans:
                if book == book_id:
                    self._loans.pop(book_id)
            for customer in self._returned_loans.values():
                for loan in customer:
                    if loan.get_book_id() == book_id:
                        customer.pop(customer.index(loan))
            for customer in self._late_returned_loan.values():
                for loan in customer:
                    if loan.get_book_id() == book_id:
                        customer.pop(customer.index(loan))
            return True

    def find_customer_by_name(self, customer_first_name):
        ret_val = []
        for customer_id, customer in self._customer.items():
            if customer.get_customer_first_name() == customer_first_name:
                ret_val.append(customer)
        return ret_val


    def remove_customer(self, customer_id: str) -> bool:
        if customer_id not in self._customer or customer_id in self._loans:
            raise Library.CustomerAlreadyExistsError(customer_id)
        else:
            self._customer.pop(customer_id)
            return True

    def look_for_a_loan_by_customer(self, customer_id: str):

        if customer_id in self._loans.keys():
            return self._loans[customer_id]
        else:
            return False

    def look_for_abook_by_author(self, book_author_name: str):

        if book_author_name in self._book.keys():
            return self._book[book_author_name]
        else:
            return False






