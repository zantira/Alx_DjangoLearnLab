"""
A script which contains a query for each of the following queries for the relationship_app
    1. Query all books by a specific author
    2. List all books in a Library
    3. Retrieve a Librarian for a Library
"""

#query all books by a specific author
from relationship_app.models import *
#get author instance by name
author_name = 'name of author'
author = Author.objects.get(name=author_name)

#retrieve all books specific author
books = Book.objects.filter(author=author)

#list all books in the library
library_name = 'name of library'
library = Library.objects.get(name=library_name)
all_books = library.books.all()

#retrieve the name of the librarian
librarian = Librarian.librarian
