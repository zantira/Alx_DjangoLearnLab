from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

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

from .models import Book

def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})
