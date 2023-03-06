

class Book:

    def __init__(self, book_id: str, book_name: str, author_first_name: str,author_last_name: str, year_published: str, book_type: int):

        self._author_last_name = author_last_name
        self._year_published = year_published
        self._author_first_name = author_first_name
        self._book_name = book_name
        self._book_id = book_id
        self._book_type = book_type

    def __str__(self):
        print_me = f'book name: {self._book_name}, author first name: {self._author_first_name}, author last name: {self._author_last_name}, ' \
                   f' book id {self._book_id}, book year: {self._year_published} ' \
               f'book type: {self._book_type}'
        return print_me

    def get_book_id(self):
        return self._book_id

    def get_book_name(self):
        return self._book_name

    def get_author_first_name(self):
        return self._author_first_name

    def get_author_last_name(self):
        return self._author_last_name

    def get_year_published(self):
        return self._year_published

    def get_book_type(self):
        return self._book_type















