from django.shortcuts import render, HttpResponse
from models import Book
from .models import Library
from django.views.generic import DetailView

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
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