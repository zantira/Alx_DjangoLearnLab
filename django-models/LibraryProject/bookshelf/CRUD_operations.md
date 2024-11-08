### This instruction is about how to create an instance of a book from the Book model

### create new_book instance operation
***command***
```python
# create operations
new_book = Book(title='1984', author='George Orwell', publication_year=1949)

###expected out
<Book: 1984 by George Orwell>

### Retrieve operations

new_book = Book.objects.get(title='1984', author='George Orwell', publication_year=1949)
new_book.title, new_book.author, new_book.publication_year

#expected output
('1984', 'George Orwell', 1949)


### update operations

new_book = Book.objects.get(title='1984', author='George Orwell', publication_year=1949)

new_book.title = 'Nineteen Eighty-Four'
new_book.save()
new_book.title

#expected output
'Nineteen Eighty-Four'


### Delete operations

#retrieve the book instance
new_book = Book.objects.get(title='Nineteen Eighty-four', author='George Orwell', publication_year=1949)

#delete the book instance
new_book.delete()

#confirm delete
Book.objects.all()

# expected output
<QuerySet []>