"""BookSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path

from BookSystem.views.add_author import AddAuthor
from BookSystem.views.add_book import AddBook
from BookSystem.views.add_category import AddCategory
from BookSystem.views.add_publisher import AddPublisher
from BookSystem.views.add_read_book import AddReadBook
from BookSystem.views.approve_book import ApproveBook
from BookSystem.views.author import Author
from BookSystem.views.book import Book
from BookSystem.views.book_authors import BookAuthors
from BookSystem.views.books_for_approval import BooksForApproval
from BookSystem.views.books_in_category import BooksInCategory
from BookSystem.views.category import Category
from BookSystem.views.delete_book import DeleteBook
from BookSystem.views.edit_book import EditBook
from BookSystem.views.home import HomeView
from BookSystem.views.login import LogIn
from BookSystem.views.logout import Logout
from BookSystem.views.publisher import Publisher
from BookSystem.views.read_books_for_user import UserReadBooks
from BookSystem.views.register import Register
from BookSystem.views.suggest_books import SuggestBooks

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('category/', Category.as_view(), name='category'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('author/', Author.as_view(), name='author'),
    path('add_author/', AddAuthor.as_view(), name='add_author'),
    path('publisher/', Publisher.as_view(), name='publisher'),
    path('add_publisher/', AddPublisher.as_view(), name='add_publisher'),
    path('book/', Book.as_view(), name='book'),
    path('add_book/', AddBook.as_view(), name='add_book'),
    path('register/', Register.as_view(), name='register'),
    path('accounts/login/', LogIn.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('category/book/<int:id>/', BooksInCategory.as_view(), name='books_in_category'),
    path('book/add_read/', AddReadBook.as_view(), name='add_read_book'),
    path('book/user/', UserReadBooks.as_view(), name='book_for_user'),
    path('book/suggest/', SuggestBooks.as_view(), name='suggest_book'),
    path('books/approve/', BooksForApproval.as_view(), name='books_for_approval'),
    path('book/approve/', ApproveBook.as_view(), name='approve_book'),
    path('book/edit/<int:id>/', EditBook.as_view(), name='edit_book'),
    path('book/authors/<int:id>/', BookAuthors.as_view(), name='book_authors'),
    path('book/delete/', DeleteBook.as_view(), name='delete_book'),


]
