from django.urls import path
from . import views
from views import LibraryDetailView
from .views import li
urlpatterns = [
    path('book/', views.book_list, name='book' ),
    path('bookDetails/', views.BookDetailtView, name='bookDetails'),
    path('libraryDetails/', LibraryDetailView.as_view(), name='libraryDetails')
]
