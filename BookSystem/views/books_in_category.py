from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render

from BookSystem.services import BookService


class BooksInCategory(View):

    @method_decorator(login_required)
    def get(self, request, id):
        books = BookService.getBooksInCategory(id=id)
        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'books': books,  'adminUsers': adminUsers}
        return render(request, "books_in_category.html", context)

