### Delete operations
**command**
```python

from bookshelf.models import Book
#retrieve the book instance
new_book = Book.objects.get(title='Nineteen Eighty-four', author='George Orwell', publication_year=1949)

#delete the book instance
new_book.delete()