### operations
**command**
```python
new_book = Book.objects.get(title='1984', author='George Orwell', publication_year=1949)

new_book.title = 'Nineteen Eighty-Four'
new_book.save()
new_book.title

#expected output
'Nineteen Eighty-Four'
