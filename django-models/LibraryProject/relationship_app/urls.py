from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

#add urls
urlpatterns = [
    path('book/', views.list_books, name='book' ),
    path('bookDetails/', views.BookDetailtView, name='bookDetails'),
    path('libraryDetails/', LibraryDetailView.as_view(), name='libraryDetails'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html')),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html')),
    path('register/', views.register, name='register')
    
]
