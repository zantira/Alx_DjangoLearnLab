### Retrieve operations
**command**
```python
new_book = Book.objects.get(title='1984', author='George Orwell', publication_year=1949)
new_book.title, new_book.author, new_book.publication_year

#expected output
('1984', 'George Orwell', 1949)
