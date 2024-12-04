import json
from logic import Book, Checker



def user_add_book():
    book_title = str(input("Enter book Title: "))
    book_author = str(input("Enter book Author: "))
    book_year = str(input("Enter book Year: "))
    return Book(book_title, book_author, book_year)

def user_delete_book():
    pass

def user_search_book():
    pass

def user_change_status():
    pass
def user_show_all_books():
    pass 

if __name__ == "__main__":
    library_db = dict()
    print("Welcome to CLI-library-manager")
    
    while True:
        print("1 - Add book\n2 - Delete book by ID \n3 - Search book\n4 - Show all books")
        user_choise = input()
        
        if user_choise == '1':
            checker = Checker()
            new_book = user_add_book()

            result = checker.check_author(new_book), checker.check_title(new_book), checker.check_year(new_book)
        
            # print(type(result))
            print(checker.checker_state)
            if checker.checker_state == '000':
                entry = new_book.add_to_db()
                print(entry)
                library_db.update(entry)
                
                print(library_db)

        elif user_choise == '2':
            user_delete_book()
        elif user_choise == '3':
            user_search_book()
        elif user_choise == '4':
            user_show_all_books()
        else: 
            with open('db.json', 'a', encoding='utf-8') as db:
                json.dump(library_db, db, ensure_ascii=False, indent=4)

            break


