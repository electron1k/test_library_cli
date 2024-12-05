import uuid
import json

class Checker():

    def __init__(self):
        self.checker_state =''

    def check_author(self, obj):
        if obj.author != ' ' and len(obj.author) > 0:
            self.checker_state += "0"


    def check_title(self, obj):
        if obj.title != ' ' and len(obj.title) > 0:
            self.checker_state += "0"

    
    def check_year(self, obj):
        if obj.year != ' ' and len(obj.year) > 0 and obj.year.isnumeric():
            self.checker_state += "0"




class Book():

    def __init__(self, title, author, year):
        self.id = str(uuid.uuid3(uuid.NAMESPACE_DNS, title))
        self.title = title
        self.author = author
        self.year = year
        self.status = "in_stock"

    def _set_status(self, status): # getters and setters
        self.status = status

    def __repr__(self):
        # return {self.id : {
        #                     "title" : self.title,
        #                     "author": self.author,
        #                     "year": self.year,
        #                     "status": self.status
        #                     }
        #         }
        return f'Book ID:{self.id}\nTitle:{self.title}'

    def add_to_db(self): # need rename
        """ Add new book entry  """
        data = {str(self.id) : {
                            "title" : self.title,
                            "author": self.author,
                            "year": self.year,
                            "status": self.status
                            }
                }
        return data
        # with open('db.json', 'a', encoding='utf-8') as db:
        #     json.dump(data, db, ensure_ascii=False, indent=4)



# book_1 = Book("test2", "Author1", 2000)

# print("id", book_1.id)
# print("year", book_1.year)
# print('status', book_1.status)

# book_1._set_status("in_use")
# book_1 = Book("test2", "Author1", 2000)

# print("id", book_1.id)
# print("year", book_1.year)
# print('status', book_1.status)

# book_1._set_status("in_use")

# print('status', book_1.status)

# # save_book = json.dumps(book_1

# print(book_1)

# book_1.add_to_db()
# print('status', book_1.status)

# # save_book = json.dumps(book_1

# print(book_1)

# print(book_1.__dict__)l
