
import json
import uuid


class Library():
    """" Main Library database class. """
    def __init__(self, data_file):
        # self.data = data_file
        with open(f'{data_file}', 'r', encoding='utf-8') as db:
            try:
                self.data =json.load(db)
            except Exception:
                self.data = dict()

        # return data
    
    def __repr__(self):
        return f'In Library {self.data}'
    
    def add_book(self, obj):
        """" Adding book to library data base """
        checker = Checker()
            
        checker.check_author(obj) 
        checker.check_title(obj) 
        checker.check_year(obj)
    
        if checker.checker_state == '000':
            entry = obj.entry_for_db()
            print("Book successfully added")
            return self.data.update(entry)
        else:
            print("Wrong format of entered data")
            
    def delete_book(self, book_id: str):
        """" Delete book from library database """
        try:
            del self.data[book_id]
            print("Book successfully deleted.")
        except KeyError:
            print("Book with id {book_id} didnt found.")
            
    def update_state(self, user_input: tuple):
        """" Change availability book in library database """
        try:
            self.data[user_input[0]][3] = user_input[1]
        except KeyError:
            print("Book with id {user_input[0]} didnt found.")
            
    def search(self, user_input: str) -> list:
        """" Search  book or books in library database """
        result = list()
        for book_id, entry in self.data.items():
            if user_input in entry:
            # print(f"{k} value {v}")
                result.append(f"{book_id} - {entry}")
        if len(result) > 0:
            return result
        else:
            return "Not found"
        

    def save(self):
        """Save all entries to JSON file"""
        with open('database/library.json', 'w', encoding='utf-8') as db:
            json.dump(self.data, db, ensure_ascii=False, indent=4)
            
            

class Checker():
    """Checking instance of book for correct data in fields. """
    def __init__(self):
        self.checker_state =''

    def check_author(self, obj):
        """Check author"""
        if obj.author != ' ' and len(obj.author) > 0:
            self.checker_state += "0"


    def check_title(self, obj):
        """Check title"""
        if obj.title != ' ' and len(obj.title) > 0:
            self.checker_state += "0"

    
    def check_year(self, obj):
        """Check year"""
        if obj.year != ' ' and len(obj.year) > 0 and obj.year.isnumeric():
            self.checker_state += "0"




class Book():

    def __init__(self, title, author, year):
        """Create instance of book.
        id - generates by uuid on title and author 
        title - name of book
        author - name of book author
        year - year of book was written
        status - availability in library

        """
        self.id = str(uuid.uuid3(uuid.NAMESPACE_DNS, name= title + author))
        self.title = title
        self.author = author
        self.year = year
        self.status = "in_stock"

    def __repr__(self):
        return f'Book ID:{self.id}\nTitle:{self.title}'

    def entry_for_db(self) -> dict: 
        """Create right format of user data for adding in database"""
        data = {str(self.id) : [
                            self.title,
                            self.author,
                            self.year,
                            self.status
                        ]               
                }
        return data