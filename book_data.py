

class Book:

    def __init__(self, book_id: str, book_name: str, author_name: str, year_published: str):

        self._year_published = year_published
        self._author_name = author_name
        self._book_name = book_name
        self._book_id = book_id

        self._book_type = {1: 10,
                     2: 5,
                     3: 2}

    def get_book_id(self):
        return self._book_id

    def get_book_name(self):
        return self._book_name

    def get_author_name(self):
        return self._author_name

    def get_year_published(self):
        return self._year_published

    def get_book_type(self, book_id):
        if book_id in self._book_id:
            return self._book_type












