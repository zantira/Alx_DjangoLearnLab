from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm

# Create your views here.


# Views
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_post(request):
    return render(request, 'bookshelf/edit_post.html')

@permission_required('bookshelf.can_create', raise_exception=True)
def create_post(request):
    return render(request, 'bookshelf/create_post.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_post(request):
    return render(request, 'bookshelf/delete_post.html')

@permission_required('bookshelf.can_view', raise_exception=True)
def view_post(request):
    return render(request, 'bookshelf/view_post.html')

# bookshelf/views

def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})


# Insecure - vulnerable to SQL injection
query = "SELECT * FROM my_table WHERE name = '%s'" % ExampleForm

# Secure using Django ORM

results = Book.objects.filter(name=ExampleForm)
