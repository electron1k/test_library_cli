
import json

class Book():

    def __init__(self, id, title, author, year):
        self.id = id
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


book_1 = Book(1, "test1", "Author1", 2000)

print("id", book_1.id)
print("year", book_1.year)
print('status', book_1.status)

book_1.set_status("in_use")

print('status', book_1.status)

# save_book = json.dumps(book_1

print(book_1)

