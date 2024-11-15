from django.shortcuts import render, HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile


from django.contrib.auth.decorators import permission_required

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)


class BookDetailtView(DetailView):
    model = Book
    template_name = 'list_books.html'
    
    def get_book_details(self, request):
        context = super().get_book_details(request)
        book = self.get_objects()
        context['average_rating'] = book.get_average_rating()
        return HttpResponse(request, 'relationship_app/list_books.html', context)
    
        
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    
    
    def get_library_details(self, request):
        context = super().get_library_details(request)
        library = self.get_objects()
        context['library_details'] = library.get_library_details()
        return HttpResponse(request, 'relationship_app/library_detail.html', context)
    
#Create a view that handles form submission and redirects users upon successful registration.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        return redirect(request, 'relationship_app/register.html', {'form': form})
    
    
#Set up role-based access for Admin, Librarian, and Member
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

#Set up role-based view for Admin, Librarian, and Member


#Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome!, Admin'})

#Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome! Librarian'})

#Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome! Member'})

#Add permissions for Book model
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request):
    return render(request, 'relationship_app/delete_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request):
    return render(request, 'relationship_app/change_book.html')