

from database.database_processing import Library, Book
from utils.functions import user_add_book, user_delete_book, user_search_book, user_show_all_books, user_change_status


if __name__ == "__main__":
    library = Library('database/library.json')
    
    print("Welcome to CLI-library-manager")
    
    while True:
        print("1 - Add book\n2 - Delete book \n3 - Search book\n4 - Show all books\n5 - Change availability of book"
              )
        user_choise = str(input()).lower()
        
        if user_choise == '1':
            library.add_book(user_add_book())
            library.save()
        elif user_choise == '2':
            library.delete_book(user_delete_book())
            library.save()
        elif user_choise == '3':
            print(library.search(user_search_book()))
        elif user_choise == '4':
            user_show_all_books(library)
        elif user_choise == '5':
            library.update_state(user_change_status())
            library.save()
        elif user_choise == 'exit':
            library.save()
            break
        else: 
            continue


