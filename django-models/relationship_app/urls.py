from django.urls import path
from . import views
from views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

#add urls
urlpatterns = [
    path('book/', views.book_list, name='book' ),
    path('bookDetails/', views.BookDetailtView, name='bookDetails'),
    path('libraryDetails/', LibraryDetailView.as_view(), name='libraryDetails'),
    path('login/', LoginView.as_view(template_name='login.html', name='login')),
    path('logout/', LogoutView.as_view(template_name='logout.html', name='logout')),
    
]
