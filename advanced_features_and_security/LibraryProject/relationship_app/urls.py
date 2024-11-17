from django.urls import path
from . import views
from .views import LibraryDetailView
# from .views import list_books, admin_view, librarian_view, member_view
# from .views import delete_book, change_book, add_book
from django.contrib.auth.views import LoginView, LogoutView

#add urls
urlpatterns = [
    path('book/', views.list_books, name='book' ),
    path('bookDetails/', views.BookDetailtView, name='bookDetails'),
    path('libraryDetails/', LibraryDetailView.as_view(), name='libraryDetails'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html')),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html')),
    path('register/', views.register, name='register'),
    path('admin_view/', views.admin_view, name='admin_view' ),
    path('member_view/', views.member_view, name='member_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('delete_book/', views.delete_book, name='delete_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('change_book/', views.change_book, name='change_book'),
    path('edit_book/', views.edit_book, name='edit_book')
    
]
