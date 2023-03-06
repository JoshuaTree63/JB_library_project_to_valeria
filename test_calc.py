import unittest
from library_master import Library
from side_calc import Address
import datetime
from book_data import Book
from loan_data import Loan


class TestLibrary(unittest.TestCase):

    def setUp(self):
        library_address = Address("israel", "ramat gan", "shimoni", 1233, 3)
        library_name = "matnes ramt gan"

        self.library = Library(library_name, library_address)

        self.customer_1 = {"id": "001", "first_name": "John", "last_name": "Doe", "address": "456 Elm St.",
                           "email": "johndoe@example.com", "birth_date": 1980}
        self.customer_2 = {"id": "002", "first_name": "Jane", "last_name": "Doe", "address": "789 Oak St.",
                           "email": "janedoe@example.com", "birth_date": 1990}
        self.book_1 = {"id": "101", "name": "Book 1", "author_first_name": "Author", "author_last_name": "One",
                       "year_published": "2010", "book_type": 1}
        self.book_2 = {"id": "102", "name": "Book 2", "author_first_name": "Author", "author_last_name": "Two",
                       "year_published": "2012", "book_type": 2}



class LoanTest(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("123", "12 rolls of life", "david", "piterson", "2019", 1)
        self.book2 = Book("12345", "dogma", "shira", "chohen", "2019", 2)
        self.loan1 = Loan("Customer 1", self.book1, datetime.datetime(2023, 2, 14))
        self.loan2 = Loan("Customer 2", self.book2, datetime.datetime(2023, 2, 1))

    def test_max_to_of_book_loan(self):
        self.assertEqual(self.loan1.max_to_of_book_loan(datetime.datetime(2023, 2, 14)), datetime.datetime(2023, 2, 26))
        self.assertEqual(self.loan2.max_to_of_book_loan(datetime.datetime(2023, 2, 1)), datetime.datetime(2023, 2, 6))


    def test_get_loan_date(self):
        self.assertEqual(self.loan1.get_loan_date(), datetime.datetime(2023, 2, 14))
        self.assertEqual(self.loan2.get_loan_date(), datetime.datetime(2023, 2, 1))

    def test_get_book_id(self):
        self.assertEqual(self.loan1.get_book_id(), 1)
        self.assertEqual(self.loan2.get_book_id(), 2)

    def test_get_customer_id(self):
        self.assertEqual(self.loan1.get_customer_id(), "Customer 1")
        self.assertEqual(self.loan2.get_customer_id(), "Customer 2")

    def test_get_book_type(self):
        self.assertEqual(self.loan1.get_book_type(), 1)
        self.assertEqual(self.loan2.get_book_type(), 2)

    def test_get_return_date(self):
        self.assertIsNone(self.loan1.get_return_date())
        self.assertIsNone(self.loan2.get_return_date())

if __name__ == '__main__':
    unittest.main()



