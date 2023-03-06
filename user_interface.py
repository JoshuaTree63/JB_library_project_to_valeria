import os.path
import pickle

import book_data
import side_calc
from customer_data import Customer
from library_master import Library
from side_calc import *

if __name__ == '__main__':

    library_master = None
    if os.path.exists('library_master.py'):
        with open('library_master.py', 'rb') as f:
            
            library_master = pickle.load(f)
    else:
        library_master = Library()
    try:

        library_address = Address("Israel", "Ramat gan", "Echad Ham", 1234, 6, None, None)
        new_customer_address = Address("Israel", "Ramat gan", "shimouni", 544124, 6, 6, 6)
        my_library = Library("Ramat Gan", library_address)
        librarian_exit = ["x"]

        librarian_choose = int(input(f"Welcome to {Library.get_library_name}, please choose what you want to do\n"
                                     f"1 - Add new book:\n"
                                     f"2 - Add new customer:\n"
                                     f"3 - Find a book by name:\n"
                                     f"4 - Display all loans:\n"
                                     f"5 - Display all late loans:\n"
                                     f"6 - Find loan by specific customer:\n"
                                     f"7 - Find book by author:\n"
                                     f"8 - Find customer by name:\n"
                                     f"9 - Remove a book from library:\n"
                                     f"10 - Remove a customer from library:\n"
                                     f"11 - If you can exit.\n"))

        def librarian_create_a_book():

            while True:
                book_id = input('Insert the book ID: ')
                book_name = input('Insert the book name: ').lower()
                author_last_name = input('Insert author last name: ').lower()
                author_first_name = input('Insert author first name: ').lower()
                year_publish = input('Insert the year of book publish: ')
                book_type = int(input('Insert the book type, "1", "2" or "3": '))
                author_full_name = author_first_name + " " + author_last_name
                if side_calc.is_digit(book_id) is False:
                    print('There is something wrong with the book ID number please try again')
                elif side_calc.is_valid_name(author_full_name) is False:
                    print('There is something wrong with the author name please try again: ')
                elif side_calc.is_digit(year_publish) is False:
                    print('There is something wrong with the year of book publish, try again: ')
                elif book_type not in ("1", "2", "3"):
                    print('Book type can be only "1", "2", or "3". Please try again: ')
                else:
                    new_book = book_data.Book(book_id, book_name, author_first_name, author_last_name, year_publish,
                                              book_type)
                    break
            return new_book


        def librarian_create_new_customer():

            while True:
                last_name = input('Insert customer last name: ').lower()
                first_name = input('Insert customer first name: ').lower()
                customer_id = input('Insert customer id number: ')
                email = input('Insert customer email: ').lower()
                birthday = input('Insert customer birth day in the falling order DD/MM/YYYY:')
                customer_full_name = first_name + " " + last_name
                new_customer_address = Address("Israel", "Ramat gan", "shimouni", 544124, 6, 6, 6)
                if side_calc.is_valid_name(customer_full_name) is False:
                    print('There is something wrong with the customer name please try again:')
                elif side_calc.is_digit(customer_id) is False:
                    print('There is something wrong with the customer ID number please try again:')
                elif side_calc.check_email(email) is False:
                    print('There is something wrong with the customer e-mail please try again: ')
                elif side_calc.is_valid_bday(birthday) is False:
                    print('There is something wrong with the customer birth day please try again: ')
                else:
                    new_customer = Customer(customer_id, first_name, last_name, new_customer_address, email, birthday)
                    return new_customer


        def librarian_look_for_book():

            book_name = input("Enter book name: ")
            temp = my_library.get_book_by_name(book_name)
            if temp is not False:
                return temp
            else:
                return print(f"We dont have {book_name} in our library.")


        def librarian_display_all_loans():

            return my_library.display_all_loans()


        def librarian_display_all_late_loans():
            return my_library.display_all_late_loans()


        def librarian_look_for_loan_for_a_customer():

            customer_id = input("Enter customer ID please: ")
            temp = my_library.get_book_by_name(customer_id)
            if temp is not False:
                return temp
            else:
                return print(f"We dont have {customer_id} in our DB.")


        def librarian_look_for_a_book_by_author():

            librarian_ask = input("Enter author name please: ")
            return my_library.look_for_abook_by_author(librarian_ask)


        def librarian_look_for_a_customer_by_name():

            customer_first_name = input("Enter customer ID please: ")
            temp = my_library.find_customer_by_name(customer_first_name)
            if temp is not False:
                return temp
            else:
                return print(f"We dont have {customer_first_name} in our DB.")


        def librarian_remove_a_book_from_library():

            book_id = input("What is the book ID you want to remove?")
            return my_library.remove_book_from_library(book_id)


        def librarian_remove_a_customer_from_library():

            customer_id = input("What is the customer ID you want to remove?")
            return my_library.remove_customer(customer_id)


        if librarian_choose == 1:
            librarian_look_for_book()
        elif librarian_choose == 2:
            librarian_create_new_customer()
        elif librarian_choose == 3:
            librarian_look_for_book()
        elif librarian_choose == 4:
            librarian_display_all_loans()
        elif librarian_choose == 5:
            librarian_display_all_late_loans()
        elif librarian_choose == 6:
            librarian_look_for_loan_for_a_customer()
        elif librarian_choose == 7:
            librarian_look_for_a_book_by_author()
        elif librarian_choose == 8:
            librarian_look_for_a_customer_by_name()
        elif librarian_choose == 9:
            librarian_remove_a_book_from_library()
        elif librarian_choose == 10:
            librarian_remove_a_customer_from_library()
        elif librarian_choose == 11:
            print("Thanks and see you soon.")
        pass

    except:

        print("error occurred, saving and exiting")
    finally:
        with open('library_master.py', 'wb') as f:
            pickle.dump(library_master, f)
            f.close()
