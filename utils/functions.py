
from database.database_processing import Library, Book

def user_add_book():
    """request user data to create Book entry in data base."""
    book_title = str(input("Enter book Title: ")).lower()
    book_author = str(input("Enter book Author: ")).lower()
    book_year = str(input("Enter book Year: "))
    return Book(book_title, book_author, book_year)

def user_delete_book():
    """Request book ID to delete from database."""
    book_id = str(input("Enter book id for deleting entry: "))
    return book_id

def user_search_book():
    """Request user data for search in database. """
    search_input = str(input("Enter Titile or Author or Year of book need find: ")).lower()
    return search_input

def user_change_status():
    """Request user data - book ID and availability to change entry of book. 
    book_id - ID of book in library database.
    availability - "in_stock" or "in_use"
    """
    book_id = str(input("Enter book id for update availability: "))
    availability = str(input("Enter availability: "))
    return book_id, availability

def user_show_all_books(db):
    """Show all entries in library database"""
    print(db)